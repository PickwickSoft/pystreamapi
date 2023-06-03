# String Conditions

### `contains(x)`: Check if string contains a substring

Returns a condition that checks if a string contains a specified substring.

```python
Stream.of(["apple", "banana", "cherry"] \
    .filter(contains("na")) \
    .for_each(print) # banana
```

### `not_contains(x)`: Check if string does not contain a substring

Returns a condition that checks if a string does not contain a specified substring.

```python
Stream.of(["apple", "banana", "cherry"] \
    .filter(not_contains("na")) \
    .for_each(print) # apple, cherry
```

### `starts_with(x)`: Check if string starts with a substring

Returns a condition that checks if a string starts with a specified substring.

```python
Stream.of(["apple", "banana", "cherry"] \
    .filter(starts_with("ba")) \
    .for_each(print) # banana
```

### `ends_with(x)`: Check if string ends with a substring

Returns a condition that checks if a string ends with a specified substring.

```python
Stream.of(["apple", "banana", "cherry"] \
    .filter(ends_with("ry")) \
    .for_each(print) # cherry
```

### `matches(x)`: Check if string matches a regular expression pattern

Returns a condition that checks if a string matches a specified regular expression pattern.

```python
Stream.of(["apple", "banana", "cherry"] \
    .filter(matches("^a.*e$")) \
    .for_each(print) # apple
```

### `not_matches(x)`: Check if string does not match a regular expression pattern

Returns a condition that checks if a string does not match a specified regular expression pattern.

```python
Stream.of(["apple", "banana", "cherry"] \
    .filter(not_matches("^a.*e$")) \
    .for_each(print) # banana, cherry
```

### `longer_than(x)`: Check if string is longer than a specified length

Returns a condition that checks if a string is longer than a specified length.

```python
Stream.of(["apple", "banana", "cherry"] \
    .filter(longer_than(5)) \
    .for_each(print) # banana, cherry
```

### `shorter_than(x)`: Check if string is shorter than a specified length

Returns a condition that checks if a string is shorter than a specified length.

```python
Stream.of(["apple", "banana", "cherry"] \
    .filter(shorter_than(6)) \
    .for_each(print) # apple
```

### `longer_than_or_equal(x)`: Check if string is longer than or equal to a specified length

Returns a condition that checks if a string is longer than or equal to a specified length.

```python
Stream.of(["apple", "banana", "cherry"] \
    .filter(longer_than_or_equal(6)) \
    .for_each(print) # banana, cherry
```

### `shorter_than_or_equal(x)`: Check if string is shorter than or equal to a specified length

Returns a condition that checks if a string is shorter than or equal to a specified length.

```python
Stream.of(["apple", "banana", "cherry"] \
    .filter(shorter_than_or_equal(5)) \
    .for_each(print) # apple
```

### `equal_to_ignore_case(x)`: Check if string is equal to another string (case-insensitive)

Returns a condition that checks if a string is equal to another string, ignoring the case.

```python
Stream.of(["apple", "banana", "cherry"] \


    .filter(equal_to_ignore_case("BANANA")) \
    .for_each(print) # banana
```

### `not_equal_to_ignore_case(x)`: Check if string is not equal to another string (case-insensitive)

Returns a condition that checks if a string is not equal to another string, ignoring the case.

```python
Stream.of(["apple", "banana", "cherry"] \
    .filter(not_equal_to_ignore_case("BANANA")) \
    .for_each(print) # apple, cherry
```

### `contains_ignore_case(x)`: Check if string contains a substring (case-insensitive)

Returns a condition that checks if a string contains a specified substring, ignoring the case.

```python
Stream.of(["apple", "banana", "cherry"] \
    .filter(contains_ignore_case("AN")) \
    .for_each(print) # apple, banana
```

### `not_contains_ignore_case(x)`: Check if string does not contain a substring (case-insensitive)

Returns a condition that checks if a string does not contain a specified substring, ignoring the case.

```python
Stream.of(["apple", "banana", "cherry"] \
    .filter(not_contains_ignore_case("AN")) \
    .for_each(print) # cherry
```

### `starts_with_ignore_case(x)`: Check if string starts with a substring (case-insensitive)

Returns a condition that checks if a string starts with a specified substring, ignoring the case.

```python
Stream.of(["apple", "banana", "cherry"] \
    .filter(starts_with_ignore_case("BA")) \
    .for_each(print) # banana
```

### `ends_with_ignore_case(x)`: Check if string ends with a substring (case-insensitive)

Returns a condition that checks if a string ends with a specified substring, ignoring the case.

```python
Stream.of(["apple", "banana", "cherry"] \
    .filter(ends_with_ignore_case("RY")) \
    .for_each(print) # cherry
```

### `matches_ignore_case(x)`: Check if string matches a regular expression pattern (case-insensitive)

Returns a condition that checks if a string matches a specified regular expression pattern, ignoring the case.

```python
Stream.of(["apple", "banana", "cherry"] \
    .filter(matches_ignore_case("^A.*E$")) \
    .for_each(print) # apple
```

### `not_matches_ignore_case(x)`: Check if string does not match a regular expression pattern (case-insensitive)

Returns a condition that checks if a string does not match a specified regular expression pattern, ignoring the case.

```python
Stream.of(["apple", "banana", "cherry"] \
    .filter(not_matches_ignore_case("^A.*E$")) \
    .for_each(print) # banana, cherry
```
