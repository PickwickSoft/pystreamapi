# Numeric Conditions

### `even()`: Check if number is even

Returns a condition that checks if a number is even.

```python
Stream.of([1, 2, 3, 4, 5] \
    .filter(even()) \
    .for_each(print) # 2, 4
```

### `odd()`: Check if number is odd

Returns a condition that checks if a number is odd.

```python
Stream.of([1, 2, 3, 4, 5] \
    .filter(odd()) \
    .for_each(print) # 1, 3, 5
```

### `positive()`: Check if number is positive

Returns a condition that checks if a number is positive.

```python
Stream.of([-1, 0, 2, -3, 4] \
    .filter(positive()) \
    .for_each(print) # 2, 4
```

### `negative()`: Check if number is negative

Returns a condition that checks if a number is negative.

```python
Stream.of([-1, 0, 2, -3, 4] \
    .filter(negative()) \
    .for_each(print) # -1, -3
```

### `zero()`: Check if number is zero

Returns a condition that checks if a number is zero.

```python
Stream.of([-1, 0, 2, -3, 4] \
    .filter(zero()) \
    .for_each(print) # 0
```

### `non_zero()`: Check if number is non-zero

Returns a condition that checks if a number is non-zero.

```python
Stream.of([-1, 0, 2, -3, 4] \
    .filter(non_zero()) \
    .for_each(print) # -1, 2, -3, 4
```

### `greater_than(n)`: Check if number is greater than a given value

Returns a condition that checks if a number is greater than a given value.

```python
Stream.of([1, 2, 3, 4, 5] \
    .filter(greater_than(3)) \
    .for_each(print) # 4, 5
```

### `greater_than_or_equal(n)`: Check if number is greater than or equal to a given value

Returns a condition that checks if a number is greater than or equal to a given value.

```python
Stream.of([1, 2, 3, 4, 5] \
    .filter(greater_than_or_equal(3)) \
    .for_each(print) # 3, 4, 5
```

### `less_than(n)`: Check if number is less than a given value

Returns a condition that checks if a number is less than a given value.

```python
Stream.of([1, 2, 3, 4, 5] \
    .filter(less_than(3)) \
    .for_each(print) # 1, 2
```

### `less_than_or_equal(n)`: Check if number is less than or equal to a given value

Returns a condition that checks if a number is less than or equal to a given value.

```python
Stream.of([1, 2, 3, 4, 5] \
    .filter(less_than_or_equal(3)) \
    .for_each(print) # 1, 2, 3
```

### `between(minimum, maximum)`: Check if number is between two given values

Returns a condition that checks if a number is between two given values (inclusive).

```python
Stream.of([1, 2, 3, 4, 5] \
    .filter(between(2, 4)) \
    .for_each(print) # 2, 3, 4
```

### `not_between(minimum, maximum)`: Check if number is not between two given values

Returns a condition that checks if a number is not between two given values (inclusive).

```python
Stream.of([1, 2, 3, 4, 5] \
    .filter(not_between(2, 4)) \
    .for_each(print) # 1, 5
```

### `equal_to(n)`: Check if number is equal to a given value

Returns a condition that checks if a number is equal to a given value.

```python
Stream.of([1, 2, 3, 4, 5] \
    .filter(equal_to(3)) \
    .for_each(print) # 3
```

### `not_equal_to(n)`: Check if number is not equal to a given value

Returns a condition that checks if a number is not equal to a given value.

```python
Stream.of([1, 2, 3, 4, 5] \
    .filter(not_equal_to(3)) \
    .for_each(print) # 1, 2, 4, 5
```

### `multiple_of(n)`: Check if number is a multiple of a given value

Returns a condition that checks if a number is a multiple of a given value.

```python
Stream.of([1, 2, 3, 4, 5] \
    .filter(multiple_of(2)) \
    .for_each(print) # 2, 4
```

### `not_multiple_of(n)`: Check if number is not a multiple of a given value

Returns a condition that checks if a number is not a multiple of a given value.

```python
Stream.of([1, 2, 3, 4, 5] \
    .filter(not_multiple_of(2)) \
    .for_each(print) # 1, 3, 5
```

### `divisor_of(n)`: Check if number is a divisor of a given value

Returns a condition that checks if a number is a divisor of a given value.

```python
Stream.of([1, 2, 3, 4, 5] \
    .filter(divisor_of(12)) \
    .for_each(print) # 1, 2, 3, 4, 6, 12
```

### `not_divisor_of(n)`: Check if number is not a divisor of a given value

Returns a condition that checks if a number is not a divisor of a given value.

```python
Stream.of([1, 2, 3, 4, 5] \
    .filter(not_divisor_of(12)) \
    .for_each(print) # 5
```

### `prime()`: Check if number is prime

Returns a condition that checks if a number is prime.

```python
Stream.of([1, 2, 3, 4, 5] \
    .filter(prime()) \
    .for_each(print) # 2, 3, 5
```

### `not_prime()`: Check if number is not prime

