# Python Stream API

[![DeepSource](https://deepsource.io/gh/PickwickSoft/pystreamapi.svg/?label=active+issues&show_trend=true&token=7lV9pH1U-N1oId03M-XKZL5B)](https://deepsource.io/gh/PickwickSoft/pystreamapi/?ref=repository-badge)
[![Tests](https://github.com/PickwickSoft/pystreamapi/actions/workflows/unittests.yml/badge.svg)](https://github.com/PickwickSoft/pystreamapi/actions/workflows/unittests.yml)
[![Pylint](https://github.com/PickwickSoft/pystreamapi/actions/workflows/pylint.yml/badge.svg)](https://github.com/PickwickSoft/pystreamapi/actions/workflows/pylint.yml)

PyStreamAPI is a stream library for Python inspired by the Java Stream API and implements almost exact the same method names and functionality as Java Stream API!

PyStreamAPI uses lazy execution and offers sequential as well as parallel streams.

***Now you might think: Why another library? There are so many!***

Here are a few of the advantages this implementation has:

- Sequential as well as parallel version

- Lazy execution

- High speed

- 100% test coverage

- Pythonic implementation

- Clean and easy to read code

**Here a small example:**

```python
from pystreamapi import Stream

Stream.parallel_of([" ", '3', None, "2", 1, ""]) \
    .filter(lambda x: x is not None) \
    .map(str) \
    .map(lambda x: x.strip()) \
    .filter(lambda x: len(x) > 0) \
    .map(int) \
    .sorted() \
    .for_each(print) # Output: 1 2 3
```

The same code in Java:

```java
Object[] words = { " ", '3', null, "2", 1, "" };
Arrays.stream( words )
      .filter( Objects::nonNull )
      .map( Objects::toString )
      .map( String::trim )
      .filter( s -> ! s.isEmpty() )
      .map( Integer::parseInt )
      .sorted()
      .forEach( System.out::println );  // Output: 1 2 3
```

## What is a Stream?

A stream is a pipeline, in which elements from an Iterable are computed on demand.
It is similar to SQL queries and is used to manipulate data. 

E.g. Get the second-highest salary of Employee

```sql
Select distinct Salary from Employee e1 
where 2=Select count(distinct Salary) 
from Employee e2 where e1.salary<=e2.salary;
```

Now the same thing in Python

```python
employees = [...] # A list with employee objects
Stream.of(employees) \
    .map(lambda x: x.salary) \
    .sorted() \
    .reversed() \
    .to_list()[1] # Returns the second-highest salary
```

`pystreamapi.Stream` represents a stream on which one or more operations can be performed. Stream operations are either intermediate or terminal.

The terminal operations return a result of a specific type, and intermediate operations return the stream itself, so we can chain multiple methods together to perform the operation in multiple steps.

*Again the example from above:*

```python
Stream.of(employees) \ # Create a BaseStream object
    .map(lambda x: x.salary) \ # Intermediate Operation
    .sorted() \ # Intermediate Operation
    .reversed() \ # Intermediate Operation
    .to_list()[1] # Terminal Operation
```

Operations can be performed on a stream in parallel or sequentially. When parallel, it is called parallel stream else it is a sequential stream.

Based on the above points, a stream is:

- Not a data structure
- Not offering indexed access
- Designed for lambdas
- Easy to aggregate as lists or tuples/sets
- Parallelizable
- Processing lazy

## Get started: Installation

To start using PyStreamAPI just install the module with this command:

```bash
pip install streams.py  
```

Afterwards you can import it with:

```python
from pystreamapi import Stream
```

:tada: PyStreamAPI is now ready to process your data

## Build a new Stream

There are a few factory methods that create new Streams.

```python
Stream.of([1, 2, 3]) # Can return a sequential or a parallel stream
```

Using the `of()` method will let the implementation decide which `Stream` to use.

> **Note** 
> 
> Currently, it returns always a `SequentialStream`

---

```python
Stream.parallel_of([1, 2, 3]) # Returns a parallel stream
```

---

```python
Stream.sequential_of([1, 2, 3]) # Returns a sequential stream
```

---

```python
Stream.of_noneable([1, 2, 3]) # Can return a sequential or a parallel stream
```

If the source is `None`, you get an empty `Stream`

---

```python
Stream.iterate(0, lambda n: n + 2)
```

Creates a Stream of an infinite Iterator like 0, 2, 4, 6, 8, 10, 12, 14...

> **Note**
> Do not forget to limit the stream with `.limit()`

---

```python
Stream.concat(Stream.of([1, 2]), Stream.of([3, 4])) 
# Like Stream.of([1, 2, 3, 4])
```

Creates a new Stream from multiple Streams. Order doesn't change

## API Documentation

### Intermediate Operations

#### `filter()` : Restrict the Stream

Returns a stream consisting of the elements of this stream that match the given predicate.

```python
Stream.of([1, 2, 3, None]) \
    .filter(lambda x: x is not None) \
    .for_each(print) # 1 2 3
```

#### `map()` : Convert the elements in the Stream

Returns a stream consisting of the results of applying the given function to the elements of this stream.

```python
Stream.of([1, "2", 3.0, None]) \
    .map(str) \
    .to_list() # ["1", "2", "3.0", "None"]
```

#### `map_to_int()` : Convert the elements in the Stream to an Integer

Returns a stream consisting of the results of applying the `int()` function to the elements of this stream. Note that this method is not none safe.

```python
Stream.of([1, "2", 3.0]) \
    .map_to_int() \
    .to_list() # [1, 2, 3]
```

#### m̀ap_to_str() : Convert the elements in the Stream to a String

Returns a stream consisting of the results of applying the `str()` function to the elements of this stream.

```python
Stream.of([1, 2, 3]) \
    .map_to_str() \
    .to_list() # ["1", "2", "3"]
```

#### `flat_map()` : Streams in Streams

Returns a stream consisting of the results of replacing each element of this stream with the contents of a mapped stream produced by applying the provided mapping function to each element.

```python
Stream.of([1, 2, 3]) \
    .flat_map(lambda x: self.stream([x, x])) \
    .to_list() # [1, 1, 2, 2, 3, 3]
```

#### `distinct()` : Remove duplicates

Returns a stream consisting of the distinct elements of this stream.

```python
Stream.of([1, 1, 2, 3]) \
    .distinct() \
    .to_list() # [1, 2, 3]
```

#### `sorted()` : Sort Stream

Returns a stream consisting of the elements of this stream, sorted according to natural order.

```python
Stream.of([2, 9, 1]) \
    .sorted() \
    .to_list() # [1, 2, 9]
```

#### `reversed()` : Reverse Stream

Returns a stream consisting of the elements of this stream in reverse order.

```python
Stream.of([1, 2, 3]) \
    .reversed() \
    .to_list() # [3, 2, 1]
```

#### `peek()` : View intermediate results

Returns a stream consisting of the elements of this stream, additionally performing the provided action on each element as elements are consumed from the resulting stream.

```python
Stream.of([2, 1, 3]) \
    .sorted() \
    .peek(print) \ # 1, 2, 3
    .reversed() \
    .for_each(print) # 3, 2, 1
```

#### `limit()` : Limit the Stream to a certain number of elements

Returns a stream consisting of the elements of this stream, truncated to be no longer than maxSize in length.

```python
Stream.of([1, 2, 3]) \
    .limit(2) \
    .to_list() # [1, 2]
```

#### `skip()` : Skip the first n elements of the Stream

Returns a stream consisting of the remaining elements of this stream after discarding the first n elements of the stream.

```python
Stream.of([1, 2, 3]) \
    .skip(2) \
    .to_list() # [3]
```

#### `take_while()` : Take elements while the predicate is true

Returns, if this stream is ordered, a stream consisting of the longest prefix of elements taken from this stream that match the given predicate.

```python
Stream.of([1, 2, 3]) \
    .take_while(lambda x: x < 3) \
    .to_list() # [1, 2]
```

#### `drop_while()` : Drop elements while the predicate is true

Returns, if this stream is ordered, a stream consisting of the remaining elements of this stream after dropping the longest prefix of elements that match the given predicate.

```python
Stream.of([1, 2, 3]) \
    .drop_while(lambda x: x < 3) \
    .to_list() # [3]
```

### Terminal Operations

These operations will trigger the pipeline's execution

#### `all_match()` : Check if all elements match a predicate

Returns whether all elements of this stream match the provided predicate.

```python
Stream.of([1, 2, 3]) \
    .all_match(lambda x: x > 0) # True
```

#### `any_match()` : Check if any element matches a predicate

Returns whether any elements of this stream match the provided predicate.

```python
Stream.of([1, 2, 3]) \
    .any_match(lambda x: x < 0) # False
```

#### `none_match()` : Check if no element matches a predicate

Returns whether no elements of this stream match the provided predicate.

```python
Stream.of([1, 2, 3]) \
    .none_match(lambda x: x < 0) # True
```

#### `count()` : Count the number of elements in the Stream

Returns the number of elements in this stream.

```python
Stream.of([1, 2, 3]) \
    .count() # 3
```

#### `min()` : Find the minimum element in the Stream

Returns the minimum element of this stream

```python
Stream.of([1, 2, 3]) \
    .min() # 1
```

#### `max()` : Find the maximum element in the Stream

Returns the maximum element of this stream

```python
Stream.of([1, 2, 3]) \
    .max() # 3
```

#### `reduce()` : Reduce the Stream to a single value

Returns the result of reducing the elements of this stream to a single value using the provided reducer.

```python
Stream.of([1, 2, 3]) \
    .reduce(lambda x, y: x + y) # 6
```

#### `for_each()` : Perform an action for each element in the Stream

Performs the provided action for each element of this stream.

```python
Stream.of([1, 2, 3]) \
    .for_each(print) # 1 2 3
```

#### `to_list()` : Convert the Stream to a List

Returns a list containing the elements of this stream.

```python
Stream.of([1, 2, 3]) \
    .to_list() # [1, 2, 3]
```

#### `to_set()` : Convert the Stream to a Set

Returns a set containing the elements of this stream.

```python
Stream.of([1, 2, 3]) \
    .to_set() # {1, 2, 3}
```

#### `to_tuple()` : Convert the Stream to a Tuple

Returns a tuple containing the elements of this stream.

```python
Stream.of([1, 2, 3]) \
    .to_tuple() # (1, 2, 3)
```

#### `find_first()` : Find the first element in the Stream

Returns an Optional describing the first element of this stream, or an empty Optional if the stream is empty.

```python
Stream.of([1, 2, 3]) \
    .find_first() # Optional[1]
```

#### `find_any()` : Find an element in the Stream

Returns an Optional describing an arbitrary element of this stream, or an empty Optional if the stream is empty.

```python
Stream.of([1, 2, 3]) \
    .find_any() # Optional[1]
```

## Complex Examples

#### Get all numbers from list of different types. Use parallelization.

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

#### Generate a Stream of 10 Fibonacci numbers

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

## Performance

Note that parallel Streams are not always faster than sequential Streams. Especially when the number of elements is small, we can expect sequential Streams to be faster.

## Bug Reports

Bug reports can be submitted in GitHub's [issue tracker](https://github.com/PickwickSoft/pystreamapi/issues).

## Contributing

Contributions are welcome! Please submit a pull request or open an issue.