import os

from config import MAX_CHARS


def get_file_content(working_directory, file_path):
    full_file_path = os.path.join(working_directory, file_path)
    absolute_path = os.path.abspath(full_file_path)
    absolute_path_working_dir = os.path.abspath(working_directory)

    if not absolute_path.startswith(absolute_path_working_dir):
        return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'

    if not os.path.isfile(full_file_path):
        return f'Error: File not found or is not a regular file: "{file_path}"'

    try:
        with open(full_file_path, "r") as f:
            file_content_string = f.read(MAX_CHARS)

            if f.read() != "":
                file_content_string += (
                    f' [...File "{file_path}" truncated at 10000 characters]'
                )

            return file_content_string
    except Exception as e:
        return f'Error: File "{file_path}" could not be read. {e}'
