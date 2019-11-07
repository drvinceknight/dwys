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

def diff(input_code, expected_output_code, execution_command, input_filename=None,):
    """
    Run the input code with the specified <execuation_command>, and generates a
    diff with the output code.
    """
    if input_filename is None:
        input_filename = tempfile.NamedTemporaryFile().name

    with open(input_filename, "w") as file_to_write:
        for code_snippet in input_code:
            file_to_write.write(code_snippet)

    completed_process = subprocess.run([execution_command, input_filename], capture_output=True)
    assert completed_process.stderr == b'', "Syntax error in code"
    output = completed_process.stdout.decode("utf-8")

    # TODO Make the diff usable.
    return difflib.unified_diff("\n".join(expected_output_code), output, n=0)
