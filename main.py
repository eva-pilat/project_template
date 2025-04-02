import app.io.input as app_input
import app.io.output as app_output

if __name__ == "__main__":
    file_in = "/Users/evadun/PycharmProjects/project_template/data"
    # data = "{1: 'one', 2: 'two', 3: 'three'}"
    # call our input func and then storing input in the data file
    text_input = app_input.input_from_console()
    app_output.write_file_python(file_in, text_input)

    file_content = app_input.read_file_python(file_in)
    app_output.write_file_python(file_in, file_content)

    file_content_pandas = app_input.read_file_pandas(file_in)
    app_output.write_file_python(file_in, str(file_content_pandas))
