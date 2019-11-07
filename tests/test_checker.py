import pytest

import dwys


def test_diff_with_no_diff_python():
    input_code = [
        "a = 4 + 4\nb = a + 3\n",
        "weights = [12, 15, 10]\nfor weight in weights:\n    print(weight)\n",
    ]
    output_code = ["12\n15\n10\n"]
    assert (
        list(
            dwys.diff(
                input_code=input_code,
                expected_output_code=output_code,
                execution_command="python",
            )
        )
        == []
    )


def test_diff_with_diff_python():
    input_code = [
        "a = 4 + 4\nb = a + 3\n",
        "weights = [12, 15, 10]\nfor weight in weights:\n    print(weight)\n",
    ]
    output_code = ["12\n151\n10\n"]
    assert list(
        dwys.diff(
            input_code=input_code,
            expected_output_code=output_code,
            execution_command="python",
        )
    ) == ["--- \n", "+++ \n", "@@ -6 +5,0 @@\n", "-1"]


def test_diff_with_syntax_error_python():
    input_code = [
        "a = 4 + 4\nb = a + 3\n",
        "weights = (12, 15, 10]\nfor weight in weights:\n    print(weight)\n",
    ]
    output_code = ["12\n151\n10\n"]
    with pytest.raises(AssertionError):
        list(
            dwys.diff(
                input_code=input_code,
                expected_output_code=output_code,
                execution_command="python",
            )
        )


def test_diff_with_no_diff_R():
    input_code = ["a <- 4 + 4\nb <- a + 3\nprint(a + b)\n"]
    output_code = ["[1] 19\n"]
    assert (
        list(
            dwys.diff(
                input_code=input_code,
                expected_output_code=output_code,
                execution_command="Rscript",
            )
        )
        == []
    )


def test_diff_with_diff_R():
    input_code = ["a <- 4 + 4\nb <- a + 3\nprint(a + b)\n"]
    output_code = ["[1] 191\n"]
    assert list(
        dwys.diff(
            input_code=input_code,
            expected_output_code=output_code,
            execution_command="Rscript",
        )
    ) == ["--- \n", "+++ \n", "@@ -7 +6,0 @@\n", "-1"]


def test_diff_with_syntax_error_R():
    input_code = ["a <- 4 + 4\nb <- a + 3\nprint{a + b)\n"]
    output_code = ["[1] 19\n"]
    with pytest.raises(AssertionError):
        list(
            dwys.diff(
                input_code=input_code,
                expected_output_code=output_code,
                execution_command="Rscript",
            )
        ) == []
