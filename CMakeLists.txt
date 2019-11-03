cmake_minimum_required(VERSION 3.15)
set(CMAKE_CXX_STANDARD 14)
project(nighthawk)

include_directories(
        ./include
        ./source
        ./bazel-bin
        ./bazel-bin/external/envoy_api
        ./bazel-bin/external/envoy/bazel/foreign_cc/ares/include
        ./bazel-bin/external/com_envoyproxy_protoc_gen_validate
        ./bazel-nighthawk.git/external/envoy/source
        ./bazel-nighthawk.git/external/envoy/include
        ./bazel-nighthawk.git/external/com_github_gabime_spdlog/include
        ./bazel-nighthawk.git/external/com_github_c_ares_c_ares
        ./bazel-nighthawk.git/external/com_google_absl
        ./bazel-nighthawk.git/external/com_google_protobuf/src
        ./bazel-nighthawk.git/external/com_github_fmtlib_fmt/include
        ./bazel-nighthawk.git/external/com_github_eile_tclap/include
        ./bazel-nighthawk.git/external/com_github_grpc_grpc/include
        ./bazel-nighthawk.git
)

aux_source_directory(./source/client nighthawk_client_src)
aux_source_directory(./source/common nighthawk_client_src)
add_executable(nighthawk_client ${nighthawk_client_src})

#boringssl
#com_envoyproxy_protoc_gen_validate
#com_github_c_ares_c_ares
#com_github_circonus_labs_libcircllhist
#com_github_cncf_udpa
#com_github_curl
#com_github_cyan4973_xxhash
#com_github_datadog_dd_opentracing_cpp
#com_github_eile_tclap
#com_github_envoyproxy_sqlparser
#com_github_fmtlib_fmt
#com_github_gabime_spdlog
#com_github_golang_protobuf
#com_github_google_jwt_verify
#com_github_gperftools_gperftools
#com_github_grpc_grpc
#com_github_jbeder_yaml_cpp
#com_github_libevent_libevent
#com_github_luajit_luajit
#com_github_msgpack_msgpack_c
#com_github_nanopb_nanopb
#com_github_nghttp2_nghttp2
#com_github_nodejs_http_parser
#com_github_openzipkin_zipkinapi
#com_github_pallets_jinja
#com_github_pallets_markupsafe
#com_github_tencent_rapidjson
#com_google_absl
#com_google_cel_cpp
#com_google_googleapis
#com_google_protobuf
#com_googlesource_code_re2
#com_lightstep_tracer_cpp
#dep_hdrhistogram_c
#envoy
#envoy_api
#foreign_cc_platform_utils
#go_sdk
#grpc_httpjson_transcoding
#io_bazel_rules_go
#io_bazel_rules_nogo
#io_opencensus_cpp
#io_opentracing_cpp
#kafka_source
#local_config_cc
#local_config_xcode
#net_zlib
#opencensus_proto
#org_golang_x_tools
#prometheus_metrics_model
