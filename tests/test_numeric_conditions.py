import unittest
from pystreamapi.conditions import *


class TestNumericConditions(unittest.TestCase):

    def test_even(self):
        self.assertTrue(even(0))
        self.assertTrue(even(2))
        self.assertTrue(even(-2))
        self.assertFalse(even(1))
        self.assertFalse(even(-1))

    def test_odd(self):
        self.assertTrue(odd(1))
        self.assertTrue(odd(-1))
        self.assertFalse(odd(0))
        self.assertFalse(odd(2))
        self.assertFalse(odd(-2))

    def test_positive(self):
        self.assertTrue(positive(1))
        self.assertTrue(positive(2))
        self.assertFalse(positive(-1))
        self.assertFalse(positive(0))
        self.assertFalse(positive(-2))

    def test_negative(self):
        self.assertTrue(negative(-1))
        self.assertTrue(negative(-2))
        self.assertFalse(negative(0))
        self.assertFalse(negative(1))
        self.assertFalse(negative(2))

    def test_zero(self):
        self.assertTrue(zero(0))
        self.assertFalse(zero(1))
        self.assertFalse(zero(-1))

    def test_non_zero(self):
        self.assertTrue(non_zero(1))
        self.assertTrue(non_zero(-1))
        self.assertFalse(non_zero(0))

    def test_greater_than(self):
        greater_than_5 = greater_than(5)
        self.assertTrue(greater_than_5(6))
        self.assertFalse(greater_than_5(5))
        self.assertFalse(greater_than_5(4))

    def test_greater_than_or_equal(self):
        greater_than_or_equal_5 = greater_than_or_equal(5)
        self.assertTrue(greater_than_or_equal_5(6))
        self.assertTrue(greater_than_or_equal_5(5))
        self.assertFalse(greater_than_or_equal_5(4))

    def test_less_than(self):
        less_than_5 = less_than(5)
        self.assertTrue(less_than_5(4))
        self.assertFalse(less_than_5(5))
        self.assertFalse(less_than_5(6))

    def test_less_than_or_equal(self):
        less_than_or_equal_5 = less_than_or_equal(5)
        self.assertTrue(less_than_or_equal_5(4))
        self.assertTrue(less_than_or_equal_5(5))
        self.assertFalse(less_than_or_equal_5(6))

    def test_between(self):
        between_3_and_5 = between(3, 5)
        self.assertTrue(between_3_and_5(4))
        self.assertFalse(between_3_and_5(2))
        self.assertFalse(between_3_and_5(6))

    def test_not_between(self):
        not_between_3_and_5 = not_between(3, 5)
        self.assertTrue(not_between_3_and_5(2))
        self.assertTrue(not_between_3_and_5(6))
        self.assertFalse(not_between_3_and_5(4))

    def test_equal_to(self):
        equal_to_5 = equal_to(5)
        self.assertTrue(equal_to_5(5))
        self.assertFalse(equal_to_5(4))
        self.assertFalse(equal_to_5(6))

    def test_not_equal_to(self):
        not_equal_to_5 = not_equal_to(5)
        self.assertTrue(not_equal_to_5(4))
        self.assertTrue(not_equal_to_5(6))
        self.assertFalse(not_equal_to_5(5))

    def test_multiple_of(self):
        self.assertTrue(multiple_of(3)(9))
        self.assertFalse(multiple_of(3)(10))

    def test_not_multiple_of(self):
        self.assertTrue(not_multiple_of(3)(10))
        self.assertFalse(not_multiple_of(3)(9))

    def test_divisor_of(self):
        self.assertTrue(divisor_of(9)(3))
        self.assertFalse(divisor_of(3)(10))

    def test_not_divisor_of(self):
        self.assertTrue(not_divisor_of(3)(10))
        self.assertFalse(not_divisor_of(9)(3))

    def test_prime(self):
        self.assertTrue(prime(7))
        self.assertFalse(prime(10))

    def test_not_prime(self):
        self.assertTrue(not_prime(10))
        self.assertFalse(not_prime(7))

    def test_perfect_square(self):
        self.assertTrue(perfect_square(9))
        self.assertFalse(perfect_square(10))

    def test_not_perfect_square(self):
        self.assertTrue(not_perfect_square(10))
        self.assertFalse(not_perfect_square(9))

    def test_perfect_cube(self):
        self.assertTrue(perfect_cube(8))
        self.assertFalse(perfect_cube(9))

    def test_not_perfect_cube(self):
        self.assertTrue(not_perfect_cube(9))
        self.assertFalse(not_perfect_cube(8))

    def test_perfect_power(self):
        self.assertTrue(perfect_power(16))
        self.assertFalse(perfect_power(17))

    def test_not_perfect_power(self):
        self.assertTrue(not_perfect_power(17))
        self.assertFalse(not_perfect_power(16))

    def test_palindrome(self):
        self.assertTrue(palindrome("racecar"))
        self.assertFalse(palindrome("hello"))

    def test_not_palindrome(self):
        self.assertTrue(not_palindrome("hello"))
        self.assertFalse(not_palindrome("racecar"))

    def test_armstrong(self):
        self.assertTrue(armstrong(153))
        self.assertFalse(armstrong(10))

    def test_not_armstrong(self):
        self.assertTrue(not_armstrong(10))
        self.assertFalse(not_armstrong(153))

    def test_narcissistic(self):
        self.assertTrue(narcissistic(153))
        self.assertFalse(narcissistic(10))

    def test_not_narcissistic(self):
        self.assertTrue(not_narcissistic(10))
        self.assertFalse(not_narcissistic(153))

    def test_happy(self):
        self.assertTrue(happy(19))
        self.assertFalse(happy(4))

    def test_sad(self):
        self.assertTrue(sad(4))
        self.assertFalse(sad(19))

    def test_abundant(self):
        self.assertTrue(abundant(12))
        self.assertFalse(abundant(7))

    def test_not_abundant(self):
        self.assertTrue(not_abundant(7))
        self.assertFalse(not_abundant(12))

    def test_deficient(self):
        self.assertTrue(deficient(7))
        self.assertFalse(deficient(12))

    def test_not_deficient(self):
        self.assertTrue(not_deficient(12))
        self.assertFalse(not_deficient(7))

    def test_perfect(self):
        self.assertTrue(perfect(6))
        self.assertFalse(perfect(7))

    def test_not_perfect(self):
        self.assertTrue(not_perfect(7))
        self.assertFalse(not_perfect(6))
