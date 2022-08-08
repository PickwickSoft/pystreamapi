class TestHelper:
    """A simple test helper to test whether lazy execution works well"""

    def __init__(self):
        self.value = 0

    def increment(self, num=0):
        """
        Increments the value member with num

        :param num: Default to 0
        """
        self.value = self.value + num
