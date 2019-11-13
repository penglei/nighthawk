#!/bin/bash

ROOT=$(cd $(dirname "${BASH_SOURCE}") && pwd -P)

REPO_ROOT=$(cd ${ROOT}/.. && pwd)
cd $REPO_ROOT
WORKDIR=$(mktemp -d --tmpdir=${REPO_ROOT})

strip $REPO_ROOT/bazel-bin/nighthawk_client -o $WORKDIR/nighthawk_client

image_build_args=
if [[ "$HTTP_PROXY" != "" ]]; then
      image_build_args="--build-arg HTTP_PROXY=${HTTP_PROXY}"
fi

docker build ${image_build_args} -t nighthawk -f ${ROOT}/docker/Dockerfile ${WORKDIR}

rm -rf ${WORKDIR}

echo docker tag nighthawk ccr.ccs.tencentyun.com/mesh-perf/nighthawk
