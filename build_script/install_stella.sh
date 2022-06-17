###
 # @Author: your name
 # @Date: 2020-04-08 12:42:25
 # @LastEditTime: 2020-04-10 18:54:24
 # @LastEditors: Please set LastEditors
 # @Description: In User Settings Edit
 # @FilePath: /inference-engine-doc/build/install_stella.sh
 ###
# --- begin runfiles.bash initialization ---
# Copy-pasted from Bazel's Bash runfiles library (tools/bash/runfiles/runfiles.bash).
set -euo pipefail
if [[ ! -d "${RUNFILES_DIR:-/dev/null}" && ! -f "${RUNFILES_MANIFEST_FILE:-/dev/null}" ]]; then
  if [[ -f "$0.runfiles_manifest" ]]; then
    export RUNFILES_MANIFEST_FILE="$0.runfiles_manifest"
  elif [[ -f "$0.runfiles/MANIFEST" ]]; then
    export RUNFILES_MANIFEST_FILE="$0.runfiles/MANIFEST"
  elif [[ -f "$0.runfiles/bazel_tools/tools/bash/runfiles/runfiles.bash" ]]; then
    export RUNFILES_DIR="$0.runfiles"
  fi
fi
if [[ -f "${RUNFILES_DIR:-/dev/null}/bazel_tools/tools/bash/runfiles/runfiles.bash" ]]; then
  source "${RUNFILES_DIR}/bazel_tools/tools/bash/runfiles/runfiles.bash"
elif [[ -f "${RUNFILES_MANIFEST_FILE:-/dev/null}" ]]; then
  source "$(grep -m1 "^bazel_tools/tools/bash/runfiles/runfiles.bash " \
            "$RUNFILES_MANIFEST_FILE" | cut -d ' ' -f 2-)"
else
  echo >&2 "ERROR: cannot find @bazel_tools//tools/bash/runfiles:runfiles.bash"
  exit 1
fi
# --- end runfiles.bash initialization ---

if [[ $# -ne 1 ]]; then
  echo "Usage: $0 <target directory>"
  exit 1
fi
TARGET="$1"

if [[ ! -d "${TARGET}/lib" ]]; then
  echo "Target directory ${TARGET} does not have a lib directory"
  exit 1
fi

# Copy the tensorflow dependencies into build/lib
#TODO:增加对不同OS的支持，.dylib\.so\...
#TODO:其他模块开发完成后，增加对应的模块打包功能；
cp -f "$(rlocation org_tensorflow/tensorflow/libtensorflow_framework.dylib)" \
  "${TARGET}/lib"
#cp -f "$(rlocation org_tensorflow/tensorflow/libtensorflow_cc.so)" \
#  "${TARGET}/lib"

