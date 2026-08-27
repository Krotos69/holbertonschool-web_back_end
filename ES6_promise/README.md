#   ES6 Promises 
A **Promise** is an object that represents a value that you *don’t have yet* because the operation is asynchronous. It can be **pending**, **fulfilled**, or **rejected**. You use **then**, **catch**, and **finally** to react to those outcomes. You use **async/await** to write promise‑based code that *looks* synchronous. Errors are handled with **throw/try/catch**.

Below is a complete *study‑mode* explanation with examples for **every major Promise concept**.

---

#    What is a Promise? (How, Why, What)

A **Promise** is a placeholder for a future value.  
MDN says: *“The Promise object represents the eventual completion (or failure) of an asynchronous operation and its resulting value.”* 

### Why Promises?
- Avoid callback hell  
- Make async flows predictable  
- Allow chaining  
- Work with async/await

### Promise states
- **pending** → still working  
- **fulfilled** → success  
- **rejected** → failure  

MDN: *“A Promise is in one of these states: pending, fulfilled, rejected.”* 

---

#    Creating a Promise

```js
const p = new Promise((resolve, reject) => {
  setTimeout(() => {
    resolve("Done!");
  }, 1000);
});
```

---

#    Using `.then()`, `.catch()`, `.finally()`

MDN: *“The promise methods then(), catch(), and finally() are used to associate further action with a promise that becomes settled.”* 

### `.then()` — handle success (and optionally failure)

```js
p.then(result => {
  console.log("Success:", result);
});
```

### `.catch()` — handle errors

```js
p.catch(error => {
  console.error("Error:", error);
});
```

### `.finally()` — always runs

```js
p.finally(() => {
  console.log("Always runs");
});
```

###  Full chain example

```js
new Promise((resolve) => {
  resolve("Hello");
})
  .then(msg => msg + " world")
  .then(msg => console.log(msg))
  .catch(err => console.error(err))
  .finally(() => console.log("Done"));
```

---

#     Promise.resolve(), Promise.reject()

### `Promise.resolve(value)`
```js
Promise.resolve(42).then(v => console.log(v));
```

### `Promise.reject(error)`
```js
Promise.reject("Oops").catch(err => console.error(err));
```

MDN: *“Promise.resolve() returns a Promise object that is resolved with the given value.”* 

---

#     Promise.all(), allSettled(), race(), any()

MDN: *“The Promise class offers four static methods to facilitate async task concurrency.”* 

### `Promise.all()` — waits for all
```js
Promise.all([
  Promise.resolve(1),
  Promise.resolve(2)
]).then(values => console.log(values));
```

### `Promise.allSettled()` — waits for all (success or fail)
```js
Promise.allSettled([
  Promise.resolve("ok"),
  Promise.reject("fail")
]).then(results => console.log(results));
```

### `Promise.race()` — first to settle wins
```js
Promise.race([
  new Promise(res => setTimeout(() => res("fast"), 100)),
  new Promise(res => setTimeout(() => res("slow"), 500))
]).then(v => console.log(v));
```

### `Promise.any()` — first success wins
```js
Promise.any([
  Promise.reject("no"),
  Promise.resolve("yes")
]).then(v => console.log(v));
```

---

#     Throw / Try / Catch with Promises

### Throw inside a Promise chain
MDN: *“If the handler throws an error, the new promise is rejected with the thrown error.”* 

```js
Promise.resolve("ok")
  .then(() => {
    throw new Error("Something broke");
  })
  .catch(err => console.error(err));
```

### Try/catch does NOT catch inside a Promise unless using async/await

```js
try {
  Promise.reject("fail");
} catch (e) {
  // This does NOT run
}
```

---

#     The `await` operator

`await` pauses execution inside an `async` function until the Promise settles.

```js
async function demo() {
  const value = await Promise.resolve(123);
  console.log(value);
}
demo();
```

---

#     Using `async` functions

An `async` function **always returns a Promise**.

```js
async function getData() {
  return "Hello";
}

getData().then(console.log); // "Hello"
```

### With await inside

```js
async function fetchUser() {
  const user = await Promise.resolve({ name: "Krotos" });
  return user;
}

fetchUser().then(console.log);
```

### Error handling with async/await

```js
async function run() {
  try {
    const result = await Promise.reject("Oops");
    console.log(result);
  } catch (err) {
    console.error("Caught:", err);
  }
}
run();
```

---

#     Study-mode summary (quick reference)

### Core concepts
- **Promise** = future value  
- **then** = success  
- **catch** = error  
- **finally** = always  
- **resolve/reject** = settle promise  
- **async** = function returns a Promise  
- **await** = pause until promise settles  
- **throw** = reject promise  
- **try/catch** = handle errors with async/await  

### Concurrency helpers
- **Promise.all** → wait for all  
- **Promise.allSettled** → wait for all outcomes  
- **Promise.race** → first to settle  
- **Promise.any** → first success  

---

