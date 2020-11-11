function func() {
  const CONST_VALUE = "this is const variable";
  let let_value = "let function scope";
  var var_value = "var function scope";
  if (true) {
    const CONST_VALUE_IN_BLOCK = "this is const variable too";
    console.log(CONST_VALUE_IN_BLOCK);
    let let_value = "let block scope";
    var var_value = "var block scope";

    console.log(CONST_VALUE_IN_BLOCK);
    console.log(let_value);
    console.log(var_value);
  }

  console.log(CONST_VALUE);
  //console.log(CONST_VALUE_IN_BLOCK);
  console.log(let_value);
  console.log(var_value);
}

func();

console.log(pre_defined_value);
var pre_defined_value = 10;

/*
- 변수 호이스팅(hoisting)
- var pre_defined_value;
- console.log(pre_defined_value);
- pre_defined_value = 10;
*/

//비동기 처리(3,4교시)
/* 
비동기 처리 vs 동기식 처리
- 파이썬(Python) 소켓 프로그래밍에서 사용했던 accept() 나
- recv() 같은 동작을 생각해보자, 혹은 input()
- 사용자의 연결을 기다리는 것을 "동기식 처리" 라고 한다.
- setTimeout(): 일정 시간동안 기다렸다가 명령어를 수행, 비동기저리 함수이다.
*/

console.log("start");

setTimeout(function () {
  console.log("end");
}, 3000);
console.log("restart");

//1. callback을 이용한 비동기 처리
console.log("start");

function timeOut(callback_function) {
  setTimeout(() => {
    console.log("end");
    if (callback_function) {
      callback_function();
    }
  }, 3000);
}

timeOut((n) => {
  console.log("restart");
});

//2.Call back 지목
// 예를 들면 setTimeout을 이요해서 초당 한번씩 동작하는 프로그램을
// 작성하고 싶은 경우
let count = 0;
for (let i; i < 10; i++) {
  setTimeout(function () {
    count++;
    console.log(count);
  }, 1000);
}
//
function timeout(n, callback_function) {
  setTimeout(function () {
    let count = n + 1;
    console.log(count);
    if (callback_function) {
      callback_function(count);
    }
  }, 1000);
}
timeout(0, (n) => {
  console.log("end");
});
