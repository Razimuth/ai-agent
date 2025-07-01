#get_files_info.py
import os

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

