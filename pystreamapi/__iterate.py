def iterate(function, seed_value):
    """
    Create a generator that yields the results of applying the function to the previous value

    :param seed_value: The initial value
    :param function: function: Peek function
    """
    yield seed_value
    while True:
        seed_value = function(seed_value)
        yield seed_value
