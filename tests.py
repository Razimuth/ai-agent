# tests.py

# from subdirectory.filename import function_name
from functions.get_files_info import get_files_info

for test in range(4):
     match test:
        case 0:
             result = get_files_info("calculator", ".")
             print(result)
        case 1:
             result = get_files_info("calculator", "pkg")
             print(result)
        case 2:
             result = get_files_info("calculator", "/bin")
             print(result)
        case 3:
             result = get_files_info("calculator", "../")
             print(result)
       
               