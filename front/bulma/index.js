// console.log(document.querySelector("#burger"));
const burgerIcon = document.querySelector("#burger");
const navbarMenu = document.querySelector("#nav-links");

burgerIcon.addEventListener("click", () => {
  navbarMenu.classList.toggle("is-active");
});

// Tabs

const tabs = document.querySelectorAll(".tabs li");
const tabContentBoxes = document.querySelector("#tab-content > div");

tabs.forEach((tab) => {
  tab.addEventListener("click", () => {
    tabs.forEach((item) => item.classList.remove("is-active"));
    tab.classList.add("is-active");

    const target = tab.dataset.target;
    conole.log("target", target);
    tabContentBoxes.forEach((box) => {
      if (box.getAttribute("id") === target) {
        box.classList.remove("is-hidden");
      } else {
        box.classList.add("is-hidden");
      }
    });
  });
});

// Js
console.log(document.querySelector("#nav-links"));
console.log(parseInt("53423421461"));

function a() {
  "use strict";
  let b = "lss";
}

console.log(a());

const s = [3, 4, 5];

function b() {
  //   s = [6, 7, 8];
  s[0] = 100;
}

b();
console.log(s);

function freezeObj() {
  const MATH_CONST = {
    PI: 3.14,
  };
  Object.freeze(MATH_CONST);
  try {
    MATH_CONST.PI = 100;
  } catch (ex) {
    console.log(ex);
  }
  return MATH_CONST.PI;
}

console.log(freezeObj());

const magic = () => new Date();
console.log(magic());
x = "asa";
y = "jiji";
const myconcat = (x, y) => x.concat(y);
console.log(myconcat(x, y));

const theArray = [4, 7, 9, 2, -2, -7, -8];

z = (num) => Number.isInteger(num) && num > 0;
z2 = (num) => Math.pow(num, 2);
(z3 = (a, b) => a + b), 0;

u1 = theArray.filter(z).reduce(z3);

console.log("array", theArray);
console.log("filter", theArray.filter(z));
console.log("filter_map", theArray.filter(z).map(z2));
console.log("filter_map_reduce", theArray.filter(z).map(z2).reduce(z3));
console.log("filter_reduce", theArray.filter(z).reduce(z3));
console.log("reduce", theArray.reduce(z3));

function summer(...args) {
  console.log("inside sumeer", args[0]);
  return args[0].reduce(z3);
}

console.log("summer", summer(theArray));

console.log("Spread operator", ...theArray);
console.log("Spread operator braks", [...theArray]);

vo = { x: 1, y: 2, z: 3 };

const { x: u2, y: u3, z: u4 } = vo;
console.log(u4);

const u8 = ([, , ...arr] = theArray);

console.log("full", u8);
console.log("...arr", arr);

huge = 1390219302;
const greetings = `Lorem ipsum dolor sit, amet ${huge}consectetur adipisicing elit.`;
console.log(greetings);

class SpaceShuttle {
  constructor(targetPlant) {
    this.targetPlant = targetPlant;
  }
}

var zeus = new SpaceShuttle("Mervury");

console.log(zeus);

class Book {
  constructor(name) {
    this._name = name;
  }

  get name() {
    return this._name;
  }

  set name(add_name) {
    this._name = add_name;
  }
}

u9 = new Book("hisjka");
u9._name = "sasass";

console.log(u9);
