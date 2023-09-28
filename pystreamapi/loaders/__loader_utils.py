import contextlib
import os


class LoaderUtils:
    """Utility class for loaders to validate paths and cast data"""

    @staticmethod
    def try_cast(value):
        """Try to cast value to primary data types from python (int, float, bool)"""
        for cast in (int, float):
            with contextlib.suppress(ValueError):
                return cast(value)
        # Try to cast to bool
        return value.lower() == 'true' if value.lower() in ('true', 'false') else value

    @staticmethod
    def validate_path(file_path: str):
        """Validate the path to the CSV file"""
        if not os.path.exists(file_path):
            raise FileNotFoundError("The specified file does not exist.")
        if not os.path.isfile(file_path):
            raise ValueError("The specified path is not a file.")
        return file_path
