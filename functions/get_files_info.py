import os


def get_files_info(working_directory, directory="."):
    full_path = os.path.join(working_directory, directory)
    absolute_path = os.path.abspath(full_path)
    absolute_path_working_dir = os.path.abspath(working_directory)

    if not os.path.isdir(full_path):
        print(f'Error: "{directory}" is not a directory')

    if absolute_path.startswith(absolute_path_working_dir):
        print(f"Result for '{directory}' directory:")

        files = os.listdir(full_path)

        for file in files:
            file_path = os.path.join(absolute_path, file)
            file_size = os.path.getsize(file_path)
            file_is_dir = os.path.isdir(file_path)

            print(f"- {file}: file_size={file_size} bytes, is_dir={file_is_dir}")

    else:
        print(f"Result for '{directory}' directory:")
        print(
            f'\tError: Cannot list "{directory}" as it is outside the permitted working directory'
        )
