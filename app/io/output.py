def write_to_console(data):
    """
        Prints data to the console

        Args:
            data(Any): Everything that needs to be printed to the console.
    """
    print(data)
    pass


def write_file_python(filepath, data):
    """
        Writes data to file using built-in open

        Args:
            filepath(str): Path to file that will be storing data.
            data(Any): Everything that needs to be saved in the file.
    """
    with open(filepath, "w") as f:
        f.write(data)
    pass
