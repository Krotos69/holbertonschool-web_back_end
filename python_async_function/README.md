

---

# 📘 Python - Async IO & Random Module in Python  
**Author:** *Eugenio Martínez*

## 🧭 Objective  
This project introduces the fundamentals of **asynchronous programming in Python** using `async`, `await`, and the `asyncio` module.  
You will also review the basics of Python’s `random` module for generating pseudo‑random values.

The goal is to understand **how concurrency works**, how to **run coroutines**, how to **create tasks**, and how to **apply randomness** in simple programs.

---

## 📚 Table of Contents  
1. [Introduction](#introduction)  
2. [Key Concepts](#key-concepts)  
   - async / await  
   - Running async programs  
   - Concurrent coroutines  
   - asyncio tasks  
   - random module  
3. [Questions We Have](#questions-we-have)  
4. [Summary](#summary)  
5. [Author](#author)

---

## 🧩 Introduction  
Python’s `asyncio` library provides a way to write **non‑blocking**, **concurrent** programs using coroutines.  
Instead of waiting for slow operations (like network calls or timers), your program can continue running other tasks.

At the same time, the `random` module allows you to introduce randomness into your programs—useful for simulations, games, testing, and more.

This README gives you a structured overview of these topics in a way that supports **active recall**, **practice**, and **Holberton‑style learning**.

---

## 🔑 Key Concepts

### 1. `async` and `await`  
- `async def` defines a coroutine  
- `await` pauses execution until the awaited task completes  
- Coroutines run inside an **event loop**

**Example:**
```python
import asyncio

async def greet():
    print("Hello...")
    await asyncio.sleep(1)
    print("...world!")
```

---

### 2. Running an Async Program  
Use `asyncio.run()` to start the event loop and execute your main coroutine.

```python
asyncio.run(greet())
```

---

### 3. Running Concurrent Coroutines  
Use `asyncio.gather()` to run multiple coroutines at the same time.

```python
await asyncio.gather(
    task1(),
    task2(),
    task3()
)
```

---

### 4. Creating asyncio Tasks  
Tasks allow coroutines to run **in the background**.

```python
t = asyncio.create_task(my_coroutine())
await t
```

Tasks start running immediately after creation.

---

### 5. Using the `random` Module  
Common functions:
- `random.random()` → float between 0.0 and 1.0  
- `random.randint(a, b)` → integer between a and b  
- `random.choice(seq)` → pick a random element  
- `random.shuffle(list)` → shuffle list in place  
- `random.uniform(a, b)` → float between a and b  

**Example:**
```python
import random

print(random.randint(1, 6))
print(random.choice(["red", "blue", "green"]))
```

---

## ❓ Questions We Have  
These guide your active recall and deeper understanding:

1. What is the difference between concurrency and parallelism?  
2. Why must `await` be used inside an `async` function?  
3. What does `asyncio.run()` do behind the scenes?  
4. When should you use `asyncio.gather()` vs `asyncio.create_task()`?  
5. How does Python generate pseudo‑random numbers?  
6. What are common use cases for the `random` module?  
7. What happens if you forget to `await` a coroutine?

---

## 📝 Summary  
- `async` and `await` let you write **non‑blocking**, **concurrent** code.  
- `asyncio.run()` starts and manages the event loop.  
- `asyncio.gather()` runs multiple coroutines concurrently.  
- `asyncio.create_task()` schedules coroutines to run in the background.  
- The `random` module provides tools for generating pseudo‑random numbers and selecting random elements.  

Together, these tools help you build efficient, responsive programs and introduce randomness when needed.

---

## 👤 Author  
**Eugenio Martínez**

---
