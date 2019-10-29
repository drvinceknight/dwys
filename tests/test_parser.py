import dwys
import re

def test_parser_with_basic_delimiters():
    text = """
Here is some text with some python code:

Code starts:
a = 4 + 4
b = a + 3
Code end.

Here is some more code:

Code starts:
weights = [12, 15, 10]
for weight in weights:
    print(weight)
Code end.

Output starts:
12
15
10
Output end.
    """
    in_pattern = re.compile(r"Code starts:\n(.*?)\nCode end", re.DOTALL)
    out_pattern = re.compile(r"Output starts:\n(.*?)\nOutput end", re.DOTALL)

    input_code, output_code = dwys.parse(
            string=text,
            in_pattern=in_pattern,
            out_pattern=out_pattern,
            )
    assert input_code == ["a = 4 + 4\nb = a + 3", "weights = [12, 15, 10]\nfor weight in weights:\n    print(weight)"]
    assert output_code == ['12\n15\n10']

def test_parser_with_latex_delimiters():
    text = r"""
Here is some text with some python code:

\begin{pyin}
a = 4 + 4
b = a + 3
\end{pyin}

Here is some more code:

\begin{pyin}
weights = [12, 15, 10]
for weight in weights:
    print(weight)
\end{pyin}

\begin{pyout}
12
15
10
\end{pyout}
    """
    in_pattern = re.compile(r"\\begin\{pyin\}\n(.*?)\n\\end\{pyin\}", re.DOTALL)
    out_pattern = re.compile(r"\\begin\{pyout\}\n(.*?)\n\\end\{pyout\}", re.DOTALL)

    input_code, output_code = dwys.parse(
            string=text,
            in_pattern=in_pattern,
            out_pattern=out_pattern,
            )
    assert input_code == ["a = 4 + 4\nb = a + 3", "weights = [12, 15, 10]\nfor weight in weights:\n    print(weight)"]
    assert output_code == ['12\n15\n10']
def test_parser_with_basic_delimiters():
    text = """
Here is some text with some python code:

Code starts:
a = 4 + 4
b = a + 3
Code end.

Here is some more code:

Code starts:
weights = [12, 15, 10]
for weight in weights:
    print(weight)
Code end.

Output starts:
12
15
10
Output end.
    """
    in_pattern = re.compile(r"Code starts:\n(.*?)\nCode end", re.DOTALL)
    out_pattern = re.compile(r"Output starts:\n(.*?)\nOutput end", re.DOTALL)

    input_code, output_code = dwys.parse(
            string=text,
            in_pattern=in_pattern,
            out_pattern=out_pattern,
            )
    assert input_code == ["a = 4 + 4\nb = a + 3", "weights = [12, 15, 10]\nfor weight in weights:\n    print(weight)"]
    assert output_code == ['12\n15\n10']
