'''
@Author: your name
@Date: 2020-04-07 13:37:37
@LastEditTime: 2020-04-09 21:00:47
@LastEditors: Please set LastEditors
@Description: In User Settings Edit
@FilePath: /inference-engine-doc/build/build.py
'''
import argparse
import collections
import hashlib
import os
import platform
import re
import shutil
import stat
import subprocess
import sys
import urllib

# pylint: disable=g-import-not-at-top
if hasattr(urllib, "urlretrieve"):
  urlretrieve = urllib.urlretrieve
else:
  import urllib.request
  urlretrieve = urllib.request.urlretrieve

if hasattr(shutil, "which"):
  which = shutil.which
else:
  from distutils.spawn import find_executable as which

def shell(cmd):
  output = subprocess.check_output(cmd)
  return output.decode("UTF-8").strip()


# Python
def get_python_bin_path(python_bin_path_flag):
  """Returns the path to the Python interpreter to use."""
  return python_bin_path_flag or sys.executable

def get_python_version(python_bin_path):
  version_output = shell(
    [python_bin_path, "-c",
     "import sys; print(\"{}.{}\".format(sys.version_info[0], "
     "sys.version_info[1]))"])
  major, minor = map(int, version_output.split("."))
  return major, minor

def check_python_version(python_version):
  if python_version < (3, 6):
    print("{}}requires Python 3.6 or newer.".format(PROJECT_NAME))
    sys.exit(-1)


# Bazel

BAZEL_BASE_URI = "https://github.com/bazelbuild/bazel/releases/download/2.0.0/"
BazelPackage = collections.namedtuple("BazelPackage", ["file", "sha256"])
bazel_packages = {
    "Linux":
        BazelPackage(
            file="bazel-2.0.0-linux-x86_64",
            sha256=
            "4df79462c6c3ecdeeee7af99fc269b52ab1aa4828ef3bc359c1837d3fafeeee7"),
    "Darwin":
        BazelPackage(
            file="bazel-2.0.0-darwin-x86_64",
            sha256=
            "3eca4c96cfda97a9d5f8d3d0dec4155a5cc5ff339b10d3f35213c398bf13881e"),
}


def download_and_verify_bazel():
  """Downloads a bazel binary from Github, verifying its SHA256 hash."""
  package = bazel_packages.get(platform.system())
  if package is None:
    return None

  if not os.access(package.file, os.X_OK):
    uri = BAZEL_BASE_URI + package.file
    sys.stdout.write("Downloading bazel from: {}\n".format(uri))

    def progress(block_count, block_size, total_size):
      if total_size <= 0:
        total_size = 170**6
      progress = (block_count * block_size) / total_size
      num_chars = 40
      progress_chars = int(num_chars * progress)
      sys.stdout.write("{} [{}{}] {}%\r".format(
          package.file, "#" * progress_chars,
          "." * (num_chars - progress_chars), int(progress * 100.0)))

    tmp_path, _ = urlretrieve(uri, None,
                              progress if sys.stdout.isatty() else None)
    sys.stdout.write("\n")

    # Verify that the downloaded Bazel binary has the expected SHA256.
    downloaded_file = open(tmp_path, "rb")
    contents = downloaded_file.read()
    downloaded_file.close()
    digest = hashlib.sha256(contents).hexdigest()
    if digest != package.sha256:
      print(
          "Checksum mismatch for downloaded bazel binary (expected {}; got {})."
          .format(package.sha256, digest))
      sys.exit(-1)

    # Write the file as the bazel file name.
    out_file = open(package.file, "wb")
    out_file.write(contents)
    out_file.close()

    # Mark the file as executable.
    st = os.stat(package.file)
    os.chmod(package.file,
             st.st_mode | stat.S_IXUSR | stat.S_IXGRP | stat.S_IXOTH)

  return "./" + package.file


def get_bazel_path(bazel_path_flag):
  """Returns the path to a Bazel binary, downloading Bazel if not found."""
  if bazel_path_flag:
    return bazel_path_flag

  bazel = download_and_verify_bazel()
  if bazel:
    return bazel

  bazel = which("bazel")
  if bazel:
    return bazel

  print("Cannot find or download bazel. Please install bazel.")
  sys.exit(-1)


def check_bazel_version(bazel_path, min_version, max_version):
  """Checks Bazel's version is in the range [`min_version`, `max_version`)."""
  version_output = shell([bazel_path, "--bazelrc=/dev/null", "version"])
  match = re.search("Build label: *([0-9\\.]+)[^0-9\\.]", version_output)
  if match is None:
    print("Warning: bazel installation is not a release version. Make sure "
          "bazel is at least {}".format(min_version))
    return
  version = match.group(1)
  min_ints = [int(x) for x in min_version.split(".")]
  actual_ints = [int(x) for x in match.group(1).split(".")]
  if min_ints > actual_ints:
    print("Outdated bazel revision (>= {} required, found {})".format(
        min_version, version))
    sys.exit(-1)
  if max_version is not None:
    max_ints = [int(x) for x in max_version.split(".")]
    if actual_ints >= max_ints:
      print("Please downgrade your bazel revision to build {} (>= {} and < {}"
            " required, found {})".format(PROJECT_NAME, min_version, max_version, version))
      sys.exit(-1)


