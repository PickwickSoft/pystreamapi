import unittest
from pystreamapi.__optional import Optional

class TestOptional(unittest.TestCase):
    def test_of(self):
        # Test that creating an Optional with a non-None value works
        optional = Optional.of(5)
        self.assertTrue(optional.is_present())
        self.assertEqual(optional.get(), 5)

        # Test that creating an Optional with None raises a ValueError
        with self.assertRaises(ValueError):
            Optional.of(None)

    def test_empty(self):
        # Test that creating an empty Optional works
        optional = Optional.empty()
        self.assertFalse(optional.is_present())

    def test_get(self):
        # Test that get returns the Optional's value if present
        optional = Optional.of(5)
        self.assertEqual(optional.get(), 5)

        # Test that get raises a ValueError if the Optional is empty
        optional = Optional.empty()
        with self.assertRaises(ValueError):
            optional.get()

    def test_or_else(self):
        # Test that or_else returns the Optional's value if present
        optional = Optional.of(5)
        self.assertEqual(optional.or_else(10), 5)

        # Test that or_else returns the default value if the Optional is empty
        optional = Optional.empty()
        self.assertEqual(optional.or_else(10), 10)

    def test_or_else_get(self):
        # Test that or_else_get returns the Optional's value if present
        optional = Optional.of(5)
        self.assertEqual(optional.or_else_get(lambda: 10), 5)

        # Test that or_else_get returns the supplier's value if the Optional is empty
        optional = Optional.empty()
        self.assertEqual(optional.or_else_get(lambda: 10), 10)

    def test_map(self):
        # Test that map applies the mapper function to the Optional's value
        optional = Optional.of(5)
        mapped_optional = optional.map(lambda x: x * 2)
        self.assertTrue(mapped_optional.is_present())
        self.assertEqual(mapped_optional.get(), 10)

        # Test that map returns an empty Optional if the original Optional is empty
        optional = Optional.empty()
        mapped_optional = optional.map(lambda x: x * 2)
        self.assertFalse(mapped_optional.is_present())

    def test_flat_map(self):
        # Test that flat_map applies the mapper function to the
        # Optional's value and returns the result
        optional = Optional.of(5)
        mapped_optional = optional.flat_map(lambda x: Optional.of(x * 2))
        self.assertTrue(mapped_optional.is_present())
        self.assertEqual(mapped_optional.get(), 10)

        # Test that flat_map returns an empty Optional if the original Optional is empty
        optional = Optional.empty()
        mapped_optional = optional.flat_map(lambda x: Optional.of(x * 2))
        self.assertFalse(mapped_optional.is_present())

        # Test that flat_map raises a TypeError if the mapper function doesn't return an Optional
        optional = Optional.of(5)
        with self.assertRaises(TypeError):
            optional.flat_map(lambda x: x * 2)

    def test_filter(self):
        # Test that filter returns the Optional if the predicate is true
        optional = Optional.of(5)
        filtered_optional = optional.filter(lambda x: x > 3)
        self.assertTrue(filtered_optional.is_present())
        self.assertEqual(filtered_optional.get(), 5)

        # Test that filter returns an empty Optional if the predicate is false
        optional = Optional.of(5)
        filtered_optional = optional.filter(lambda x: x > 10)
        self.assertFalse(filtered_optional.is_present())

        # Test that filter returns an empty Optional if the original Optional is empty
        optional = Optional.empty()
        filtered_optional = optional.filter(lambda x: x > 3)
        self.assertFalse(filtered_optional.is_present())

    def test_if_present(self):
        # Test that if_present calls the consumer function if the Optional is present
        optional = Optional.of(5)
        result = []
        optional.if_present(result.append)
        self.assertEqual(result, [5])

        # Test that if_present doesn't call the consumer function if the Optional is empty
        optional = Optional.empty()
        result = []
        optional.if_present(result.append)
        self.assertEqual(result, [])

    def test_str(self):
        # Test that str returns the string representation of the Optional's value
        optional = Optional.of(5)
        self.assertEqual(str(optional), "Optional(5)")

        # Test that str returns "Optional()" if the Optional is empty
        optional = Optional.empty()
        self.assertEqual(str(optional), "Optional()")

    def test_repr(self):
        # Test that repr returns the string representation of the Optional's value
        optional = Optional.of(5)
        self.assertEqual(repr(optional), "Optional(5)")

        # Test that repr returns "Optional()" if the Optional is empty
        optional = Optional.empty()
        self.assertEqual(repr(optional), "Optional()")

    def test_eq(self):
        # Test that eq returns True if the two Optionals have the same value
        optional1 = Optional.of(5)
        optional2 = Optional.of(5)
        self.assertEqual(optional1, optional2)

        # Test that eq returns False if the two Optionals have different values
        optional1 = Optional.of(5)
        optional2 = Optional.of(10)
        self.assertNotEqual(optional1, optional2)

        # Test that eq returns False if the other object is not an Optional
        optional = Optional.of(5)
        self.assertNotEqual(optional, 5)
