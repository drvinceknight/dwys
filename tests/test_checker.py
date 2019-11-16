import pytest

import dwys


def test_diff_with_no_diff_python():
    input_code = [
        "a = 4 + 4\nb = a + 3\nprint(b)\n",
        "weights = [12, 15, 10]\nfor weight in weights:\n    print(weight)\n",
    ]
    expected_output_code = ["11\n12\n15\n10"]
    diff, output_code, expected_output = dwys.diff(
        input_code=input_code,
        expected_output_code=expected_output_code,
        execution_command="python",
    )
    assert expected_output_code == [output_code]


def test_diff_with_diff_python():
    input_code = [
        "a = 4 + 4\nb = a + 3\n",
        "weights = [12, 15, 10]\nfor weight in weights:\n    print(weight)\n",
    ]
    expected_output_code = ["12\n151\n10\n"]
    diff, output_code, expected = dwys.diff(
        input_code=input_code,
        expected_output_code=expected_output_code,
        execution_command="python",
    )
    assert expected_output_code != [output_code]


def test_diff_with_syntax_error_python():
    input_code = [
        "a = 4 + 4\nb = a + 3\n",
        "weights = (12, 15, 10]\nfor weight in weights:\n    print(weight)\n",
    ]
    output_code = ["12\n151\n10\n"]
    with pytest.raises(AssertionError):
        dwys.diff(
            input_code=input_code,
            expected_output_code=output_code,
            execution_command="python",
        )


def test_diff_with_no_diff_R():
    input_code = ["a <- 4 + 4\nb <- a + 3\nprint(a + b)\n"]
    expected_output_code = ["[1] 19"]
    diff, output_code, expected = dwys.diff(
        input_code=input_code,
        expected_output_code=expected_output_code,
        execution_command="Rscript",
    )
    assert list(diff) == []
    assert expected_output_code == [output_code]


def test_diff_with_diff_R():
    input_code = ["a <- 4 + 4\nb <- a + 3\nprint(a + b)\n"]
    expected_output_code = ["[1] 191\n"]
    diff, output_code, expected = dwys.diff(
        input_code=input_code,
        expected_output_code=expected_output_code,
        execution_command="Rscript",
    )
    assert list(diff) == [
        "--- \n",
        "+++ \n",
        "@@ -5,4 +5,2 @@\n",
        " 1",
        " 9",
        "-1",
        "-\n",
    ]
    assert expected_output_code != [output_code]


def test_diff_with_syntax_error_R():
    input_code = ["a <- 4 + 4\nb <- a + 3\nprint{a + b)\n"]
    output_code = ["[1] 19\n"]
    with pytest.raises(AssertionError):
        dwys.diff(
            input_code=input_code,
            expected_output_code=output_code,
            execution_command="Rscript",
        )
