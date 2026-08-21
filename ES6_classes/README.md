
---

# ES6 Classes & Metaprogramming — Basics

Introduces the fundamentals of JavaScript ES6 classes, including class definitions, methods, static methods, inheritance, and metaprogramming with Symbols. It is based on the MDN documentation for Classes and Keith Cirkel’s article *JavaScript Symbols are awesome*.

---

## 1. How to Define a Class

A class is a template for creating objects. Under the hood, classes are “special functions” and behave similarly to constructor functions, but with cleaner syntax.

```js
class Rectangle {
  constructor(height, width) {
    this.height = height;
    this.width = width;
  }
}
```

Classes can also be defined as expressions:

```js
const Rectangle = class {
  constructor(h, w) {
    this.h = h;
    this.w = w;
  }
};
```

> MDN: “Classes are in fact ‘special functions’, and just as you can define function expressions and function declarations, a class can be defined in two ways.” 

---

## 2. How to Add Methods to a Class

Methods defined inside a class are placed on the class prototype and shared across all instances.

```js
class Rectangle {
  constructor(h, w) {
    this.h = h;
    this.w = w;
  }

  calcArea() {
    return this.h * this.w;
  }

  get area() {
    return this.calcArea();
  }
}
```

You can define:
- Regular methods  
- Getters / setters  
- Generator methods  
- Async methods  

> MDN: “Methods are defined on the prototype of each class instance and are shared by all instances.” 

---

## 3. Why and How to Add a Static Method

Static methods belong to the **class itself**, not its instances. They are ideal for utilities, factories, metadata, and shared configuration.

```js
class Point {
  constructor(x, y) {
    this.x = x;
    this.y = y;
  }

  static distance(a, b) {
    return Math.hypot(a.x - b.x, a.y - b.y);
  }
}

Point.distance(new Point(0,0), new Point(3,4)); // 5
```

> MDN: “Static methods are often used to create utility functions… static fields are useful for caches, fixed‑configuration, or any other data that doesn’t need to be replicated across instances.” 

---

## 4. How to Extend a Class from Another

Use `extends` to create a subclass and `super()` to call the parent constructor.

```js
class Animal {
  speak() {
    console.log("Generic sound");
  }
}

class Dog extends Animal {
  speak() {
    super.speak();
    console.log("Woof!");
  }
}
```

> MDN: “The extends keyword is used… to create a class as a child of another constructor.” 

---

## 5. Metaprogramming & Symbols

Symbols are unique and immutable primitive values often used as hidden object keys. They enable advanced metaprogramming patterns and avoid naming collisions.

```js
const size = Symbol("size");

class Collection {
  constructor() {
    this[size] = 0;
  }

  add(item) {
    this[this[size]] = item;
    this[size]++;
  }
}
```

Symbols also power **well‑known metaprogramming hooks**:

- `Symbol.iterator` — custom iteration  
- `Symbol.toPrimitive` — custom type coercion  
- `Symbol.hasInstance` — customize `instanceof`  
- `Symbol.toStringTag` — customize `Object.prototype.toString`  
- `Symbol.species` — control derived constructors  

Example: custom iterator:

```js
class Collection {
  *[Symbol.iterator]() {
    let i = 0;
    while (this[i] !== undefined) {
      yield this[i++];
    }
  }
}
```

> Keith Cirkel: “Symbols give a whole new sense of purpose… they provide a kind of hidden under layer to Objects.” 

---

## Summary

This README covers:

- Class declarations & expressions  
- Prototype methods  
- Static methods  
- Inheritance with `extends`  
- Metaprogramming with Symbols  

It provides a solid foundation for ES6 class usage and advanced JavaScript design patterns.

---

