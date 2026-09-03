#   NodeJS Basics  

---

## Overview  
Node.js is a powerful, event‑driven JavaScript runtime that lets you build servers, CLIs, automation scripts, APIs, and full backend applications using JavaScript outside the browser. This README walks through the essential building blocks of Node.js: running JS, using modules, reading files, handling process arguments, building servers (native + Express), advanced routing, ES6/Babel usage, and speeding up development with Nodemon.





---

## Questions & Expanded Answers  

### 1. Run JavaScript using NodeJS  
Node.js executes JavaScript directly from the terminal using the V8 engine.  
Example:  
```js
// hello.js
console.log("Hello from Node!");
```  
Run it:  
```bash
node hello.js
```  
This allows JavaScript to be used for backend development, automation, and scripting.  
Learn more: Run JS

---

### 2. Use NodeJS modules  
Node supports both CommonJS (`require`) and ES Modules (`import`).  
Example (CommonJS):  
```js
const os = require("node:os");
console.log(os.platform());
```  
Example (ESM):  
```js
import os from "node:os";
console.log(os.platform());
```  
Modules let you reuse code, import Node’s standard library, and install external packages.  
Explore modules: Node modules

---

### 3. Use a specific NodeJS module to read files  
Node’s `fs` module gives full access to the filesystem.  
Sync example:  
```js
const fs = require("node:fs");
const data = fs.readFileSync("notes.txt", "utf8");
console.log(data);
```  
Async example:  
```js
fs.readFile("notes.txt", "utf8", (err, data) => {
  if (err) throw err;
  console.log(data);
});
```  
This is essential for CLIs, logs, configs, and JSON processing.  
More file operations: Read files

---

### 4. Use `process` to access command‑line arguments and environment  
`process` is a global object available everywhere.

#### Command‑line arguments  
```js
console.log(process.argv);
```  
Run:  
```bash
node app.js hello world
```  

#### Environment variables  
```js
console.log(process.env.DB_PASSWORD);
```  
Set a variable:  
```bash
DB_PASSWORD=secret node app.js
```  

This enables configuration, secrets, and dynamic script behavior.  
Deep dive: process object

---

### 5. Create a small HTTP server using NodeJS  
Node’s built‑in `http` module lets you build servers without frameworks.  
```js
const http = require("node:http");

const server = http.createServer((req, res) => {
  res.writeHead(200, { "Content-Type": "text/plain" });
  res.end("Hello from Node server!");
});

server.listen(3000);
```  
Visit:  
```
http://localhost:3000
```  
This teaches how Express works internally.  
More server examples: Node HTTP server

---

### 6. Create a small HTTP server using ExpressJS  
Express simplifies routing and responses.  
Install:  
```bash
npm install express
```  
Example:  
```js
const express = require("express");
const app = express();

app.get("/", (req, res) => {
  res.send("Hello from Express!");
});

app.listen(3000);
```  
Express is ideal for APIs, web apps, and middleware‑driven logic.  
Explore Express: Express basics

---

### 7. Create advanced routes with ExpressJS  
Express supports parameters, queries, middleware, and routers.

#### Route parameters  
```js
app.get("/users/:id", (req, res) => {
  res.send(`User ID: ${req.params.id}`);
});
```

#### Query parameters  
```js
app.get("/search", (req, res) => {
  res.send(req.query);
});
```

#### Middleware  
```js
app.use((req, res, next) => {
  console.log("Request received");
  next();
});
```

#### Router groups  
```js
const router = express.Router();

router.get("/profile", (req, res) => res.send("Profile"));
router.get("/settings", (req, res) => res.send("Settings"));

app.use("/user", router);
```  

Advanced routing is essential for building structured REST APIs.  
More routing: Advanced Express routing

---

### 8. Use ES6 with NodeJS (with Babel‑node)  
Node supports modern ES6+ features natively. Babel is used when you want experimental syntax or older Node compatibility.

Install Babel:  
```bash
npm install @babel/core @babel/node @babel/preset-env
```  

Create `.babelrc`:  
```json
{
  "presets": ["@babel/preset-env"]
}
```  

Run your app:  
```bash
npx babel-node app.js
```  

This enables decorators, advanced syntax, and future JavaScript features.  
Learn ES6: ES6 in Node

---

### 9. Use Nodemon to develop faster  
Nodemon restarts your app automatically when files change.

Install:  
```bash
npm install -g nodemon
```  

Run:  
```bash
nodemon app.js
```  

This speeds up development dramatically.  
More Nodemon usage: Nodemon guide

---

## Summary  
Node.js gives you everything you need to build modern backend applications using JavaScript. You can run JS files, use modules, read files, handle environment variables, build servers, use Express for routing, write ES6 code, and speed up development with Nodemon. Together, these tools form the foundation of real‑world Node.js development and prepare you for building full APIs, CLIs, and production‑ready applications.

