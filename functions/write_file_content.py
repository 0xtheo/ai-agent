import os
from google.genai import types

def write_file(working_directory, file_path, content):
    abs_path_work_dir = os.path.abspath(working_directory)
    abs_file_path = os.path.join(abs_path_work_dir, file_path)

    if not abs_file_path.startswith(abs_path_work_dir):
        return f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory'
    try:
        if not os.path.exists(abs_file_path):
            #create dir/file
            os.makedirs(os.path.dirname(abs_file_path), exist_ok=True)
    except Exception as e:
        return f"Error: could not create directory from {file_path}, error is {e}"
    try:
        with open(abs_file_path, "w") as f:
            f.write(content)
    except Exception as e:
        return f"Error: could not write to {file_path}, error is {e}"
    
    # Return successful write to LLM
    return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'

schema_write_file_content = types.FunctionDeclaration(
    name="write_file_content",
    description="Specify the file to write content into and the content to enter into the file.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="Specifies the file to write content to",
            ),
            "content": types.Schema(
                type=types.Type.STRING,
                description="Specifies the content to write to the file",
            ),
        },
    ),
)