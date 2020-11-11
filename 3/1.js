//for문
/*
for (let i = 10; i > 0; i--) {
  console.log(i);
}*/

//while문
/*
let i = 0;
while (i < 10) {
  console.log(i);
  i++;
}

let array = [1, 2, 3, 4, 5]

for (let ele of array){
  console.log(ele);
}
*/
// break, continue는 (블록)내에서만 사용 가능
// block scope

// 함수 반복문 실습 예제
// numbers 라는 배열을 매개변수로 받아서
//x보다 작은 수의 총합을 구하는 함수를 만들어 봅시다.

// x = 5
// [1, 10, 4, 9, 2, 3, 8, 5, 7, 6]
console.log("내 코드");
let numbers = [1, 10, 4, 9, 2, 3, 8, 5, 7, 6];

function plus(numbers) {
  let sum = 0;
  let x = 5;
  for (let i = 0; i < numbers.length; i++) {
    if (x > numbers[i]) {
      sum += numbers[i];
    }
  }
  return sum;
}

console.log(plus(numbers));

console.log("강사님 코드");
function func01(numbers) {
  let x = 5;
  let total = 0;

  /*for (let ele of numbers) {
    if (ele < x) {
      total += ele;
    }
  }
  return total;*/

  let i = 0;
  total = 0;
  while (i < numbers.length) {
    if (numbers[i] < x) {
      total += numbers[i];
    }
    i++;
  }
  return total;
}

console.log(func01(numbers));

// 변수 타입을 함수로 정의하는 느낌
//화살표 함수
/*
let func02 = (numbers) => {};
*/

//변수 선언
var globalVarVariable = "global use var";
let globalLetVariable = "global use let";
const globalConstVariable = "global const type";

function func() {
  console.log("call func");

  var localVarVariable = "local use var";
  let localLetVariable = "local use let";
  const localConstVariable = "local const type";

  // 함수 내에서 전역 변수에 대한 접근
  console.log(globalVarVariable);
  console.log(globalLetVariable);
  console.log(globalConstVariable);

  // 함수 내에서 지역 변수에 대한 접근
  console.log(localVarVariable);
  console.log(localLetVariable);
  console.log(localConstVariable);
}
func();

//함수 밖에서 전역 변수에 대한 접근
console.log("전역 변수를 함수 밖에서 접근하면?");
console.log(globalVarVariable);
console.log(globalLetVariable);
console.log(globalConstVariable);

//함수 밖에서 지역 변수에 대한 접근 :error 발생
//console.log(localVarVariable);
//console.log(localLetVariable);
//console.log(localConstVariable);
