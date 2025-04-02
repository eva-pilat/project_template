import os
import unittest
import pandas.errors
import app.io.input as inp


class ReadFilePython(unittest.TestCase):

    def test_exist_file(self):
        """Check to see if an existing file is being read correctly.
        """
        project_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir, os.pardir))
        filename = os.path.join(project_dir, 'data', 'input.csv')
        expected_text = "x,y,z\n2,5,9\n5,1,4\n5,15,68"
        self.assertEqual(inp.read_file_python(filename), expected_text)

    def test_not_exist_file(self):
        """Check to see if a non-existent file has been detected correctly.
        """
        project_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir, os.pardir))
        filename = os.path.join(project_dir, 'data', 'test_table_new.csv')
        with self.assertRaises(FileNotFoundError):
            inp.read_file_python(filename)

    def test_empty_file(self):
        """Check for correct processing of an empty file.
        """
        project_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir, os.pardir))
        filename = os.path.join(project_dir, 'data', 'input_copy.csv')
        self.assertEqual(inp.read_file_python(filename), "")


class ReadFilePandas(unittest.TestCase):

    def test_exist_file(self):
        """Check to see if an existing file is being read correctly. (with pandas)
        """
        project_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir, os.pardir))
        filename = os.path.join(project_dir, 'data', 'input.csv')
        expected_text = ['x', 'y', 'z']
        self.assertEqual(list(inp.read_file_pandas(filename)), expected_text)

    def test_not_exist_file(self):
        """Check to see if a non-existent file has been detected correctly. (with pandas)
        """
        project_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir, os.pardir))
        filename = os.path.join(project_dir, 'data', 'test_table_new.csv')
        with self.assertRaises(FileNotFoundError):
            inp.read_file_pandas(filename)

    def test_empty_file(self):
        """Check for correct processing of an empty file. (with pandas)
        """
        project_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir, os.pardir))
        filename = os.path.join(project_dir, 'data', 'input_copy.csv')
        with self.assertRaises(pandas.errors.EmptyDataError):
            inp.read_file_pandas(filename)


if __name__ == '__main__':
    unittest.main()