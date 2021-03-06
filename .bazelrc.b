# Flag to enable remote config
common --experimental_repo_remote_exec

build --repo_env PYTHON_BIN_PATH="/usr/bin/python"
build --python_path="/usr/bin/python"
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

# By default, build Project in C++ 17 mode.
build:linux --cxxopt=-std=c++14
build:linux --host_cxxopt=-std=c++14
#build:linux --linkopt=-Wl,-rpath,
build:macos --cxxopt=-std=c++14
build:macos --host_cxxopt=-std=c++14
build:windows --cxxopt=/std:c++14
build:windows --host_cxxopt=/std:c++14
build --action_env STELLA_ENV_PATH="./" --cxxopt=-std=c++14

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

