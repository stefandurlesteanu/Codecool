""" User Interface (UI) module """


def print_table(table, title_list):
    """
    Prints table with data.

    Example:
        /-----------------------------------\
        |   id   |      title     |  type   |
        |--------|----------------|---------|
        |   0    | Counter strike |    fps  |
        |--------|----------------|---------|
        |   1    |       fo       |    fps  |
        \-----------------------------------/

    Args:
        table (list): list of lists - table to display
        title_list (list): list containing table headers

    Returns:
        None: This function doesn't return anything it only prints to console.
    """
    title_lenght = []
    for elements in title_list:
        title_lenght.append(len(elements))
    for row in table:
        for index in range(len(row)):
            if len(row[index]) > title_lenght[index]:
                title_lenght[index] = len(row[index])
    table_width = (len(title_list) + 1) + (len(title_list) * 2) - 2
    for row in title_lenght:
        table_width += row
    top_bottom_line = '-' * table_width
    print(f'\n\t/{top_bottom_line}\\')
    string_title = ''
    string_tabulator = ''
    for index in range(len(title_list)):
        string_title += '| {0:^{1}} '.format(
            title_list[index], title_lenght[index])
        string_tabulator += '|{0:^{1}}'.format(
            '-' * ((title_lenght[index]) + 2), title_lenght[index])
    print('\t' + string_title + '|')
    print('\t' + string_tabulator + '|')
    for row in table:
        string_table = ''
        for index in range(len(row)):
            string_table += '| {0:^{1}} '.format(
                row[index], title_lenght[index])
        print(f'\t{string_table}|')
        if row != table[-1]:
            print(f'\t{string_tabulator}|')
    print(f'\t\\{top_bottom_line}/\n')


def print_result(result, label):
    """
    Displays results of the special functions.

    Args:
        result: result of the special function (string, number, list or dict)
        label (str): label of the result

        None: This function doesn't return anything it only prints to console.
    """
    print("#" * 3, label, "#" * 3)
    if isinstance(result, (int, str)):
        print(result)
    elif isinstance(result, dict):
        for i in result.items():
            print(i[0], i[1])
    elif isinstance(result, list):
        if isinstance(result[0], str):
            for i in result:
                print(i)
        elif isinstance(result[0], list):
            for i in result:
                print(i)
    print ("\n")


def print_menu(title, list_options, exit_message):
    """
    Displays a menu. Sample output:
        Main menu:
            (1) Store manager
            (2) Human resources manager
            (3) Inventory manager
            (4) Accounting manager
            (5) Sales manager
            (6) Customer relationship management (CRM)
            (0) Exit program

    Args:
        title (str): menu title
        list_options (list): list of strings - options that will be shown in menu
        exit_message (str): the last option with (0) (example: "Back to main menu")

    Returns:
        None: This function doesn't return anything it only prints to console.
    """
    print("\n" + '#' * 3, title, "#" * 3)
    for count, option in enumerate(list_options):
        print(f"({count + 1}) {option}")
    print(f"({0}) {exit_message}")


def get_inputs(list_labels, title):
    """
    Gets list of inputs from the user.
    Sample call:
        get_inputs(["Name","Surname","Age"],"Please provide your personal information")
    Sample display:
        Please provide your personal information
        Name <user_input_1>
        Surname <user_input_2>
        Age <user_input_3>

    Args:
        list_labels (list): labels of inputs
        title (string): title of the "input section"

    Returns:
        list: List of data given by the user. Sample return:
            [<user_input_1>, <user_input_2>, <user_input_3>]
    """
    inputs = []
    print(title)
    for i in range(0, len(list_labels)):
        user_input = input(f"\t{list_labels[i].title()}")
        inputs.append(user_input)
    return inputs


def print_error_message(message):
    """
    Displays an error message (example: ``Error: @message``)

    Args:
        message (str): error message to be displayed

    Returns:
        None: This function doesn't return anything it only prints to console.
    """
    print('\nError: {}'.format(message))

