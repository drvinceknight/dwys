import re

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
