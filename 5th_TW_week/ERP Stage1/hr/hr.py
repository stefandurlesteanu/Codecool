""" Inventory module

Data table structure:
    * id (string): Unique and random generated identifier
        at least 2 special characters (except: ';'), 2 number, 2 lower and 2 upper case letters)
    * name (string): Name of item
    * manufacturer (string)
    * purchase_year (number): Year of purchase
    * durability (number): Years it can be used
"""
import ui
import data_manager
import common


list_labels = ["id", "name", "year"]
read_file = common.path() + "hr/persons.csv"
table = data_manager.get_table_from_file(read_file)
back_to_main_menu = True

def start_module():
    """
    Starts this module and displays its menu.
     * User can access default special features from here.
     * User can go back to main menu from here.

    Returns:
        None
    """
    global back_to_main_menu
    back_to_main_menu = True
    while back_to_main_menu == True:
        global table
        global read_file
        table = data_manager.get_table_from_file(read_file)
        start_menu()
        try:
            choose()
        except KeyError as err:
            ui.print_error_message(str(err))


def start_menu():
    options = ["Show table",
               "Add new item",
               "Remove item",
               "Update item",
               "Get Oldest Person",
               "Get Persons Closest to Average"]

    ui.print_menu("Human Resources Manager", options, "Back to main menu")


def choose():
    inventory_option = ui.get_inputs(["Please select option: "], "")[0]
    if inventory_option == "1":
        show_table(table)
        return False
    elif inventory_option == "2":
        add_new_table = add(table)
        show_table(add_new_table)
        save(add_new_table)
    elif inventory_option == "3":
        remove_table = remove(table, id())
        try:
            show_table(remove_table)
            save(remove_table)
        except TypeError:
            return False
        return False
    elif inventory_option == "4":
        updated_table = update(table, id())
        try:
            show_table(updated_table)
            save(updated_table)
        except TypeError:
            return False
        return False
    elif inventory_option == "5":
        ui.print_result(get_oldest_person(table), "Oldest person")
        return False
    elif inventory_option == "6":
        ui.print_result(get_persons_closest_to_average(table), "Closest to average age")
        return False
    elif inventory_option == "0":
        global back_to_main_menu
        back_to_main_menu = False
        return back_to_main_menu
    else:
        raise KeyError("There is no such option.")

def show_table(table):
    """
    Display a table

    Args:
        table (list): list of lists to be displayed.

    Returns:
        None
    """
    title_list = list_labels
    ui.print_table(table, title_list)


def add(table):
    """
    Asks user for input and adds it into the table.

    Args:
        table (list): table to add new record to

    Returns:
        list: Table with a new record
    """
    title_input = "Please insert new manager: "
    inputs = ui.get_inputs([x + ": " for x in list_labels[1:]], title_input)
    inputs.insert(0, common.generate_random(table))
    table.append(inputs)

    return table


def remove(table, id):
    """
    Remove a record with a given id from the table.

    Args:
        table (list): table to remove a record from
        id (str): id of a record to be removed

    Returns:
        list: Table without specified record.
    """
    while id != "EXIT":
        new_table = []
        for i in range(len(table)):
            if id == table[i][0]:
                continue
            else:
                new_table.append(table[i])
        table = new_table
        return table
    

def id():
    """
    Generates a unique ID and validates its uniqueness. 
    Use it as argument for "update" function!
    Args:
        None
    Returns:
        Verified unique ID
    """
    valid_ids = [item[0] for item in table]
    id_label = ["Unique ID: "]
    while True:
        id_ = ui.get_inputs(id_label, "Please insert unique id: ")
        if id_[0] not in valid_ids and (id_[0]).upper() != "EXIT":
            ui.print_error_message("Not a valid ID!\n")
        elif (id_[0]).upper() == "EXIT":
            return (id_[0]).upper()
        else:
            return id_[0]


def update(table, id_):
    """
    Updates specified record in the table. Ask users for new data.

    Args:
        table (list): list in which record should be updated
        id_ (str): id of a record to update

    Returns:
        list: table with updated record
    """
    print(id_)
    while id_ != "EXIT":
        title = "Provide new data:"
        new_values = ui.get_inputs([x + ": " for x in list_labels[1:]], title)
        check_id = id_
        for line in table:
            if check_id in line:
                for item in range(1, len(line)):
                    line[item] = new_values[item-1]
        return table


def get_oldest_person(table):
    """
    Question: Who is the oldest person?

    Args:
        table (list): data table to work on

    Returns:
        list: A list of strings (name or names if there are two more with the same value)
    """
    count_for_table = 0
    list_age = []
    while count_for_table < len(table):

        list_age.append(table[count_for_table][2])
        count_for_table += 1
    max_list_age = max(list_age)
    name_list = []
    count_table_age = 0
    while count_table_age < len(table):
        if max_list_age == str(table[count_table_age][2]):
            name_list.append(table[count_table_age][1])
            count_table_age += 1
        else:
            count_table_age += 1
    return name_list


def get_persons_closest_to_average(table):
    """
    Question: Who is the closest to the average age?

    Args:
        table (list): data table to work on

    Returns:
        list: list of strings (name or names if there are two more with the same value)
    """
    sum_number = 0
    average_year = 0
    for count_for_year in range(len(table)):
        sum_number += int(table[count_for_year][2])
    average_year = sum_number / len(table)

    list_min_avr_year = []
    list_max_avr_year = []
    for row in range(len(table)):
        if int(table[row][2]) < average_year:
            list_min_avr_year.append(table[row][2])
    for row in range(len(table)):
        if int(table[row][2]) > average_year:
            list_max_avr_year.append(table[row][2])
    min_avr_year = max(list_min_avr_year)
    max_avr_year = min(list_max_avr_year)
    final_year = ''
    if (int(max_avr_year) - average_year) < (average_year - int(min_avr_year)):
        final_year += max_avr_year
    else:
        final_year += min_avr_year
    list_name_persons_closest_to_average = []
    d = 0
    while d < len(table):
        if final_year == table[d][2]:
            list_name_persons_closest_to_average.append(table[d][1])
        d += 1
    return list_name_persons_closest_to_average


def save(table):
    while True:
        save_Y_n = (ui.get_inputs(["Do you want to save the changes? (Y/n): "], "")[0]).upper()
        try:
            if save_Y_n == "Y":
                data_manager.write_table_to_file(read_file, table)
                return False
            elif save_Y_n == "N":
                return False
            else:
                raise ValueError
        except ValueError:
            ui.print_error_message("Invalid character! Please choose Y/n")
