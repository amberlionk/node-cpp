#include <napi.h>
#include "function_arg.h"
#include "callback.h"
#include "object_factory.h"

Napi::Object Init(Napi::Env env, Napi::Object exports) {


  exports.Set(Napi::String::New(env, "add"), Napi::Function::New(env, Add));
  exports.Set(Napi::String::New(env, "functionWithCalback"), Napi::Function::New(env, RunCallback));
  exports.Set(Napi::String::New(env, "createObject"), Napi::Function::New(env, CreateObject));

  return exports;
}

NODE_API_MODULE(NODE_GYP_MODULE_NAME, Init)