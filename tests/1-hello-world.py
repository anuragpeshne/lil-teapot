from string import Template

def get_statement():
    statement = """
    Challenge 1: Introduction
    ~~~~~~~~~~~~~~~~~~~~~~~~~

    Hello, welcome to the "li'l teapot" test. This test consists of very simple
    challenges which will help you to learn syntax of new language.
    The motive of these challenges are not to test your algorithmic skills but
    to get you acquainted with basic syntax and standard library of the language.

    After a challenge is displayed, a new file will be created and you need to
    fill it with code to pass the test.

    So let's get started. Here's your first challenge, it will test if you can
    write to standard out.
    """
    return Template(statement).safe_substitute(expected_output=get_expected_output(),
                                               input_file_name=get_input_file_name())

def get_expected_output():
    output = "Hello World, I'm a li'l teapot!\n"
    return output

def get_input_file_name():
    return "1-hello-world.${ext}"


def get_stdin_str():
    return ""
