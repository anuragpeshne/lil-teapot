def get_statement():
    statement = """
    Challenge 4: Add some Sugar
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~

    Some people add sugar, milk, lemon, choco and what not to their tea.
    Teapots must know some Maths!

    Take 3 integers as input, one on each line, and sum them up.
    - If the sum is greater than 100, subtract 110
    - else add 180
    """
    return statement

def get_expected_output():
    int_str_list = get_stdin_str().split("\n")
    int_list = [int(i) for i in int_str_list if i != '']
    sum = int_list[0] + int_list[1] + int_list[2]
    if sum > 100:
        return str(sum - 110) + "\n"
    else:
        return str(sum + 180) + "\n"

def get_stdin_str():
    return "22\n43\n123\n"

def get_input_file_name():
    return "4-add-some-sugar.${ext}"