Returns a condition that checks if a number is not prime.

```python
Stream.of([1, 2, 3, 4, 5]

 \
    .filter(not_prime()) \
    .for_each(print) # 1, 4
```

### `perfect_square()`: Check if number is a perfect square

Returns a condition that checks if a number is a perfect square.

```python
Stream.of([1, 2, 3, 4, 5] \
    .filter(perfect_square()) \
    .for_each(print) # 1, 4
```

### `not_perfect_square()`: Check if number is not a perfect square

Returns a condition that checks if a number is not a perfect square.

```python
Stream.of([1, 2, 3, 4, 5] \
    .filter(not_perfect_square()) \
    .for_each(print) # 2, 3, 5
```

### `perfect_cube()`: Check if number is a perfect cube

Returns a condition that checks if a number is a perfect cube.

```python
Stream.of([1, 2, 3, 4, 5] \
    .filter(perfect_cube()) \
    .for_each(print) # 1
```

### `not_perfect_cube()`: Check if number is not a perfect cube

Returns a condition that checks if a number is not a perfect cube.

```python
Stream.of([1, 2, 3, 4, 5] \
    .filter(not_perfect_cube()) \
    .for_each(print) # 2, 3, 4, 5
```

### `perfect_power()`: Check if number is a perfect power

Returns a condition that checks if a number is a perfect power.

```python
Stream.of([1, 2, 3, 4, 5] \
    .filter(perfect_power()) \
    .for_each(print) # 1, 4
```

### `not_perfect_power()`: Check if number is not a perfect power

Returns a condition that checks if a number is not a perfect power.

```python
Stream.of([1, 2, 3, 4, 5] \
    .filter(not_perfect_power()) \
    .for_each(print) # 2, 3, 5
```

### `palindrome()`: Check if number is a palindrome

Returns a condition that checks if a number is a palindrome.

```python
Stream.of([12321, 456, 78987] \
    .filter(palindrome()) \
    .for_each(print) # 12321, 78987
```

### `not_palindrome()`: Check if number is not a palindrome

Returns a condition that checks if a number is not a palindrome.

```python
Stream.of([12321, 456, 78987] \
    .filter(not_palindrome()) \
    .for_each(print) # 456
```

### `armstrong()`: Check if number is an Armstrong number

Returns a condition that checks if a number is an Armstrong number.

```python
Stream.of([153, 370, 9474] \
    .filter(armstrong()) \
    .for_each(print) # 153, 370, 9474
```

### `not_armstrong()`: Check if number is not an Armstrong number

Returns a condition that checks if a number is not an Armstrong number.

```python
Stream.of([153, 370, 9474] \
    .filter(not_armstrong()) \
    .for_each(print) # None
```

### `narcissistic()`: Check if number is a narcissistic number

Returns a condition that checks if a number is a narciss

istic number.

```python
Stream.of([153, 370, 9474] \
    .filter(narcissistic()) \
    .for_each(print) # 153, 370, 9474
```

### `not_narcissistic()`: Check if number is not a narcissistic number

Returns a condition that checks if a number is not a narcissistic number.

```python
Stream.of([153, 370, 9474] \
    .filter(not_narcissistic()) \
    .for_each(print) # None
```

### `happy()`: Check if number is a happy number

Returns a condition that checks if a number is a happy number.

```python
Stream.of([19, 32, 86] \
    .filter(happy()) \
    .for_each(print) # 19, 32
```

### `sad()`: Check if number is a sad number

Returns a condition that checks if a number is a sad number.

```python
Stream.of([19, 32, 86] \
    .filter(sad()) \
    .for_each(print) # 86
```

### `abundant()`: Check if number is an abundant number

Returns a condition that checks if a number is an abundant number.

```python
Stream.of([12, 16, 28] \
    .filter(abundant()) \
    .for_each(print) # 12, 16, 28
```

### `not_abundant()`: Check if number is not an abundant number

Returns a condition that checks if a number is not an abundant number.

```python
Stream.of([12, 16, 28] \
    .filter(not_abundant()) \
    .for_each(print) # None
```

### `deficient()`: Check if number is a deficient number

Returns a condition that checks if a number is a deficient number.

```python
Stream.of([12, 16, 28] \
    .filter(deficient()) \
    .for_each(print) # None
```

### `not_deficient()`: Check if number is not a deficient number

Returns a condition that checks if a number is not a deficient number.

```python
Stream.of([12, 16, 28] \
    .filter(not_deficient()) \
    .for_each(print) # 12, 16, 28
```

### `perfect()`: Check if number is a perfect number

Returns a condition that checks if a number is a perfect number.

```python
Stream.of([6, 28, 496] \
    .filter(perfect()) \
    .for_each(print) # 6, 28, 496
```

### `not_perfect()`: Check if number is not a perfect number

Returns a condition that checks if a number is not a perfect number.

```python
Stream.of([6, 28, 496] \
    .filter(not_perfect()) \
    .for_each(print) # None
```
