package(
    default_visibility = ["//visibility:public"],
    licenses = ["notice"],
)

filegroup(
    name  = "version_files",
    srcs = [
        "Version.cpp",
        "Version.h",
    ],
)

cc_binary(
  name = "Version",
  srcs = [
    ":version_files",
    "Driver.cpp",
  ],
  deps = [
    "@llvm-project//llvm:Support",
  ],
)

