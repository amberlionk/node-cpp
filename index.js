// https://github.com/nodejs/node-addon-examples
// const fn_nan = require('bindings')('fn_nan')
// const fn_v8_10 = require('bindings')('fn_v8_10')
// const fn_napi = require('bindings')('fn_napi')
// const fn_naddon = require('bindings')('fn_naddon')

// console.log('This should be eight [fn_nan]:', fn_nan.add(3, 5))
// console.log('This should be eight [fn_v8_10]:', fn_v8_10.add(3, 5))
// console.log('This should be eight [fn_napi]:', fn_napi.add(3, 5))
// console.log('This should be eight [fn_naddon]:', fn_naddon.add(3, 5))

//-------------------------------------------------------------------------------------------------------------------------------

const naddon = require('./build/Release/naddon.node')
// const naddon = require('bindings')('naddon')

console.log('This should be eight [naddon]:', naddon.add(3, 5))
naddon.functionWithCalback(msg => console.log(msg))
console.log(naddon.createObject("new object"))