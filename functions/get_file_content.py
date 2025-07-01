# get_file_content.py

import os
MAX_CHARS = 10000

def get_file_content(working_directory, file_path):
    abs_working_directory = os.path.abspath(working_directory)
    abs_file_path = os.path.abspath(os.path.join(abs_working_directory, file_path))
    if not abs_file_path.startswith(abs_working_directory):
        return (f'Error: Cannot read "{file_path}" as it is outside the permitted working directory')

    file_content_string = ""
    try:
        with open(abs_file_path, "r") as file:
            size = os.path.getsize(abs_file_path)
            file_content_string = file.read(MAX_CHARS)
            if size > MAX_CHARS:
                file_content_string += (F'\n[...File "{file_path}" truncated at 10000 characters]')
    except FileNotFoundError:
        return (f'Error: File not found or is not a regular file: "{file_path}"')
    except Exception as e:
        print(f"An error occurred: {e}")

    return file_content_string


