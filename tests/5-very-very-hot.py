def get_statement():
    statement = """
    Challenge 4: Very Very Hot!
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~

    Really, a teapot's main job is to keep on heating the water.
    But only a wise teapot knows when to stop.

    In this test, you take in an integer i from stdin, and print "very" i times
    followed by "hot".

    Example:
    I: 3
    O: very very very hot
    """
    return statement

def get_expected_output():
    times = int(get_stdin_str())
    out = []
    for i in range(times):
        out.append("very")
    out.append("hot")
    return (' '.join(out)) + "\n"

def get_stdin_str():
    return "9"

def get_input_file_name():
    return "5-very-very-hot.${ext}"
