# from functions.write_file_content import write_file


# def test():
#     result = write_file("calculator", "lorem.txt", "wait, this isn't lorem ipsum")
#     print(result)

#     result = write_file("calculator", "pkg/morelorem.txt", "lorem ipsum dolor sit amet")
#     print(result)

#     result = write_file("calculator", "/tmp/temp.txt", "this should not be allowed")
#     print(result)


# if __name__ == "__main__":
#     test()


# from functions.get_files_info import get_files_info

# result = get_files_info("calculator", ".")
# print(result)
# print("-------")

# result = get_files_info("calculator", "pkg")
# print(result)
# print("-------")

# result = get_files_info("calculator", "/bin")
# print(result)
# print("-------")

# result = get_files_info("calculator", "../")
# print(result)
# print("-------")

# from functions.get_file_content import get_file_content

# result = get_file_content("calculator", "lorem.txt")
# print(result)

# result = get_file_content("calculator", "main.py")
# print(result)
# result = get_file_content("calculator", "pkg/calculator.py")
# print(result)
# result = get_file_content("calculator", "/bin/cat")
# print(result)
# result = get_file_content("calculator", "pkg/does_not_exist.py")
# print(result)

# from functions.write_file_content import write_file

# result = write_file("calculator", "lorem.txt", "wait, this isn't lorem ipsum")
# print(result)
# result = write_file("calculator", "pkg/morelorem.txt", "lorem ipsum dolor sit amet")
# print(result)
# result = write_file("calculator", "/tmp/temp.txt", "this should not be allowed")
# print(result)

# from functions.run_python import run_python_file

# result = run_python_file("calculator", "main.py")
# print(result)

# result = run_python_file("calculator", "main.py", ["3 + 5"])
# print(result)

# result = run_python_file("calculator", "tests.py")
# print(result)

# result = run_python_file("calculator", "../main.py")
# print(result)

# result = run_python_file("calculator", "nonexistent.py")
# print(result)