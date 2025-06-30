#get_files_info.py
import os

def get_files_info(working_directory, directory=None):
    absolute_working_directory = os.path.abspath(working_directory)
    absolute_directory = os.path.abspath(os.path.join(absolute_working_directory, directory))
    if not absolute_directory.startswith(absolute_working_directory):
        return (f'Error: Cannot list "{directory}" as it is outside the permitted working directory')
    if not os.path.isdir(absolute_directory):
        return (f'Error: "{directory}" is not a directory')

    full_details = []
    items = os.listdir(absolute_directory)
    for item in items:
        full_path = os.path.join(absolute_directory, item)
        size = os.path.getsize(full_path)
        if os.path.isfile(full_path):
            is_dir = False
        elif os.path.isdir(full_path):
            is_dir = True
        details = (f"- {item}: file_size={size} bytes, is_dir={is_dir} ")
        full_details.append(details)

    contents = "\n".join(full_details)
    return contents

