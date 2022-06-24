package(
    default_visibility = ["//visibility:public"],
    licenses = ["notice"],
)

cc_binary(
  name = "example",
  srcs = ["examples/test.cpp"],
  deps = [
    "@llvm-project//llvm:Support",
    "@llvm-project//llvm:attributes_gen",
    "@llvm-project//llvm:MC",
    "@llvm-project//llvm:IRReader",
  ],
)
