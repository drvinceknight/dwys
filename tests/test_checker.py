import dwys

def test_diff_with_no_diff_python():
    input_code = ["a = 4 + 4\nb = a + 3\n", "weights = [12, 15, 10]\nfor weight in weights:\n    print(weight)\n"]
    output_code = ['12\n15\n10\n']
    assert list(dwys.diff(input_code=input_code, output_code=output_code, execution_command="python")) == []

def test_diff_with_diff_python():
    input_code = ["a = 4 + 4\nb = a + 3\n", "weights = [12, 15, 10]\nfor weight in weights:\n    print(weight)\n"]
    output_code = ['12\n151\n10\n']
    assert list(dwys.diff(input_code=input_code, output_code=output_code,
        execution_command="python")) == ['--- \n', '+++ \n', '@@ -6 +5,0 @@\n', '-1']

# def test_diff_with_no_diff_R():
    # input_code = ["a <- 4 + 4\nb <- a + 3\n, print(a + b)\n"]
    # output_code = ['19']
    # assert list(dwys.diff(input_code=input_code, output_code=output_code, execution_command="Rscript")) == []
