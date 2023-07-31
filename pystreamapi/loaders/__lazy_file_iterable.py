class LazyFileIterable:
    """LazyFileIterable is an iterable that loads data from a data source lazily."""

    def __init__(self, loader):
        self.__loader = loader
        self.__data = None

    def __iter__(self):
        self.__load_data()
        return iter(self.__data)

    def __getitem__(self, index):
        self.__load_data()
        return self.__data[index]

    def __len__(self):
        self.__load_data()
        return len(self.__data)

    def __load_data(self):
        """Loads the data from the data source if it has not been loaded yet."""
        if self.__data is None:
            self.__data = self.__loader()
