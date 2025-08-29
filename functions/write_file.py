import os


def write_file(working_directory, file_path, content):
    full_file_path = os.path.join(working_directory, file_path)
    absolute_path = os.path.abspath(full_file_path)
    absolute_path_working_dir = os.path.abspath(working_directory)

    if not absolute_path.startswith(absolute_path_working_dir):
        return f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory'

    if not os.path.exists(full_file_path):
        parent_dir = os.path.dirname(full_file_path)

        try:
            os.makedirs(parent_dir, exist_ok=True)

        except Exception as e:
            return f"Error: {e}"

    try:
        with open(full_file_path, "w") as f:
            f.write(content)
        return (
            f'Successfully wrote to "{file_path}" ({len(content)} characters written)'
        )

    except OSError as e:
        return f"Error: {e}"
