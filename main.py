import app.io.input as app_input
import app.io.output as app_output

if __name__ == "__main__":
    file_in_txt = "/Users/evadun/PycharmProjects/project_template/data/input.txt"
    file_in_csv = "/Users/evadun/PycharmProjects/project_template/data/input.csv"
    file_copy_csv = "/Users/evadun/PycharmProjects/project_template/data/input_copy.csv"
    # data = "{1: 'one', 2: 'two', 3: 'three'}"
    # call our input func and then storing input in the data file
    text_input = app_input.input_from_console()
    app_output.write_file_python(file_in_txt, text_input)

    file_content = app_input.read_file_python(file_in_csv)
    app_output.write_file_python(file_copy_csv, file_content)

    file_content_pandas = app_input.read_file_pandas(file_in_csv)
    app_output.write_file_python(file_in_csv, str(file_content_pandas))
