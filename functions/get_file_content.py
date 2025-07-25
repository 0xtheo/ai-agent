import os
from google.genai import types
from config import MAX_CHARS


def get_file_content(working_directory, file_path):
    abs_path_work_dir = os.path.abspath(working_directory)
    abs_file_path = os.path.join(abs_path_work_dir, file_path)
    #print(abs_path_work_dir)
    #print(abs_file_path)
    if not abs_file_path.startswith(abs_path_work_dir):
        return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'
    if not os.path.isfile(abs_file_path):
        return f'Error: File not found or is not a regular file: "{file_path}"'
    
    try:
        with open(abs_file_path, "r") as f:
            file_content_string = f.read(MAX_CHARS)
            if os.path.getsize(abs_file_path) > MAX_CHARS:
                file_content_string += f'[...File "{file_path}" truncated at 10000 characters]'
            return file_content_string
    except Exception as e:
        return f"Error reading from file: {e}"

    


#get_file_content("calculator", "main.py")

schema_get_file_content = types.FunctionDeclaration(
    name="get_file_content",
    description="Reads content from file in the specified directory.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="The file to read from.",
            ),
        },
    ),
)