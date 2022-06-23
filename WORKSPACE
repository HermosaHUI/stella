workspace(name = "stella-1.0")

load("@bazel_tools//tools/build_defs/repo:http.bzl", "http_archive")
load("@bazel_tools//tools/build_defs/repo:utils.bzl", "maybe")
load("//third_party:repo.bzl", "tf_http_archive", "tf_mirror_urls")

http_archive(
    name = "io_bazel_rules_closure",
    sha256 = "9498e57368efb82b985db1ed426a767cbf1ba0398fd7aed632fc3908654e1b1e",
    strip_prefix = "rules_closure-0.12.0",
    urls = [
        "https://mirror.bazel.build/github.com/bazelbuild/rules_closure/archive/0.12.0.tar.gz",
        "https://github.com/bazelbuild/rules_closure/archive/0.12.0.tar.gz",
    ],
)

load("@io_bazel_rules_closure//closure:repositories.bzl", "rules_closure_dependencies", "rules_closure_toolchains")
#rules_closure_dependencies()
#rules_closure_toolchains()


http_archive(
    name = "bazel_skylib",
    urls = [
        "https://mirror.bazel.build/github.com/bazelbuild/bazel-skylib/releases/download/1.2.1/bazel-skylib-1.2.1.tar.gz",
        "https://github.com/bazelbuild/bazel-skylib/releases/download/1.2.1/bazel-skylib-1.2.1.tar.gz",
    ],
    sha256 = "f7be3474d42aae265405a592bb7da8e171919d74c16f082a5457840f06054728",
)
load("@bazel_skylib//:workspace.bzl", "bazel_skylib_workspace")
#bazel_skylib_workspace()


http_archive(
    name = "rules_cc",
    urls = ["https://github.com/bazelbuild/rules_cc/releases/download/0.0.1/rules_cc-0.0.1.tar.gz"],
    sha256 = "4dccbfd22c0def164c8f47458bd50e0c7148f3d92002cdb459c2a96a68498241",
)

http_archive(
    name = "build_bazel_rules_swift",
    sha256 = "a2fd565e527f83fb3f9eb07eb9737240e668c9242d3bc318712efa54a7deda97",
    url = "https://github.com/bazelbuild/rules_swift/releases/download/0.27.0/rules_swift.0.27.0.tar.gz",
)

#load(
#    "@build_bazel_rules_swift//swift:repositories.bzl",
#    "swift_rules_dependencies",
#)

#swift_rules_dependencies()

#load(
#    "@build_bazel_rules_swift//swift:extras.bzl",
#    "swift_rules_extra_dependencies",
#)

#swift_rules_extra_dependencies()

http_archive(
    name = "build_bazel_rules_apple",
    sha256 = "12865e5944f09d16364aa78050366aca9dc35a32a018fa35f5950238b08bf744",
    url = "https://github.com/bazelbuild/rules_apple/releases/download/0.34.2/rules_apple.0.34.2.tar.gz",
)


#load(
#    "@build_bazel_rules_apple//apple:repositories.bzl",
#    "apple_rules_dependencies",
#)

#apple_rules_dependencies()

http_archive(
    name = "build_bazel_apple_support",
    sha256 = "5bbce1b2b9a3d4b03c0697687023ef5471578e76f994363c641c5f50ff0c7268",
    url = "https://github.com/bazelbuild/apple_support/releases/download/0.13.0/apple_support.0.13.0.tar.gz",
            )

#load(
#    "@build_bazel_apple_support//lib:repositories.bzl",
#        "apple_support_dependencies",
#        )
#
#apple_support_dependencies()

http_archive(
    name = "com_google_googleapis",
    sha256 = "249d83abc5d50bf372c35c49d77f900bff022b2c21eb73aa8da1458b6ac401fc",
    strip_prefix = "googleapis-6b3fdcea8bc5398be4e7e9930c693f0ea09316a0",
    url = "https://github.com/googleapis/googleapis/archive/6b3fdcea8bc5398be4e7e9930c693f0ea09316a0.tar.gz",
)




#load(
#    "@build_bazel_rules_swift//swift:repositories.bzl",
#    "swift_rules_dependencies",
#)

#swift_rules_dependencies()

#load(
#    "@build_bazel_rules_swift//swift:extras.bzl",
#    "swift_rules_extra_dependencies",
#)

#swift_rules_extra_dependencies()

#load(
#    "@build_bazel_apple_support//lib:repositories.bzl",
#    "apple_support_dependencies",
#)

#apple_support_dependencies()

http_archive(
	name = "bazel_toolchains",
	urls = ["https://github.com/bazelbuild/bazel-toolchains/archive/dac71231098d891e5c4b74a2078fe9343feef510.tar.gz"],
	strip_prefix = "bazel-toolchains-dac71231098d891e5c4b74a2078fe9343feef510",
	sha256 = "56d5370eb99559b4c74f334f81bc8a298f728bd16d5a4333c865c2ad10fae3bc",
)

#load("@bazel_toolchains//repositories:repositories.bzl", bazel_toolchains_repositories = "repositories")
#bazel_toolchains_repositories()


http_archive(
    name = "build_bazel_rules_android",
    urls = ["https://github.com/bazelbuild/rules_android/archive/v0.1.1.zip"],
    sha256 = "cd06d15dd8bb59926e4d65f9003bfc20f9da4b2519985c27e190cddc8b7a7806",
    strip_prefix = "rules_android-0.1.1",
)

