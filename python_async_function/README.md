
---

# **Python – Async**
A concise and practical guide to Python’s asynchronous programming model using `asyncio`, including coroutine syntax, event loop execution, concurrency patterns, task creation, and usage of the `random` module.

---

## **Overview**
Python’s `asyncio` library enables writing **single‑threaded concurrent programs** using the `async` and `await` keywords. Async I/O is ideal for **I/O‑bound tasks**, allowing multiple operations to run cooperatively without blocking the main thread. This README summarizes the essential concepts needed to understand and use Python’s asynchronous features effectively.

---

## **1. Async and Await Syntax**
**Answer:**  
The `async def` syntax defines a **coroutine function**, and the `await` keyword **suspends execution** of that coroutine until the awaited operation completes.

From the documentation:

> “The `async def` syntax construct introduces a coroutine function… The `await` keyword suspends the execution of the surrounding coroutine and passes control back to the event loop.”

Example:
```python
async def greet():
    print("Hello...")
    await asyncio.sleep(1)
    print("World!")
```

---

## **2. How to Execute an Async Program With asyncio**
**Answer:**  
Use **`asyncio.run()`** to start the event loop and execute your main coroutine.

From the documentation:

> “The recommended way to start an event loop in modern Python is to use `asyncio.run()`.”

Example:
```python
import asyncio

async def main():
    print("Hello...")
    await asyncio.sleep(1)
    print("World!")

asyncio.run(main())
```

---

## **3. How to Run Concurrent Coroutines**
**Answer:**  
Use **`asyncio.gather()`** to run multiple coroutines concurrently.

From the documentation:

> “The `main()` function… uses `asyncio.gather()` to run three instances of `count()` concurrently.”

Example:
```python
async def main():
    await asyncio.gather(count(), count(), count())
```

---

## **4. How to Create asyncio Tasks**
**Answer:**  
Use **`asyncio.create_task()`** to schedule coroutines to run concurrently as background tasks.

Example:
```python
async def main():
    task1 = asyncio.create_task(worker(1))
    task2 = asyncio.create_task(worker(2))
    await task1
    await task2
```

Tasks allow the event loop to run other operations while the coroutine is suspended.

---

## **5. How to Use the `random` Module**
**Answer:**  
The `random` module provides pseudo‑random numbers using the **Mersenne Twister** generator.

From the documentation:

> “This module implements pseudo-random number generators… Almost all module functions depend on the basic function `random()`.”

Common functions:
```python
import random

random.random()          # float in [0.0, 1.0)
random.randint(1, 10)    # integer in [1, 10]
random.choice(seq)       # random element
random.uniform(2.5, 10)  # float in [2.5, 10]
```

---

## **Theme Summary**
Python’s asynchronous model centers on **coroutines**, **awaitable operations**, and the **event loop**. Using `asyncio`, developers can efficiently manage large numbers of I/O‑bound tasks without relying on threads or processes. Tools like `asyncio.gather()` and `asyncio.create_task()` enable structured concurrency, while modules like `random` integrate seamlessly into async workflows. Together, these features allow Python programs to scale gracefully and perform concurrent operations with clarity and control.

---

### **Author:**  
**Eugenio Martinez (Krotos)**

---
