def get_statement():
    statement = """
    Challenge 3: Tea or Coffee - Choose one
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    Teapots are good at making Coffee too!
    But you can make either tea or coffee, not both.

    Take an integer as input:
    - if the integer is even print "Coffee"
    - else print "Tea"
    """
    return statement

def get_expected_output():
    if int(get_stdin_str()) % 2 == 0:
        return "Coffee\n"
    else:
        return "Tea\n"

def get_stdin_str():
    return "2"

def get_input_file_name():
    return "3-tea-or-coffee.${ext}"
