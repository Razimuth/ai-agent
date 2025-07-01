# tests.py

# from subdirectory.filename import function_name
#from functions.get_files_info import get_files_info
from functions.get_file_content import get_file_content

def test():
     result = get_file_content("calculator", "main.py")
     print(f"{result}\n")

     result = get_file_content("calculator", "pkg/calculator.py")
     print(f"{result}\n")

     result = get_file_content("calculator", "/bin/cat")
     print(f"{result}\n")




#     result = get_file_content("calculator", "lorem.txt")
#     print(f"{result}\n")

 #    result = get_files_info("calculator", ".")
 #    print(f"{result}\n")

#     result = get_files_info("calculator", "pkg")
#     print(f"{result}\n")
     
#     result = get_files_info("calculator", "/bin")
#     print(f"{result}\n")

#     result = get_files_info("calculator", "../")
#     print(f"{result}\n")


if __name__ == "__main__":
     test()



       
               