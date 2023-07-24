from unittest import TestCase

from pystreamapi._streams.__base_stream import BaseStream
from pystreamapi._streams.__parallel_stream import ParallelStream
from pystreamapi._streams.__sequential_stream import SequentialStream
from pystreamapi._streams.numeric.__parallel_numeric_stream import ParallelNumericStream
from pystreamapi._streams.numeric.__sequential_numeric_stream import SequentialNumericStream


class TestStreamConverter(TestCase):

    def test_convert_to_numeric_stream_sequential(self):
        stream = SequentialStream(["1", "2", "3"]).map_to_int()
        self.assertIsInstance(stream, SequentialNumericStream)

    def test_convert_to_numeric_stream_parallel(self):
        stream = ParallelStream(["1", "2", "3"]).map_to_int()
        self.assertIsInstance(stream, ParallelNumericStream)

    def test_convert_to_numeric_stream_numeric_parallel(self):
        stream = ParallelNumericStream(["1", "2", "3"]).map_to_int()
        self.assertIsInstance(stream, ParallelNumericStream)

    def test_convert_to_parallel_stream_sequential(self):
        stream = SequentialStream(["1", "2", "3"]).parallel()
        self.assertIsInstance(stream, ParallelStream)

    def test_convert_to_parallel_stream_sequential_numeric(self):
        stream = SequentialNumericStream(["1", "2", "3"]).parallel()
        self.assertIsInstance(stream, ParallelNumericStream)

    def test_convert_to_parallel_stream_parallel(self):
        stream = ParallelStream(["1", "2", "3"]).parallel()
        self.assertIsInstance(stream, ParallelStream)

    def test_convert_to_parallel_stream_parallel_numeric(self):
        stream = ParallelNumericStream(["1", "2", "3"]).parallel()
        self.assertIsInstance(stream, ParallelNumericStream)

    def test_convert_to_sequential_stream_sequential(self):
        stream = SequentialStream(["1", "2", "3"]).sequential()
        self.assertIsInstance(stream, SequentialStream)

    def test_convert_to_sequential_stream_sequential_numeric(self):
        stream = SequentialNumericStream(["1", "2", "3"]).sequential()
        self.assertIsInstance(stream, SequentialNumericStream)

    def test_convert_to_sequential_stream_parallel(self):
        stream = ParallelStream(["1", "2", "3"]).sequential()
        self.assertIsInstance(stream, SequentialStream)

    def test_convert_to_sequential_stream_parallel_numeric(self):
        stream = ParallelNumericStream(["1", "2", "3"]).sequential()
        self.assertIsInstance(stream, SequentialNumericStream)