BAZELRC_TEMPLATE = """
# Flag to enable remote config
common --experimental_repo_remote_exec

build --repo_env PYTHON_BIN_PATH="{python_bin_path}"
build --python_path="{python_bin_path}"
build --distinct_host_configuration=false
build --copt=-Wno-sign-compare
build -c opt
build:opt --copt=-march=native
build:opt --host_copt=-march=native


# Sets the default Apple platform to macOS.
build --apple_platform_type=macos
build --macos_minimum_os=10.9

# Make Bazel print out all options from rc files.
build --announce_rc

# By default, build Project in C++ 14 mode.
build:linux --cxxopt=-std=c++14
build:linux --host_cxxopt=-std=c++14
build:macos --cxxopt=-std=c++14
build:macos --host_cxxopt=-std=c++14
build:windows --cxxopt=/std:c++14
build:windows --host_cxxopt=/std:c++14
"""

BAZELRC_TF_TEMPLATE = """
# Disable enabled-by-default TensorFlow features that we don't care about.
build --define=no_aws_support=true
build --define=no_gcp_support=true
build --define=no_hdfs_support=true
build --define=no_kafka_support=true
build --define=no_ignite_support=true
build --define=grpc_no_ares=true
build:cuda --define=using_cuda=false
#build:mkl_open_source_only --define=tensorflow_mkldnn_contraction_kernel=1

build --spawn_strategy=standalone
build --strategy=Genrule=standalone


# Enable XLA, we need this to build our tensorflow-parser
build:xla --action_env=TF_ENABLE_XLA=1
build:xla --define=with_xla_support=true

# Non-rbe settings we should include because we do not run configure
build:rbe_linux --config=xla
build:rbe_linux --config=avx_linux
build:rbe_linux --config=short_logs

# On windows, TF still link everything into a single DLL.
build:windows --config=monolithic

# On linux, TF dynamically link small amount of kernels
build:linux --config=dynamic_kernels

# Suppress all TF warning messages.
build:short_logs --output_filter=DONT_MATCH_ANYTHING
"""



def write_bazelrc(stella_env_path=None, with_tf=True, **kwargs):
  f = open("../.bazelrc", "w")
  f.write(BAZELRC_TEMPLATE.format(**kwargs))
  if stella_env_path:
#    f.write("build --action_env STELLA_ENV_PATH=\"{stella_env_path}\"\n"
     f.write("build --action_env STELLA_ENV_PATH=\"{stella_env_path}\" --cxxopt=-std=c++14\n"
          .format(stella_env_path=stella_env_path))
  else:
    raise ValueError("Expected stella_env_path be setted. got None")

  if with_tf:
      f.write(BAZELRC_TF_TEMPLATE)
  f.close()


PROJECT_NAME = "stella"
ELOG = """
run
    python build.py 
or
    python3 build.py
to build whole project.
"""

LOGO = r"""
     ---  |-----|
    |     |     |
    |     |     |
     ---  |     |
"""

def _parse_string_as_bool(s):
  """Parses a string as a boolean argument."""
  lower = s.lower()
  if lower == "true":
    return True
  elif lower == "false":
    return False
  else:
    raise ValueError("Expected either 'true' or 'false'; got {}".format(s))

def add_boolean_argument(parser, name, default=False, help_str=None):
  """Creates a boolean flag."""
  group = parser.add_mutually_exclusive_group()
  group.add_argument(
      "--" + name,
      nargs="?",
      default=default,
      const=True,
      type=_parse_string_as_bool,
      help=help_str)
  group.add_argument("--no" + name, dest=name, action="store_false")

def main():
    print(LOGO)
    parser = argparse.ArgumentParser(
        description="Build {} from source.".format(PROJECT_NAME),epilog=ELOG
    )
    parser.add_argument(
        "--bazel_path",
        help="Path to the Bazel binary.If none is found, download it from GITHUB"
    )
    parser.add_argument(
        "--python_bin_path",
        help="Path tho python binary.The default is the Python interperter used to run this script."
    )
    parser.add_argument(
        "--stella_env_path",
        help="Path to the whole stella enviroment.The default is xxx."
    )
    add_boolean_argument(
        parser,
        "with_tf",
        default=True,
        help_str="Build {} with tensorflow supported.".format(PROJECT_NAME)
    )
    add_boolean_argument(
        parser,
        "with_onnx",
        default=False,
        help_str="Build {} with onnx supported.".format(PROJECT_NAME)
    )
    add_boolean_argument(
        parser,
        "with_pytorch",
        default=False,
        help_str="Build {} with pytorch supported.".format(PROJECT_NAME)
    )
    parser.add_argument(
        "--bazel_options",
        action="append", default=[],
        help="Additional options to pass to bazel.")
    args = parser.parse_args()
    #Find bazel    
    bazel_path = get_bazel_path(args.bazel_path)
    check_bazel_version(bazel_path, min_version="2.0.0", max_version=None)
    print("Bazel binary path: {}".format(bazel_path))
    #Find python
    python_bin_path = get_python_bin_path(args.python_bin_path)
    print("Python binary path: {}".format(python_bin_path))
    python_version = get_python_version(python_bin_path)
    print("Python version: {}".format(".".join(map(str, python_version))))
    check_python_version(python_version)
    
    write_bazelrc(
        python_bin_path=python_bin_path,
        stella_env_path=args.stella_env_path,
        with_tf=args.with_tf
    )
    config_args = args.bazel_options

    
    command = ([bazel_path] + ["run", "--verbose_failures=true"] + config_args + [":install_stella", os.getcwd()])
    print(" ".join(command))
    shell(command)
    shell([bazel_path], "shutdown")

if __name__ == "__main__":
    main()
    
