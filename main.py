import os
from dotenv import load_dotenv
from functions.get_files_info import schema_get_files_info
from functions.get_file_content import schema_get_file_content
from functions.run_python import schema_run_python_file
from functions.write_file_content import schema_write_file_content

from call_function import call_function, available_functions
from google import genai
from google.genai import types
import sys
from prompts import system_prompt
from config import MAX_ITERS

def main():
    load_dotenv()

    api_key = os.environ.get("GEMINI_API_KEY")
    client = genai.Client(api_key=api_key)



    if len(sys.argv) < 2:
        print("Usage: python3 main.py <question for gemini>")
        exit(1)

    verbose = "--verbose" in sys.argv
    args = [arg for arg in sys.argv[1:] if not arg.startswith("--")]
    user_prompt = " ".join(sys.argv[1:])

    #
    system_prompt = """
    You are a helpful AI coding agent.

    When a user asks a question or makes a request, make a function call plan. You can perform the following operations:

    - List files and directories
    - Read file contents
    - Execute Python files with optional arguments
    - Write or overwrite files

    All paths you provide should be relative to the working directory. You do not need to specify the working directory in your function calls as it is automatically injected for security reasons.
    """

    messages = [
        types.Content(role="user", parts=[types.Part(text=user_prompt)]),
    ]


    if verbose:
        print(f"User prompt: {user_prompt}")

    #print(response)
    iters = 0
    while True:
        iters += 1
        if iters > MAX_ITERS:
            print(f"Maximum iterations ({MAX_ITERS}) reached.")
            sys.exit(1)
        try:
            final_response = generate_content(client, messages, verbose)
            if final_response:
                print(f"Final Response: {final_response}")
                break
        except Exception as e:
            print(f"Error with generate_content, {e}")

def generate_content(client, messages, verbose):

    response = client.models.generate_content(
        model='gemini-2.0-flash-001', 
        contents=messages,
        config=types.GenerateContentConfig(
        tools=[available_functions], system_instruction=system_prompt
        ),
    )
    if not response.function_calls:
        return response.text
    #print(response.text)
    #print(response.function_calls)
    function_responses = []
    try:
        for function_call_part in response.function_calls:
            #print(f"Calling function: {function_call_part.name}({function_call_part.args})")
            func_call_result = call_function(function_call_part)

            if not func_call_result.parts[0].function_response.response:
                raise Exception("Fatal exception: function call result missing")
            elif func_call_result.parts[0].function_response.response and verbose:
                print(f"-> {func_call_result.parts[0].function_response.response}")
            function_responses.append(func_call_result.parts[0])

            if not function_responses:
                print("no function responses generated, exiting")
    except Exception as e:
        return f"Error getting response, {e}"
    
    #print(f"Response: {response.candidates}")
    if response.candidates:
        for candidate in response.candidates:
            #print(f"Candidate: {candidate.content}")
            messages.append(
                candidate.content
                )
        
    messages.append(
        types.Content(role="tool", parts=function_responses)
    )


        
    if verbose:
        print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
        print(f"Response tokens: {response.usage_metadata.candidates_token_count}")




if __name__ == "__main__":
    main()