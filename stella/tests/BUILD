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

cc_binary(
  name = "llvmir_gen_example",
  srcs = ["llvm-ir/llvmir_print.cc"],
  deps = [
    "@llvm-project//llvm:Support",
    "@llvm-project//llvm:attributes_gen",
    "@llvm-project//llvm:MC",
    "@llvm-project//llvm:BitWriter",
    "@llvm-project//llvm:IRReader",
  ],
)

cc_binary(
  name = "llvm-stress",
  srcs = ["llvm-stress/llvm-stress.cpp"],
  deps = [
    "@llvm-project//llvm:Support",
    "@llvm-project//llvm:attributes_gen",
    "@llvm-project//llvm:MC",
    "@llvm-project//llvm:BitWriter",
    "@llvm-project//llvm:IRReader",
    "@llvm-project//llvm:Passes",
  ],
)

cc_binary(
  name = "llvm-compile",
  srcs = ["llvm-compile/llvm-compile.cpp"],
  deps = [
    "@llvm-project//llvm:Support",
    "@llvm-project//llvm:attributes_gen",
    "@llvm-project//llvm:MC",
    "@llvm-project//llvm:BitWriter",
    "@llvm-project//llvm:IRReader",
    "@llvm-project//llvm:Passes",
  ],
)
