# Type Conditions

### `of_type(cls)`: Check if object is of type

Checks if an element is an instance of the specified class.

```python
Stream.of([1, 3.4, "A", None] \
    .filter(of_type(int)) \
    .for_each(print) # 1
```

### `not_of_type(cls: Type)`: Check if object is not of type

Checks if an element is not an instance of the specified class.

```python
Stream.of([1, 3.4, "A", None] \
   .filter(not_of_type(int)) \
   .for_each(print) # 3.4, "A", None
```

### `none()`: Check if object is None

Checks if an element is `None`.

```python
Stream.of([1, None, "Hello", None] \
   .filter(none()) \
   .for_each(print) # None, None
```

### `not_none()`: Check if object is not None

Checks if an element is not `None`.

```python
Stream.of([1, None, "Hello", None] \
   .filter(not_none()) \
   .for_each(print) # 1, "Hello"
```

### `true()`: Check if object is True

Checks if an element is `True`.

```python
Stream.of([True, False, "Yes", 0] \
   .filter(true()) \
   .for_each(print) # True
```

### `not_true()`: Check if object is not True

Checks if an element is not `True`.

```python
Stream.of([True, False, "Yes", 0] \
   .filter(not_true()) \
   .for_each(print) # False, "Yes", 0
```

### `false()`: Check if object is False

Checks if an element is `False`.

```python
Stream.of([True, False, "Yes", 0] \
   .filter(false()) \
   .for_each(print) # False
```

### `not_false()`: Check if object is not False

Checks if an element is not `False`.

```python
Stream.of([True, False, "Yes", 0] \
   .filter(not_false()) \
   .for_each(print) # True, "Yes", 0
```

### `length(x)`: Check if object has specified length

Checks if an element has the specified length.

```python
Stream.of(["apple", "banana", "cherry", "kiwi"] \
   .filter(length(5)) \
   .for_each(print) # apple
```

### `not_length(x)`: Check if object does not have specified length

Checks if an element does not have the specified length.

```python
Stream.of(["apple", "banana", "cherry", "kiwi"] \
   .filter(not_length(6)) \
   .for_each(print) # apple, kiwi
```

### `empty()`: Check if object is empty

Checks if an element is empty (e.g., an empty list, string, etc.).

```python
Stream.of([[], "", {}, set(), None, 0] \
    .filter(empty()) \
    .for_each(print) # [], "", {}, set()
```

### `not_empty()`: Check if object is not empty

Checks if an element is not empty.

```python
Stream.of([[], "", {}, set(), None, 0] \
    .filter(not_empty()) \
    .for_each(print) # None, 0
```

### `equal(x)`: Check if object is equal to the specified value

Checks if an element is equal to the specified value.

```python
Stream.of([1, 2, 3, 4, 5] \
    .filter(equal(3)) \
    .for_each(print) # 3
```

### `not_equal(x)`: Check if object is not equal to the specified value

Checks if an element is not equal to the specified value.

```python
Stream.of([1, 2, 3, 4, 5] \
    .filter(not_equal(3)) \
    .for_each(print) # 1, 2, 4, 5
```
