{
  "targets": [
    #  {
    #   "target_name": "fn_nan",
    #   "sources": [ "src-cpp/function/function_nan.cc" ],
    #   "include_dirs": [
    #     "<!(node -e \"require('nan')\")"
    #   ]
    # },
    # {
    #   "target_name": "fn_v8_10",
    #   "sources": [ "src-cpp/function/function_nan10.cc" ]
    # },
    # {
    #   "target_name": "fn_napi",
    #   "sources": [ "src-cpp/function/function_napi.cc" ]
    # },
    # {
    #   "target_name": "fn_naddon",
    #   "cflags!": [ "-fno-exceptions" ],
    #   "cflags_cc!": [ "-fno-exceptions" ],
    #   "sources": [ "src-cpp/function/function_naddon.cc" ],
    #   "include_dirs": [
    #     "<!@(node -p \"require('node-addon-api').include\")"
    #   ],
    #   'defines': [ 'NAPI_DISABLE_CPP_EXCEPTIONS' ],
    # },


    {
      "target_name": "naddon",
      "cflags!": [ "-fno-exceptions" ],
      "cflags_cc!": [ "-fno-exceptions" ],
      "sources": [ 
        "src-cpp/naddon/addon_export.cc",
        "src-cpp/naddon/function_arg.cc",
        "src-cpp/naddon/callback.cc",
        "src-cpp/naddon/object_factory.cc"
     ],
      "include_dirs": [
        "<!@(node -p \"require('node-addon-api').include\")"
      ],
      'defines': [ 'NAPI_DISABLE_CPP_EXCEPTIONS' ],
    },
  ]
}