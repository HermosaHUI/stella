<!--
 * @Author: your name
 * @Date: 2020-04-07 20:35:03
 * @LastEditTime: 2020-04-10 19:09:30
 * @LastEditors: Please set LastEditors
 * @Description: In User Settings Edit
 * @FilePath: /inference-engine-doc/build/README.md
 -->
# 源码编译说明文档

## 1 build.py脚本

### 说明

build.py应该包含的功能：

- python version检查
- bazel版本检查及下载
- stella_env_path配置
- 命令行参数解析
- 生成对应配置下的.bazelrc文件（e.g. with_or_without_tf_support)
- BTW:目前改脚本只起到示意作用，需依据后期构建需求进行重构。


example for install-script: 内部调用了bazel run，这个脚本的主要目的是为了后期整体项目的安装；前期只需要这个脚本的.bazelrc生成功能。
```python
  python build.py --stella_env_path=./ --bazel_path=/usr/local/bin/bazel
  
```
example for build label
```shell
  bazel build --define with_tf_support=true --config macos --sandbox_debug stella:test
```

### 目前的限制和作出的修改
- stella/core/parser/tensorflow 此目录下的代码需与项目依赖的tensorflow版本一致。
  - 合理的进行stella/core/parser/tensorflow/BUILD的修改可取消限制
- 需修改所依赖的tensorflow中的部分BUILD中label的visibility;
  - 如果架构上依赖tf-mlir部分，并不希望大幅度修改相关源码和BUILD-file，要背负这个限制；
- 删除了stella/core/parser/tensorflow中对于tpu的源码和构建代码；
- 修改了stella/core/parser/tensorflow/BUILD中的target描述//tensorflow-> //stella 


### parser和框架的解耦需要做的事，以tensorflow为例
1、重构stella/core/parser/tensorflow/模块，解除不必要的tf依赖；
2、修改third_party下tensorflow的tensorflow.bzl，对应parser模块所依赖的模块进行tensorflow的源码编译（目前为了方便，直接使用了tf_workspace。主要问题是会导入过多不必要的依赖）
3、记得对应修改build.py下的逻辑
