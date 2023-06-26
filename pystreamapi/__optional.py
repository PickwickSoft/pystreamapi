class Optional:
    """
    A container object which may or may not contain a non-none value.

    If a value is present, `is_present()` will return `True` and `get()` will return the value.
    If a value is not present, `is_present()` will return `False`
    and `get()` will raise a `ValueError`.
    Additional methods provide ways to handle the presence or absence of a contained value.

    This class is inspired by Java's `Optional` class.
    """

    def __init__(self, value=None):
        """
        Constructs an Optional with the given value.

        If the value is None, the Optional is considered empty.
        """
        self._value = value
        self._is_present = value is not None

    @staticmethod
    def of(value):
        """
        Returns an Optional with the given non-none value.

        Raises a ValueError if the value is None.
        """
        if value is None:
            raise ValueError("Value cannot be None")
        return Optional(value)

    @staticmethod
    def empty():
        """Returns an empty Optional."""
        return Optional()

    def is_present(self):
        """Returns `True` if the Optional contains a non-none value, `False` otherwise."""
        return self._is_present

    def get(self):
        """Returns the value if present, otherwise raises a `ValueError`."""
        if not self._is_present:
            raise ValueError("Value is not present")
        return self._value

    def or_else(self, default_value):
        """Returns the value if present, otherwise returns the given default value."""
        return self._value if self._is_present else default_value

    def or_else_get(self, supplier):
        """
        Returns the value if present, otherwise calls the given supplier function to get a
        default value.
        """
        return self._value if self._is_present else supplier()

    def map(self, mapper):
        """
        Applies the given mapper function to the value if present, returning a new Optional
        with the result.

        If the Optional is empty, returns an empty Optional.
        """
        if not self._is_present:
            return Optional()
        mapped_value = mapper(self._value)
        return Optional(mapped_value)

    def flat_map(self, mapper):
        """
        Applies the given mapper function to the value if present, returning the result.

        If the Optional is empty, returns an empty Optional.
        If the mapper function does not return an Optional, raises a TypeError.
        """
        if not self._is_present:
            return Optional()
        optional_result = mapper(self._value)
        if not isinstance(optional_result, Optional):
            raise TypeError("Mapper function must return an Optional")
        return optional_result

    def filter(self, predicate):
        """
        Returns an Optional containing the value if present and the predicate is true,
        otherwise an empty Optional.
        """
        return self if self._is_present and predicate(self._value) else Optional()

    def if_present(self, consumer):
        """Calls the given consumer function with the value if present, otherwise does nothing."""
        if self._is_present:
            consumer(self._value)

    def __str__(self):
        """Returns a string representation of the Optional."""
        return f"Optional({self._value if self._is_present else ''})"

    def __repr__(self):
        """Returns a string representation of the Optional."""
        return self.__str__()

    def __eq__(self, other):
        """
        Returns `True` if the other object is an Optional with the same value,
        `False` otherwise.
        """
        return self._value == other._value if isinstance(other, Optional) else False

    def __hash__(self):
        """Returns the hash of the Optional's value."""
        return hash(self._value)
