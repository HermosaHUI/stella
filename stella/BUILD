load("@bazel_skylib//lib:selects.bzl", "selects")
load("@bazel_skylib//:bzl_library.bzl", "bzl_library")
load("//stella:workspace.bzl", "if_tf","if_onnx","if_pytorch")
package(
    default_visibility = ["//visibility:public"],
    licenses = ["notice"],  # Apache 2.0
)

# This flag enables external support.
config_setting(
    name = "with_tf_support",
    values = {"define": "with_tf_support=true"},
    visibility = ["//visibility:public"],
)

config_setting(
    name = "with_onnx_support",
    values = {"define": "with_onnx_support=true"},
    visibility = ["//visibility:public"],
)

config_setting(
    name = "with_pytorch_support",
    values = {"define": "with_pytorch_support=true"},
    visibility = ["//visibility:public"],
)

########config for host-cpu and OS
#config_setting(
#    name = "android_arm",
#    values = {
#        "crosstool_top": "//external:android/crosstool",
#        "cpu": "armeabi-v7a",
#    },
#    visibility = ["//visibility:public"],
#)
#
#config_setting(
#    name = "android_arm64",
#    values = {
#        "crosstool_top": "//external:android/crosstool",
#        "cpu": "arm64-v8a",
#    },
#    visibility = ["//visibility:public"],
#)
#
#config_setting(
#    name = "windows",
#    values = {"cpu": "x64_windows"},
#    visibility = ["//visibility:public"],
#)
#
#config_setting(
#    name = "macos",
#    values = {
#        "apple_platform_type": "macos",
#        "cpu": "darwin",
#    },
#    visibility = ["//visibility:public"],
#)

config_setting(
    name = "linux_aarch64",
    values = {"cpu": "aarch64"},
    visibility = ["//visibility:public"],
)

config_setting(
    name = "linux_x86_64",
    values = {"cpu": "k8"},
    visibility = ["//visibility:public"],
)

config_setting(
    name = "debug",
    values = {
        "compilation_mode": "dbg",
    },
    visibility = ["//visibility:public"],
)

config_setting(
    name = "optimized",
    values = {
        "compilation_mode": "opt",
    },
    visibility = ["//visibility:public"],
)

config_setting(
    name = "arm",
    values = {"cpu": "arm"},
    visibility = ["//visibility:public"],
)

# https://docs.bazel.build/versions/master/be/c-cpp.html#cc_binary
cc_binary(
    name = "test",
    srcs = ["test.cc"],
    copts = ["-std=c++14", "-fno-rtti"],
    deps = [
            "@llvm-project//llvm:Support",
            "@llvm-project//mlir:AllPassesAndDialects",
            "@llvm-project//mlir:MlirOptLib",
            "@llvm-project//mlir:Pass",
            "@llvm-project//mlir:Support",
            "@llvm-project//mlir/test:TestTransforms",]
             + if_tf(
                 ["@org_tensorflow//tensorflow/compiler/mlir:init_mlir",]
            ),#TODO add if_onnx&if_pytorch here after added the corresponding build support
)



#########
