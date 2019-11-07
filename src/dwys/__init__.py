import difflib
import tempfile
import re
import subprocess

def parse(string, in_pattern, out_pattern=None):
    """
    Parse a given input text to recover input code blocks and output code
    blocks.
    """
    input_code = re.findall(pattern=in_pattern, string=string)
    if out_pattern is not None:
        output_code = re.findall(pattern=out_pattern, string=string)
    else:
        output_code = None
    return input_code, output_code

def diff(input_code, output_code, execution_command, input_filename=None,
        output_filename=None, expected_output_filename=None):
    """
    Run the input code with the specified <execuation_command>, and generates a
    diff with the output code.
    """
    if input_filename is None:
        input_filename = tempfile.NamedTemporaryFile().name

    if output_filename is None:
        output_filename = tempfile.NamedTemporaryFile().name

    if expected_output_filename is None:
        expected_output_filename = tempfile.NamedTemporaryFile().name

    with open(input_filename, "w") as file_to_write:
        for code_snippet in input_code:
            file_to_write.write(code_snippet)

    with open(expected_output_filename, "w") as file_to_write:
        for code_snippet in output_code:
            file_to_write.write(code_snippet)

    completed_process = subprocess.run([execution_command, input_filename], capture_output=True)
    output = completed_process.stdout.decode("utf-8")

    with open(expected_output_filename, "r") as file_to_read:
        expected_output = file_to_read.read()

    return difflib.unified_diff(expected_output, output, n=0)
