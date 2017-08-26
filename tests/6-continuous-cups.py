import math

def get_statement():
    statement = """
    Challenge 6: Continuous Cups
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    Some cups are discrete, and some are continuous as threads in table cloth.
    Teapots must know how to distribute the tea in both!

    Take in two floating point numbers from stdin, volume of tea and cup.
    Give an integer and a double (upto 6 decimal places) which represent the
    number of cups that can be filled. Make sure to print the two values on
    separate lines.

    Example
    Input:
    22.0
    7.0
    Output:
    4
    3.142857
    """
    return statement

def get_expected_output():
    int_str_list = get_stdin_str().split("\n")
    tea_size = float(int_str_list[0])
    cup_size = float(int_str_list[1])
    ans = (str(math.ceil(tea_size / cup_size)) + "\n")
    ans = ans + '{:0.6f}'.format(tea_size / cup_size) + "\n"
    return ans

def get_stdin_str():
    return "22.0\n7.0\n"

def get_input_file_name():
    return "6-continuous-cups.${ext}"
