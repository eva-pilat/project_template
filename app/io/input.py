import pandas as pd


def input_from_console():
    """Reads text from user input"""
    value = input("Please, input something")
    return value


def read_file_python(filepath):
    """
        Reads file content using built-in open

        Args:
            filepath(str): Path to file that needs to be read.

        Returns:
            data: Data frame from file.
    """
    with open(filepath, "r") as f:
        return f.read()


def read_file_pandas(filepath):
    """
        Reads file content using pandas

        Args:
            filepath(str): Path to file that needs to be read.

        Returns:
            data: pd.DataFrame
    """
    data = pd.read_csv(filepath)
    return data
