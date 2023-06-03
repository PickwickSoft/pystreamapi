# Terminal Operations

### `all_match()` : Check if all elements match a predicate

Returns whether all elements of this stream match the provided predicate.

```python
Stream.of([1, 2, 3]) \
    .all_match(lambda x: x > 0) # True
```

### **`any_match()` : Check if any element matches a predicate**

Returns whether any elements of this stream match the provided predicate.

```python
Stream.of([1, 2, 3]) \
    .any_match(lambda x: x < 0) # False
```

### `count()` : Count the number of elements in the Stream

Returns the number of elements in this stream.

```python
Stream.of([1, 2, 3]) \
    .count() # 3
```

### `find_any()` : Find an element in the Stream

Returns an Optional describing an arbitrary element of this stream, or an empty Optional if the stream is empty.

```python
Stream.of([1, 2, 3]) \
    .find_any() # Optional[1]
```

### `find_first()` : Find the first element in the Stream

Returns an Optional describing the first element of this stream, or an empty Optional if the stream is empty.

```python
Stream.of([1, 2, 3]) \
    .find_first() # Optional[1]
```

### `for_each()` : Perform an action for each element in the Stream

Performs the provided action for each element of this stream.

```python
Stream.of([1, 2, 3]) \
    .for_each(print) # 1 2 3
```

### `none_match()` : Check if no element matches a predicate

Returns whether no elements of this stream match the provided predicate.

```python
Stream.of([1, 2, 3]) \
    .none_match(lambda x: x < 0) # True
```

### `min()` : Find the minimum element in the Stream

Returns the minimum element of this stream

```python
Stream.of([1, 2, 3]) \
    .min() # 1
```

### **`max()` : Find the maximum element in the Stream**

Returns the maximum element of this stream

```python
Stream.of([1, 2, 3]) \
    .max() # 3
```

### `reduce()` : Reduce the Stream to a single value

Returns the result of reducing the elements of this stream to a single value using the provided reducer.

```python
Stream.of([1, 2, 3]) \
    .reduce(lambda x, y: x + y) # 6
```

### `to_list()` : Convert the Stream to a List

Returns a list containing the elements of this stream.

```python
Stream.of([1, 2, 3]) \
    .to_list() # [1, 2, 3]
```

### **`to_set()` : Convert the Stream to a Set**

Returns a set containing the elements of this stream.

```python
Stream.of([1, 2, 3]) \
    .to_set() # {1, 2, 3}
```

### **`to_tuple()` : Convert the Stream to a Tuple**

Returns a tuple containing the elements of this stream.

```python
Stream.of([1, 2, 3]) \
    .to_tuple() # (1, 2, 3)
```
