def one_of(*conditions):
    """Returns a condition that is true if any of the given conditions are true.

    Args:
        *conditions: A list of conditions.

    Returns:
        A condition that is true if any of the given conditions are true.
    """
    return lambda x: any(c(x) for c in conditions)
