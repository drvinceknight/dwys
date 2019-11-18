import difflib
import re
import subprocess
import tempfile


def parse(string, in_pattern, out_pattern=None):
    """
    Parse a given input text to recover input code blocks and output code
    blocks.
j   """
    input_code = re.findall(pattern=in_pattern, string=string)
    if out_pattern is not None:
        output_code = re.findall(pattern=out_pattern, string=string)
    else:
        output_code = None
    return input_code, output_code


def diff(
    input_code,
    expected_output_code,
    execution_command,
    input_filename=None,
    spacing="\n\n",
):
    """
    Run the input code with the specified <execuation_command>, and generates a
    diff with the output code.
    """
    if input_filename is None:
        input_filename = tempfile.NamedTemporaryFile().name

    with open(input_filename, "w") as file_to_write:
        if input_code != []:
            for code_snippet in input_code[:-1]:
                file_to_write.write(code_snippet)
                file_to_write.write(spacing)

            file_to_write.write(input_code[-1])

    completed_process = subprocess.run(
        [execution_command, input_filename], capture_output=True
    )
    assert completed_process.stderr == b"", "Syntax error in code"
    output = completed_process.stdout.decode("utf-8").rstrip()

    expected_output = "\n".join(expected_output_code)
    # TODO Make the diff usable.
    return difflib.unified_diff(expected_output, output, n=2), output, expected_output
