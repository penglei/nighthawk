#/bin/bash

set -ex

#export CFLAGS="-Wno-error"
#export CXXFLAGS="-Wno-error"

export CC=clang
export CXX=clang++
#export ASAN_SYMBOLIZER_PATH=/opt/llvm/bin/llvm-symbolizer
export BAZEL_COMPILER=clang

#export CC="gcc-8"
#export CXX="g++-8"
#--compiler=clang

#target="//:nighthawk"
target="//:nighthawk_client"
#args="-c dbg" #DEBUG macro symbol is conflict...
args="-c opt"
bazel build --verbose_failures --sandbox_debug $args $target
