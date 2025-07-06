# tests.py

# from subdirectory.filename import function_name
#from functions.get_files_info import get_files_info
#from functions.get_file_content import get_file_content
#from functions.write_file import write_file
from functions.run_python_file import run_python_file

def test():

     result = run_python_file("calculator", "main.py")
     print(f"{result}\n")

     result = run_python_file("calculator", "tests.py")
     print(f"{result}\n")

     result = run_python_file("calculator", "../main.py")
     print(f"{result}\n")

     result = run_python_file("calculator", "nonexistent.py")
     print(f"{result}\n")

#     result = write_file("calculator", "lorem.txt", "wait, this isn't lorem ipsum")
#     print(f"{result}\n")

#     result = write_file("calculator", "pkg/morelorem.txt", "lorem ipsum dolor sit amet")
#     print(f"{result}\n")

#     result = write_file("calculator", "/tmp/temp.txt", "this should not be allowed")
#     print(f"{result}\n")


#     result = get_file_content("calculator", "main.py")
#     print(f"{result}\n")

#     result = get_file_content("calculator", "pkg/calculator.py")
#     print(f"{result}\n")

#     result = get_file_content("calculator", "/bin/cat")
#     print(f"{result}\n")

#     result = get_file_content("calculator", "lorem.txt")
#     print(f"{result}\n")

#     result = get_files_info("calculator", ".")
#     print(f"{result}\n")

#     result = get_files_info("calculator", "pkg")
#     print(f"{result}\n")
     
#     result = get_files_info("calculator", "/bin")
#     print(f"{result}\n")

#     result = get_files_info("calculator", "../")
#     print(f"{result}\n")


if __name__ == "__main__":
     test()



       
               