# Check out LLVM and MLIR from llvm-project.
# 当需要使用和tensorflow不一样的llvm时，可以通过url指定或者是local_repository
#LLVM_COMMIT = "d9afb8c3e8fd01a3c89ab2ddebcd44602a30a975"
#LLVM_SHA256 = "6763ad99c95b1849f4585ab8fdb473e71350dba0b306b34073121826429f6c6d"
#LLVM_URLS = [
#    "https://storage.googleapis.com/mirror.tensorflow.org/github.com/llvm/llvm-project/archive/{commit}.tar.gz".format(commit = LLVM_COMMIT),
#    "https://github.com/llvm/llvm-project/archive/{commit}.tar.gz".format(commit = LLVM_COMMIT),
#]

#tf_http_archive(
#    name = "llvm-project",
#    sha256 = LLVM_SHA256,
#    sha256 = "6763ad99c95b1849f4585ab8fdb473e71350dba0b306b34073121826429f6c6d",
#    strip_prefix = "llvm-project-d9afb8c3e8fd01a3c89ab2ddebcd44602a30a975",
#    urls = tf_mirror_urls("https://github.com/llvm/llvm-project/archive/d9afb8c3e8fd01a3c89ab2ddebcd44602a30a975.tar.gz"),
#    build_file = [
#       "//third_party/llvm:llvm.bazel",
#       "//third_party/mlir:BUILD.bazel",
#        "//third_party/mlir:test.BUILD": "mlir/test/BUILD",
#    link_files = {
#       "//third_party/llvm:BUILD.bazel": "llvm/BUILD",
#       "//third_party/llvm:binary_alias.bzl": "llvm/binary_alias.bzl",
#       "//third_party/llvm:cc_plugin_library.bzl": "llvm/cc_plugin_library.bzl",
#       "//third_party/llvm:enum_targets_gen.bzl": "llvm/enum_targets_gen.bzl",
#       "//third_party/llvm:tblgen.bzl": "llvm/tblgen.bzl",
#       "//third_party/llvm:config.bzl": "llvm/config.bzl",
#       "//third_party/llvm:template_rule.bzl": "llvm/template_rule.bzl",
#       "//third_party/mlir:BUILD.bazel": "mlir/BUILD",
#       "//third_party/mlir:build_defs.bzl": "mlir/build_defs.bzl",
#       "//third_party/mlir:linalggen.bzl": "mlir/linalggen.bzl",
#       "//third_party/mlir:tblgen.bzl": "mlir/tblgen.bzl",
#       "//third_party/mlir/test:BUILD.bazel": "mlir/test/BUILD",
#     },
#)


#For development, one can use a local LLVM-PROJECT repository instead.
new_local_repository(
   name = "llvm-raw",
   path = "../llvm-project",
   build_file_content = "# empty",
)

load("@llvm-raw//utils/bazel:configure.bzl", "llvm_configure", "llvm_disable_optional_support_deps")
llvm_configure(name = "llvm-project")

load("@llvm-raw//utils/bazel:terminfo.bzl", "llvm_terminfo_from_env")

llvm_disable_optional_support_deps()

maybe(
  llvm_terminfo_from_env,
  name = "llvm_terminfo",
)

# To update TensorFlow to a new revision,
# a) update URL and strip_prefix to the new git commit hash
# b) get the sha256 hash of the commit by running:
#    curl -L https://github.com/tensorflow/tensorflow/archive/<git hash>.tar.gz | sha256sum
#    and update the sha256 with the result.
#http_archive(
#    name = "org_tensorflow",
#    sha256 = "ae8e81e2d2e27ab9d0e8f1ec8c24f990c0c507088957c5f4fd1558c21f378f65",
#    strip_prefix = "tensorflow-2.2.0-rc2",
#    urls = [
#        "https://github.com/tensorflow/tensorflow/archive/v2.2.0-rc2.zip",
#    ],
#)

#For development, one can use a local TF repository instead.
#local_repository(
#   name = "org_tensorflow",
#   path = "../tensorflow",
#)
#
#load("@org_tensorflow//tensorflow:workspace0.bzl", "tf_bind")
#load("@org_tensorflow//tensorflow:workspace1.bzl", "workspace")
#load("@org_tensorflow//tensorflow:workspace2.bzl", "tf_workspace", "tf_bind")
#
#workspace()
#tf_bind()
#tf_workspace(
#    path_prefix = "",
#    tf_repo_name = "org_tensorflow",
#)


#if tf_version < v1.14.0, we need call this func by ourselves
#tf_bind()

# Required for TensorFlow dependency on @com_github_grpc_grpc

#load("//third_party/android:android_configure.bzl", "android_configure")
#android_configure(name="local_config_android")
#load("@local_config_android//:android.bzl", "android_workspace")
#
#android_workspace()
#
#

http_archive(
        name = "com_github_grpc_grpc",
        sha256 = "b956598d8cbe168b5ee717b5dafa56563eb5201a947856a6688bbeac9cac4e1f",
        strip_prefix = "grpc-b54a5b338637f92bfcf4b0bc05e0f57a5fd8fadd",
        url = "https://github.com/grpc/grpc/archive/b54a5b338637f92bfcf4b0bc05e0f57a5fd8fadd.tar.gz",
) 

load("@com_github_grpc_grpc//bazel:grpc_deps.bzl", "grpc_deps")
grpc_deps()
load("@com_github_grpc_grpc//bazel:grpc_extra_deps.bzl", "grpc_extra_deps")
grpc_extra_deps()

load("@upb//bazel:repository_defs.bzl", "bazel_version_repository")

bazel_version_repository(name = "bazel_version")
