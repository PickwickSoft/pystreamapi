class Optional:
    def __init__(self, value=None):
        self._value = value
        self._is_present = value is not None

    @staticmethod
    def of(value):
        if value is None:
            raise ValueError("Value cannot be None")
        return Optional(value)

    @staticmethod
    def empty():
        return Optional()

    def is_present(self):
        return self._is_present

    def get(self):
        if not self._is_present:
            raise ValueError("Value is not present")
        return self._value

    def or_else(self, default_value):
        return self._value if self._is_present else default_value

    def or_else_get(self, supplier):
        return self._value if self._is_present else supplier()

    def map(self, mapper):
        if not self._is_present:
            return Optional()
        mapped_value = mapper(self._value)
        return Optional(mapped_value)

    def flat_map(self, mapper):
        if not self._is_present:
            return Optional()
        optional_result = mapper(self._value)
        if not isinstance(optional_result, Optional):
            raise TypeError("Mapper function must return an Optional")
        return optional_result

    def filter(self, predicate):
        return self if self._is_present and predicate(self._value) else Optional()

    def if_present(self, consumer):
        if self._is_present:
            consumer(self._value)

    def __str__(self):
        return f"Optional({self._value if self._is_present else ''})"

    def __repr__(self):
        return self.__str__()

    def __eq__(self, other):
        return self._value == other._value if isinstance(other, Optional) else False
