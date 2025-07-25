import os
from google.genai import types

def get_files_info(working_directory, directory="."):
    abs_path_work_dir = os.path.abspath(working_directory)
    #print(working_directory)
    #print(abs_path_work_dir)
    #print(working_directory)
    target_dir = working_directory
    if directory:
        target_dir = os.path.abspath(os.path.join(working_directory, directory))
    #print(target_dir)
    if not target_dir.startswith(abs_path_work_dir):
        return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
    if not os.path.isdir(target_dir):
        return f'Error: "{directory}" is not a directory'
    
    #print(os.getcwd())
    try:
        files_info = []
        contents = os.listdir(target_dir)
        #print(contents)
        for filename in contents:
            filepath = os.path.join(target_dir, filename)
            file_size = 0
            is_dir = os.path.isdir(filepath)
            file_size = os.path.getsize(filepath)
            files_info.append(
                f"- {filename}: file_size={file_size} bytes, is_dir={is_dir}"
            )
        # print("\n".join(files_info))
        return "\n".join(files_info)
            # if os.path.exists(filename):
            #     print(f"- {filename}: file_size={os.path.getsize(filename)} bytes, is_dir={os.path.isdir(filename)}")
            #print(f"- {file}", end="")
            #filesize = os.path.getsize(file)
            # if not os.path.exists(filename):
            #     print(f"File {filename} did not exist")
        #print(contents)
    except Exception as e:
        return f"Error listing files: {e}"

#get_files_info("/home/theos/workspace/github.com/0xtheo/ai-agent/calculator", "pkg")

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