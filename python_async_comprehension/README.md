
---

# Python - Async Comprehension

##   Project Overview

This project explores **asynchronous generators**, **async comprehensions**, and **type-annotating asynchronous generators** in Python. These features were introduced to improve the readability, performance, and expressiveness of asynchronous code—especially when working with streams of data, concurrency, or I/O‑bound operations.

You will learn how to:

- Write asynchronous generators using `async def` and `yield`
- Use asynchronous comprehensions for cleaner async iteration
- Apply proper type hints to async generators and async iterables

---

##   Objective

The goal of this project is to help you understand:

- How asynchronous iteration works in Python
- How async comprehensions simplify asynchronous loops
- How to annotate async generators using `typing` tools
- How these features improve performance and readability in async programs

---

##   Key Definitions

### **Asynchronous Generator**
A function defined with `async def` that uses `yield` to produce values asynchronously.

```python
async def async_generator():
    for i in range(5):
        await asyncio.sleep(1)
        yield i
```

### **Async Comprehension**
A list/set/dict comprehension that iterates over an asynchronous iterator.

```python
result = [i async for i in async_generator()]
```

### **Type-Annotated Async Generator**
Using `typing.AsyncGenerator`, `AsyncIterable`, or `AsyncIterator` to annotate async generators.

```python
from typing import AsyncGenerator

async def async_generator() -> AsyncGenerator[int, None]:
    ...
```

---

##   Uses and Practical Applications

- Streaming data from APIs
- Consuming asynchronous I/O (e.g., websockets)
- Handling large datasets without blocking the event loop
- Writing efficient concurrent pipelines
- Improving readability of async loops with comprehensions

---

##   Examples

### **1. Writing an Asynchronous Generator**

```python
import asyncio
from random import random

async def async_generator():
    for _ in range(10):
        await asyncio.sleep(1)
        yield random()
```

### **2. Using an Async Comprehension**

```python
async def async_comprehension():
    return [value async for value in async_generator()]
```

### **3. Type-Annotating an Async Generator**

```python
from typing import AsyncGenerator

async def typed_async_generator() -> AsyncGenerator[float, None]:
    for _ in range(5):
        await asyncio.sleep(1)
        yield random()
```

---

##   Content Summary

This project covers:

- The syntax and behavior of asynchronous generators
- How async comprehensions improve async code readability
- The difference between synchronous and asynchronous iteration
- How to properly annotate async generators using `typing`
- Practical examples and exercises to reinforce learning

### **Resources Used**

- **PEP 530 – Asynchronous Comprehensions**  
  https://intranet.hbtn.io/rltoken/UFCR8qW3nHmEDZZaHqXL7Q

- **What’s New in Python: Asynchronous Comprehensions / Generators**  
  https://intranet.hbtn.io/rltoken/PAGwxZUyVGBR8EMFGGNnGg

- **Type-hints for generators**  
  https://intranet.hbtn.io/rltoken/fOrb8FrWbcYu8evONWj2Kw

---

##   Author

**Eugenio Martínez**

---


