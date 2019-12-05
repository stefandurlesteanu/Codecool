""" Accounting module

Data table structure:
    * id (string): Unique and random generated identifier
        at least 2 special characters (except: ';'), 2 number, 2 lower and 2 upper case letters)
    * month (number): Month of the transaction
    * day (number): Day of the transaction
    * year (number): Year of the transaction
    * type (string): in = income, out = outflow
    * amount (int): amount of transaction in USD
"""

import ui
import data_manager
import common

file_name = common.path() + "accounting/items.csv"
table = data_manager.get_table_from_file(file_name)
title_input = "Please enter the product data"
list_labels = ["Id", "Month", "Day", "Year", "Type", "Ammount"]
year_months_day = {"01": 31, "02": 29, "03": 31, "04": 30, "05": 31, "06": 30,
                   "07": 31, "08": 31, "09": 30, "10": 31, "11": 30, "12": 31}
valid_years = [str(x) for x in range(1700, 2020)]
valid_type = ["in", "out"]
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
        global file_name
        table = data_manager.get_table_from_file(file_name)
        start_menu()
        try:
            choose()
        except KeyError as err:
            ui.print_error_message(str(err))


def start_menu():
    options = ["Show Table",
                "Add Item",
                "Remove Item",
                "Update Item",
                "Most profitable year",
                "Average (per item) profit in a given year"]

    ui.print_menu("Accounting menu", options, "Back to main menu")


def choose():
    inventory_option = ui.get_inputs(["Please select option: "], "")[0]
    if inventory_option == "1":
        file_name_local = common.path() + "accounting/items.csv"
        new_table = data_manager.get_table_from_file(file_name_local)
        show_table(new_table)
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
        ui.print_result(which_year_max(table), "Most profitable year")
        return False
    elif inventory_option == "6":
        year = ui.get_inputs([x + ": " for x in ["Year"]], "")[0]
        try:
            while common.validate_years(year) == False:
                ui.print_error_message("Please enter a valid year: ")
                year = ui.get_inputs([x + ": " for x in ["Year"]], "")[0]
        except ValueError:
            return False
        ui.print_result(avg_amount(table, year), "Average (per item) profit in a given year")
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
    ui.print_table(table, list_labels)


def add(table):
    """
    Asks user for input and adds it into the table.

    Args:
        table (list): table to add new record to

    Returns:
        list: Table with a new record
    """
    title_input = "Please enter the product data: "
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


def find_profits(table):
    years_in = {}
    years_out = {}
    profits = {}
    for row in table:
        if row[4] == "in":
            try:
                years_in[row[3]] += int(row[5])
            except KeyError:
                years_in[row[3]] = int(row[5])
        else:
            try:
                years_out[row[3]] += int(row[5])
            except KeyError:
                years_out[row[3]] = int(row[5])
    for key in years_in:
        profits[key] = years_in[key] - years_out[key]
    return profits


def which_year_max(table):
    """
    Question: Which year has the highest profit? (profit = in - out)

    Args:
        table (list): data table to work on

    Returns:
        number
    """
    return int(max(find_profits(table), key=lambda k: find_profits(table)[k]))


def avg_amount(table, year):
    """
    Question: What is the average (per item) profit in a given year? [(profit)/(items count)]

    Args:
        table (list): data table to work on
        year (number)

    Returns:
        number
    """
    counter = 0
    for row in table:
        if row[3] == str(year):
            counter += 1
    return str(round(find_profits(table)[str(year)] / counter, 2))


def save(table):
    while True:
        save_Y_n = (ui.get_inputs(["Do you want to save the changes? (Y/n): "], "")[0]).upper()
        try:
            if save_Y_n == "Y":
                data_manager.write_table_to_file(file_name, table)
                return False
            elif save_Y_n == "N":
                return False
            else:
                raise ValueError
        except ValueError:
            ui.print_error_message("Invalid character! Please choose Y/n")
