# 🔄 Method Overriding & Dynamic Method Dispatch in Python

## 📌 Description

This Python program demonstrates:

* **Inheritance**
* **Method Overriding**
* **Dynamic Method Dispatch (Runtime Polymorphism)**

The child class `Second` overrides method `c()` of parent class `First`.
When the method is called using a reference to the child object, the overridden version executes.

---

## 🚀 Features

* Demonstrates inheritance
* Shows method overriding
* Demonstrates runtime polymorphism
* Uses parent-child object reference

---

## 🛠️ How It Works

### 1️⃣ Parent Class – `First`

Contains methods:

* `a()`
* `b()`
* `c()`

---

### 2️⃣ Child Class – `Second`

```python id="m8q3pl"
class Second(First)
```

👉 Inherits all methods from `First`

Overrides:

```python id="x2m7qa"
def c(self)
```

---

### 3️⃣ Object Creation

```python id="v5q1zx"
obj = Second()
```

Creates child class object.

---

### 4️⃣ Reference Assignment

```python id="n4m8pt"
r = obj
```

👉 `r` points to object of class `Second`.

---

## 💻 Code

```python id="k7m2pl"
class First:
    def a(self):
        print("Inside method a")

    def b(self):
        print("Inside method b")

    def c(self):
        print("Inside method c")


class Second(First):
    # Overridden method
    def c(self):
        print("Inside new method c")


if __name__ == "__main__":
    obj = Second()

    # Parent reference pointing to child object
    r = obj

    r.a()
    r.b()
    r.c()
```

---

## ▶️ Output

```id="p3m9qa"
Inside method a
Inside method b
Inside new method c
```

---

## 🧠 Key Concepts

### ✔ Method Overriding

Child class provides new implementation of parent method.

```python id="u6m1zx"
def c(self)
```

in `Second` overrides:

```python id="y8q4mv"
def c(self)
```

from `First`.

---

### ✔ Dynamic Method Dispatch

Method executed depends on:

* actual object type at runtime

Even though:

```python id="j5m2pt"
r = obj
```

the method:

```python id="c9q7pl"
r.c()
```

calls child version because object belongs to `Second`.

---

### ✔ Runtime Polymorphism

Same method name behaves differently depending on object type.

---

## 📚 Concepts Used

* Inheritance
* Method overriding
* Runtime polymorphism
* Dynamic method dispatch

---

## ⚠️ Important Understanding

### Parent Methods

```python id="f4m8qa"
r.a()
r.b()
```

👉 Inherited from parent class.

---

### Overridden Method

```python id="d1q6zx"
r.c()
```

👉 Executes child version.

---

## 🎯 Real-World Importance

Used in:

* Frameworks
* GUI systems
* Game engines
* API design
* Plugin architectures

---

## 🔧 Future Improvements

* Use `super()` inside overridden method
* Add abstract classes
* Demonstrate multilevel overriding
* Compare with Java polymorphism

---

## 📄 License

This project is open-source and free to use.
