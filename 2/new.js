// 심화

//일반적인 함수의 정의

function func() {
  console.log("call func");
}

func();

function add(a, b) {
  return a + b;
}

let ret = add(1, 2);
console.log(ret);

//자바스크립트에는 switch-case 문이 있다.
//문자열 다루기
/*function print(name) {
  //console.log("hello" + " " + name);
  //템플릿 리터럴
  console.log(`hello, ${name}`);
}
print("james");
*/

// 화살표를 이용한 함수의 정의: print 함수 재정의
let print = (name) => {
  console.log(`hello, ${name}`);
};
print("Jamse");

//무한 반복
function recursion() {
  console.log("recursion");
  recursion();
}

recursion();

//객체 리터럴 방식
let person = {
  name: "james",
  _age: 24,
  eat: function eat() {
    //멤버 함수, 기능
    console.log("먹고 있습니다");
  },
  //getter
  /*getName: function () {
    return this._name;
  }*/
  get name() {
    return this._name;
  },
  set name(name) {
    this._name = name;
  }
};
console.log(person.name);
console.log(person.eat());

// 생성자를 통한 객체 생성
/*function A() {//생성자
  //파이썬의 객체변수와 유사
  this.name = 'smith'
}*/

//생성자를 통한 초기화
function A(name) {
  this.name = name;
}

let obj = new A();
console.log(typeof obj);

// object 객체를 통한 생성

obj = new Object();
console.log(typeof obj);

//object 객체를 통한 초기화
obj = new Object({ name: "david" });
console.log(obj.name);

/*
Class를 이용하는 방법
ES6(2015년 ECMA)부터 적용
*/

//파이썬에서 정의했던 내용대로 구현
class Person {
  //객체 변수 영역
  #name;
  #age;
  gender;

  //클래스 변수
  static publicStaticVariable;
  static #privateStaticVariable = "private static variable"; //스테틱 변수도 private가능하다

  //ststic 메서드, 클래스 메서드
  static publicStaticMethod() {
    Person.publicStaticVariable = "this is public class member";
    return Person.publicStaticVariable;
  }

  static privateStaticMethod() {
    return Person.#privateStaticVariable;
  }
  constructor(name, age, gender) {
    //생성자를 통한 멤버 초기화
    this.#name = name;
    this.#age = age;
    this.gender = gender;
  }

  get name() {
    return this.#name;
  }

  set name(name) {
    return this.#name;
  }

  get age() {
    return this.#age;
  }
}

person = new Person("david", 22, "male"); //객체 생성(생성자 호출)
console.log(person.name);
person.name = "john";
console.log(person.age);
console.log(person.gender);
//클래스 변수 호출
Person.publicStaticVariable = "this is class member";
console.log(Person.publicStaticVariable);

// 프로토타입을 통한 객체 생성
//console.log(Person.publicStaticMethod());
console.log(Person.privateStaticVariable);
console.log(Person.privateStaticMethod);

//상속
class Student extends Person {
  /*
  get age() {
    return this.#age;
  }
  set age(age) {
    this.#age = age;
  }*/

  // 자식은 부모의 public 속성만 상속이 가능
  get gender() {
    return this.gender;
  }
}

Student = new Student("michel", 22, "male");
console.log(Student.name); //부모 클래스에 getter와 setter을 이용
console.log(Student.age); //private으로 접근 불가
console.log(Student.gender); //public 속성으로 접근 가능

//클래스 변수의 상속
console.log(Student.publicStaticVariable);
console.log(Student.privateStaticMethod());

//Override 지원: 부모 클래스의 메서드를 재지정
//Overloading은 지원하지 않음
