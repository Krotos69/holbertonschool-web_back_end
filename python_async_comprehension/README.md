
---

# Python – Async Comprehension

## Overview  
Asynchronous programming in Python allows you to write code that handles many tasks concurrently without blocking execution. **Async generators** and **async comprehensions** extend this capability by letting you iterate over asynchronous data streams in a clean, Pythonic way. They are essential when working with APIs, streaming data, network operations, or any workload that benefits from concurrency.





---

## Learning Objectives  
- Understand what an **asynchronous generator** is and how to write one  
- Use **async comprehensions** to iterate asynchronously inside list/set/dict comprehensions  
- Apply **type annotations** to synchronous and asynchronous generators  
- Learn how these features are used in real-world asynchronous applications  
- Gain confidence writing clean, modern async Python code  

---

## Questions & Answers  

### **1. How do you write an asynchronous generator?**  
An asynchronous generator is defined with `async def` and uses `yield` to produce values over time.

```python
async def async_numbers(n: int):
    for i in range(n):
        yield i
        await asyncio.sleep(0.1)
```

You consume it with:

```python
async for value in async_numbers(5):
    print(value)
```

---

### **2. How do you use async comprehensions?**  
Async comprehensions allow `async for` inside list, set, or dict comprehensions.

```python
async def async_numbers(n):
    for i in range(n):
        yield i
        await asyncio.sleep(0.1)

async def main():
    odds = [i async for i in async_numbers(10) if i % 2]
    print(odds)
```

They only work inside `async def` functions.

---

### **3. How do you type‑annotate generators?**  
Python provides typing helpers for both synchronous and asynchronous generators.

#### **Synchronous generator**
```python
from typing import Generator

def gen() -> Generator[int, None, None]:
    yield 1
```

#### **Asynchronous generator**
```python
from typing import AsyncGenerator

async def agen() -> AsyncGenerator[int, None]:
    yield 1
```

Use **Generator** when you need full control (`send`, `throw`, return value).  
Use **Iterator** when you only care about yielded values.  
Use **AsyncGenerator** for async generators.

---

## Real‑World Usage

### **1. Streaming API responses**  
Async generators are perfect for paginated or streaming APIs:

```python
async def stream_events(api):
    async for event in api.listen():
        yield event
```

This pattern is used in:
- WebSocket listeners  
- Real‑time dashboards  
- IoT sensor streams  

---

### **2. Processing large datasets without blocking**  
Async comprehensions let you transform asynchronous data elegantly:

```python
processed = [await transform(x) async for x in async_source()]
```

This is common in:
- ETL pipelines  
- Async database drivers  
- Cloud functions  

---

### **3. Rate‑limited operations**  
Async generators can throttle operations:

```python
async def rate_limited(items):
    for item in items:
        yield item
        await asyncio.sleep(0.5)
```

Useful for:
- API rate limits  
- Background workers  
- Batch processing  





---

## Author  
**Eugen Martinez**

---
