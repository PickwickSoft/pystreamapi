# Intermediate Operations

### **`distinct()` : Remove duplicates**

Returns a stream consisting of the distinct elements of this stream.

```python
Stream.of([1, 1, 2, 3]) \
    .distinct() \
    .to_list() # [1, 2, 3]
```

### **`drop_while()` : Drop elements while the predicate is true**

Returns, if this stream is ordered, a stream consisting of the remaining elements of this stream after dropping the longest prefix of elements that match the given predicate.

```python
Stream.of([1, 2, 3]) \
    .drop_while(lambda x: x < 3) \
    .to_list() # [3]
```

### **`filter()` : Restrict the Stream**

Returns a stream consisting of the elements of this stream that match the given predicate.

```python
Stream.of([1, 2, 3, None]) \
    .filter(lambda x: x is not None) \
    .for_each(print) # 1 2 3
```

### **`flat_map()` : Streams in Streams**

Returns a stream consisting of the results of replacing each element of this stream with the contents of a mapped stream produced by applying the provided mapping function to each element.

```python
Stream.of([1, 2, 3]) \
    .flat_map(lambda x: Stream.of([x, x])) \
    .to_list() # [1, 1, 2, 2, 3, 3]
```

### `group_by()`: Group the stream by a given key

Returns a stream consisting of the elements of this stream, grouped by the given classifier and extracting the key/value pairs.

```python
class Point:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    def __str__(self):
        return f"Point({self.x}, {self.y})"

Stream.of([Point(1, 2), Point(1, 5), Point(3, 4), Point(3, 1)]) \
    .group_by(lambda p: p.x) \
    .map(lambda g: (g[0], [str(p) for p in g[1]])) \
    .for_each(print)  # (1, ['Point(1, 2)', 'Point(1, 5)'])
                      # (3, ['Point(3, 4)', 'Point(3, 1)'])
```

### `limit()` : Limit the Stream to a certain number of elements

Returns a stream consisting of the elements of this stream, truncated to be no longer than max\_size.

```python
Stream.of([1, 2, 3]) \
    .limit(2) \
    .to_list() # [1, 2]
```

### **`map()` : Convert the elements in the Stream**

Returns a stream consisting of the results of applying the given function to the elements of this stream.

```python
Stream.of([1, "2", 3.0, None]) \
    .map(str) \
    .to_list() # ["1", "2", "3.0", "None"]
```

### `map_to_int()` : Convert the elements in the Stream to an Integer

Returns a stream consisting of the results of applying the `int()` function to the elements of this stream. Note that this method is not none safe.

```python
Stream.of([1, "2", 3.0]) \
    .map_to_int() \
    .to_list() # [1, 2, 3]
```

### `map_to_str()` : Convert the elements in the Stream to a String

Returns a stream consisting of the results of applying the `str()` function to the elements of this stream.

```python
Stream.of([1, 2, 3]) \
    .map_to_str() \
    .to_list() # ["1", "2", "3"]
```

### `peek()` : View intermediate results

Returns a stream consisting of the elements of this stream, additionally performing the provided action on each element as elements are consumed from the resulting stream.

```python
Stream.of([2, 1, 3]) \
    .sorted() \
    .peek(print) \ # 1, 2, 3
    .reversed() \
    .for_each(print) # 3, 2, 1
```

### `reversed()` : Reverse Stream

Returns a stream consisting of the elements of this stream in reverse order.

```python
Stream.of([1, 2, 3])
    .reversed()
    .to_list()  # [3, 2, 1]
```

### `skip()` : Skip the first n elements of the Stream

Returns a stream consisting of the remaining elements of this stream after discarding the first n elements of the stream.

```python
Stream.of([1, 2, 3]) \
    .skip(2) \
    .to_list() # [3]
```

### `sorted()` : Sort Stream

Returns a stream consisting of the elements of this stream, sorted according to natural order or comparator.

```python
Stream.of([2, 9, 1])
    .sorted()
    .to_list()  # [1, 2, 9]
```

Here is an example with a custom comparator:

```python
Stream.of(["a", "cc", "bbb"])
    .sorted(lambda x, y: len(y) - len(x))
    .to_list()  # ['bbb', 'cc', 'a']
```

### `take_while()` : Take elements while the predicate is true

Returns, if this stream is ordered, a stream consisting of the longest prefix of elements taken from this stream that match the given predicate.

```python
Stream.of([1, 2, 3]) \
    .take_while(lambda x: x < 3) \
    .to_list() # [1, 2]
```
