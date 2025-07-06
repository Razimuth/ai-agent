# functions/get_file_content.py

import os
from google.genai import types
from config import MAX_CHARS


def get_file_content(working_directory, file_path):
    abs_working_dir = os.path.abspath(working_directory)
    abs_file_path = os.path.abspath(os.path.join(working_directory, file_path))
    if not abs_file_path.startswith(abs_working_dir):
        return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'
    if not os.path.isfile(abs_file_path):
        return f'Error: File not found or is not a regular file: "{file_path}"'
    try:
        with open(abs_file_path, "r") as f:
            content = f.read(MAX_CHARS)
            if os.path.getsize(abs_file_path) > MAX_CHARS:
                content += (
                    f'[...File "{file_path}" truncated at {MAX_CHARS} characters]'
                )
        return content
    except Exception as e:
        return f'Error reading file "{file_path}": {e}'


schema_get_file_content = types.FunctionDeclaration(
    name="get_file_content",
    description=f"Reads and returns the first {MAX_CHARS} characters of the content from a specified file within the working directory.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="The path to the file whose content should be read, relative to the working directory.",
            ),
        },
        required=["file_path"],
    ),
)


"""
from google.genai import types

import os
from config import MAX_CHARS

def get_file_content(working_directory, file_path):
    abs_working_directory = os.path.abspath(working_directory)
    abs_file_path = os.path.abspath(os.path.join(abs_working_directory, file_path))
    if not abs_file_path.startswith(abs_working_directory):
        return (f'Error: Cannot read "{file_path}" as it is outside the permitted working directory')
    if not os.path.isfile(abs_file_path):
        return (f'Error: File not found or is not a regular file: "{file_path}"')
 
    file_content_string = ""
    try:
        with open(abs_file_path, "r") as file:
            file_content_string = file.read(MAX_CHARS)
            if os.path.getsize(abs_file_path) > MAX_CHARS:
                file_content_string += (F'\n[...File "{file_path}" truncated at 10000 characters]')
    except Exception as e:
        print(f"An error occurred: {e}")

    return file_content_string

schema_get_file_content = types.FunctionDeclaration(
    name="get_file_content",
    description="Lists file contents up to max characters in the specified directory, constrained to the working directory.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="The file_path used to list files from, relative to the working directory. If not provided, lists files in the working directory itself.",
            ),
        },
    ),
)

"""