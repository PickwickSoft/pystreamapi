---
description: More complex examples
---

# Examples

Here are two complex examples demonstrating the power of PyStreamAPI

### **Get all numbers from list of different types. Use parallelization.**

```python
Stream.parallel_of([" ", '3', None, "2", 1, ""]) \
    .filter(lambda x: x is not None) \
    .map(str) \
    .map(lambda x: x.strip()) \
    .filter(lambda x: len(x) > 0) \
    .map(int) \
    .sorted()\
    .for_each(print) # 1 2 3
```

### **Generate a Stream of 10 Fibonacci numbers**

```python
def fib():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

Stream.of(fib()) \
    .limit(10) \
    .for_each(print) # 0 1 1 2 3 5 8 13 21 34
```
