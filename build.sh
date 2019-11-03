#/bin/bash

set -ex

#export CFLAGS="-Wno-error"
#export CXXFLAGS="-Wno-error"

#export ASAN_SYMBOLIZER_PATH=/opt/llvm/bin/llvm-symbolizer
export CC=clang
export CXX=clang++
export BAZEL_COMPILER=clang

#all_targets="//:nighthawk"
target="//:nighthawk_client"

#bazel build -c dbg $target
#bazel build -c opt $target

#bazel build -c opt --copt -Os --config=sizeopt $target
bazel build -c opt $target --config=sizeopt
