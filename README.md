# dwys: *D*oes *W*hat *Y*ou *S*aid

A language agnostic doctester

## Why?

@geraintpalmer and I are writing a book using both R and Python. We could not
find a solution to doctest our LaTeX files with the custom code environments we
have written so we built this.

## How?

If you have a string with the following:

```python
string = """
Here is some text with some R code:

\begin{Rin}
a <- 4 + 4
b <- a + 3
\end{Rin}

Here is some more code:

\begin{Rin}
for (i in seq(30, 50, 3)) {
  print(i)
}
\end{Rin}

which will give:

\begin{Rout}
30
33
36
39
42
45
48
\end{Rout}
"""
```

The following will test that the code inputs run and that the outputs match:

```python
import re
import dwys 

# Setup the regexes to find the code snippets
in_pattern = re.compile(r"\\begin\{Rin\}\n(.*?)\\end\{Rin\}", re.DOTALL)
out_pattern = re.compile(r"\\begin\{Rout\}\n(.*?)\\end\{Rout\}", re.DOTALL)

# Parse the code
input_code, output_code = dwys.parse(
    string=text, in_pattern=in_pattern, out_pattern=out_pattern
)

# Obtain a diff and the output with the `Rscript` command
dwys.diff(
    input_code=input_code,
    expected_output_code=output_code,
    execution_command="Rscript",
)
```

This can be used in conjunction with a crawler of a file directory to doctest a
number of files.
