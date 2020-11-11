let number = document.getElementById("number");
let increase = document.getElementById("increase");
let decrease = document.getElementById("decrease");

console.log(number.innerText);
console.log(increase.innerHTML);
console.log(decrease.innerHTML);

increase.onclick = function () {
  let count = number.innerText;
  count = parseInt(count);
  number.innerText = ++count;
};

decrease.onclick = function () {
  let count = number.innerText;
  count = parseInt(count);
  number.innerText = --count;
};
