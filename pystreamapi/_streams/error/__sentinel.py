class Sentinel:
    """A class used to represent a sentinel value."""

    def __eq__(self, other):
        return isinstance(other, Sentinel)

    def __ne__(self, other):
        return not isinstance(other, Sentinel)

    def __hash__(self):
        return 0  # Return a constant value for all instances
