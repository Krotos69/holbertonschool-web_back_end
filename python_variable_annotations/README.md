

---

# 🐍 Python - Variable Annotations
# 🐍 Python Type Hints Cheat Sheet — README  
**Author:** *Eugenio Martinez*  
**Source:** Official mypy cheat sheet   [mypy.readthedocs.io](https://mypy.readthedocs.io/en/latest/cheat_sheet_py3.html)

---

## 📘 Project Overview
This project provides a concise, developer‑friendly reference to Python’s **type hints**, based on the official mypy cheat sheet. It is designed to help you quickly recall syntax, patterns, and best practices for annotating variables, functions, classes, and more.

Whether you're learning type checking for the first time or strengthening your static typing workflow, this README serves as a practical guide.

---

## 🧭 Table of Contents
1. [Introduction](#introduction)  
2. [Type Hints Cheat Sheet](#type-hints-cheat-sheet)  
   - [Variables](#variables)  
   - [Built‑in Types](#built-in-types)  
   - [Unions & Optional](#unions--optional)  
   - [Functions](#functions)  
   - [Callables & Iterators](#callables--iterators)  
   - [Classes](#classes)  
   - [Duck Types](#duck-types)  
   - [Forward References](#forward-references)  
3. [Summary](#summary)  
4. [Author](#author)

---

## 📝 Introduction
Python’s type hints allow developers to write clearer, safer, and more maintainable code. Tools like **mypy** analyze these annotations to detect type errors before runtime.

This cheat sheet distills the most important patterns and examples from the official documentation, giving you a quick reference for everyday development.

---

## 📄 Type Hints Cheat Sheet

### 🔹 Variables
```python
age: int = 1
a: int          # declared but not initialized
child: bool
```

### 🔹 Built‑in Types
```python
x: int = 1
x: float = 1.0
x: str = "hello"
x: list[int] = [1, 2, 3]          # Python 3.9+
x: dict[str, float] = {"a": 1.0}
x: tuple[int, str] = (1, "yes")
x: tuple[int, ...] = (1, 2, 3)
```

### 🔹 Unions & Optional
```python
x: int | str = 3
x: str | None = None              # Python 3.10+
```

### 🔹 Functions
```python
def stringify(num: int) -> str:
    return str(num)

def show(value: str, excitement: int = 10) -> None:
    print(value + "!" * excitement)
```

### 🔹 Callables & Iterators
```python
from collections.abc import Callable, Iterator

x: Callable[[int, float], float]

def gen(n: int) -> Iterator[int]:
    for i in range(n):
        yield i
```

### 🔹 Classes
```python
class BankAccount:
    def __init__(self, name: str, balance: int = 0) -> None:
        self.name = name
        self.balance = balance

    def deposit(self, amount: int) -> None:
        self.balance += amount
```

### 🔹 Duck Types
```python
from collections.abc import Iterable, Mapping

def f(ints: Iterable[int]) -> list[str]:
    return [str(x) for x in ints]

def g(m: Mapping[int, str]) -> list[int]:
    return list(m.keys())
```

### 🔹 Forward References
```python
from __future__ import annotations

def f(a: A) -> int:
    ...

class A:
    ...
```

---

## 🧾 Summary
This README compiles the essential syntax and examples for Python type hints, including:

- Variable annotations  
- Built‑in collection types  
- Union and Optional types  
- Function signatures  
- Callable and iterator annotations  
- Class typing patterns  
- Duck typing with `Iterable`, `Mapping`, etc.  
- Forward references and annotations behavior  

All examples are sourced from the official mypy cheat sheet   [mypy.readthedocs.io](https://mypy.readthedocs.io/en/latest/cheat_sheet_py3.html).

---

## 👤 Author
**Eugenio Martinez**

---
