document.write("<h1> hello, javascript </h1>");
console.log("hello, Javascript");

// 변수
var variable = 2;
console.log(variable);
let variable2;

// 변수의 상수화
const variable3 = 10;
console.log(variable3);
variable2 = 2;
console.log(variable2);

//변수의 재정의
variable2 = 20;
console.log(variable2);

//const 는 재정의x, 값없이 선언x 하면 오류남
const variable4 = 100;
console.log("variable4:", variable4);

console.log(typeof variable2);
variable2 = "hello";
console.log(typeof variable2);

variable2 = Infinity;
console.log(variable2);
console.log(typeof variable2);

//연산
console.log("여기부턴 연산 결과를 출력해 줍니다.");
console.log(2 * 3);
console.log(5 - 2);
console.log(3 + 9);
console.log(2 / 3);
console.log(1234 % 10);
console.log(10 ** 2);

let number = 2;
number += 3;
console.log(number);

//비교연산
console.log("여기부턴 비교 연산자 입니다.");
console.log(1 < 2);
console.log(1 > 2);
console.log(1 <= 2);
console.log(1 >= 2);
console.log(1 === "1"); //'==':true, '===':false
console.log(1 == 1); //true

//논리 연산
console.log("여기부터는 논리 연산자 입니다.");
console.log(true && true); //And
console.log(true && false);
console.log(true || true); //Or
console.log(true || false);
console.log(!true); //Not
console.log(!false);

//파이썬과 비교하면 표현만 다르기 때문에
if (true) {
  // 시작 블럭
  console.log("출력 됨");
} // 끝 블럭

if (1 === 1) {
  console.log("같다");
}

// 윤년 구하기 문제
//1. 연도가 4로 나누어 떨어지면 윤년이다.
//2. 연도가 4와 100으로 나누어 떨어지면 윤년이다.
//3. 연도가 4, 100, 400 모두로 나누어 떨어지면 윤년이다.

//내 코드
let year = 1999;

if (year % 4 === 0) {
  console.log("윤년입니다.");
  if (year % 4 === 0 && year % 100 === 0) {
    console.log("윤년입니다.");
    if (year % 4 === 0 && year % 100 === 0 && year % 400 === 0) {
      console.log("윤년입니다.");
    } else {
      console.log("윤년이 아닙니다.");
    }
  } else {
    console.log("윤년이 아닙니다.");
  }
} else {
  console.log("윤년이 아닙니다.");
}

//강사님 코드
let year1 = 2016;
if (!(year1 % 4) == 0) {
  console.log("평년입니다.");
} else if (!(year1 % 100) == 0) {
  console.log("평년입니다.");
} else if (!(year1 % 400) == 0) {
  console.log("평년입니다.");
} else {
  console.log("윤년입니다.");
}
