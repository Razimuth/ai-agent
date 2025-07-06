# functions/get_files_info.py

import os
from google.genai import types

def get_files_info(working_directory, directory=None):
    abs_working_dir = os.path.abspath(working_directory)
    target_dir = abs_working_dir
    if directory:
        target_dir = os.path.abspath(os.path.join(working_directory, directory))
    if not target_dir.startswith(abs_working_dir):
        return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
    if not os.path.isdir(target_dir):
        return f'Error: "{directory}" is not a directory'
    try:
        files_info = []
        for filename in os.listdir(target_dir):
            filepath = os.path.join(target_dir, filename)
            file_size = 0
            is_dir = os.path.isdir(filepath)
            file_size = os.path.getsize(filepath)
            files_info.append(
                f"- {filename}: file_size={file_size} bytes, is_dir={is_dir}"
            )
        return "\n".join(files_info)
    except Exception as e:
        return f"Error listing files: {e}"


schema_get_files_info = types.FunctionDeclaration(
    name="get_files_info",
    description="Lists files in the specified directory along with their sizes, constrained to the working directory.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "directory": types.Schema(
                type=types.Type.STRING,
                description="The directory to list files from, relative to the working directory. If not provided, lists files in the working directory itself.",
            ),
        },
    ),
)


"""
import os
from google.genai import types

def get_files_info(working_directory, directory=None):
    abs_working_directory = os.path.abspath(working_directory)
    abs_directory = os.path.abspath(os.path.join(abs_working_directory, directory))
    if not abs_directory.startswith(abs_working_directory):
        return (f'Error: Cannot list "{directory}" as it is outside the permitted working directory')
    if not os.path.isdir(abs_directory):
        return (f'Error: "{directory}" is not a directory')

    full_details = []
    items = os.listdir(abs_directory)
    for item in items:
        full_path = os.path.join(abs_directory, item)
        size = os.path.getsize(full_path)
        if os.path.isfile(full_path):
            is_dir = False
        elif os.path.isdir(full_path):
            is_dir = True
        details = (f"- {item}: file_size={size} bytes, is_dir={is_dir} ")
        full_details.append(details)

    contents = "\n".join(full_details)
    return contents

schema_get_files_info = types.FunctionDeclaration(
    name="get_files_info",
    description="Lists files in the specified directory along with their sizes, constrained to the working directory.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "directory": types.Schema(
                type=types.Type.STRING,
                description="The directory to list files from, relative to the working directory. If not provided, lists files in the working directory itself.",
            ),
        },
    ),
)

"""