# import sys
# import os
# modules_dir = os.path.expanduser(
#     "/Users/alexandruoriean/codecool/5_tw_week/erp/")
# sys.path.append(modules_dir)
import common  # common module
import data_manager  # data manager module
import ui  # User interface module

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
# everything you'll need is imported:

file_name = "/home/stefan/Codecool/Python/5th_TW_week/lightweight-erp-python-phoenix/accounting/items.csv"
table = data_manager.get_table_from_file(file_name)
title = "Please enter the product data"
list_labels = ["id", "month", "day", "year", "type", "ammount"]
year_months_day = {"01": 31, "02": 29, "03": 31, "04": 30, "05": 31, "06": 30, "07": 31, "08": 31, "09": 30, "10": 31, "11": 30, "12": 31}
valid_years = [str(x) for x in range(1700, 2020)]
valid_type = ["in", "out"]

def validate_day(month, day):
    return day <= year_months_day[month]


def validate_month(month):
    return int(month) in range(1, 13)

def validate_type(value):
    return value in valid_type


def validate_years(year):
    return year in valid_years


def validate_ammount(ammount):
    return ammount.isnumeric() and ammount >= 0

account_validators = [validate_day, validate_month, validate_type, validate_ammount]

def start_module():
    """
    Starts this module and displays its menu.
     * User can access default special features from here.
     * User can go back to main menu from here.

    Returns:
        None
    """

    # you code


def show_table(table):
    """
    Display a table

    Args:
        table (list): list of lists to be displayed.

    Returns:
        None
    """
    # your code
    ui.print_table(table, list_labels)


def add(table):
    """
    Asks user for input and adds it into the table.

    Args:
        table (list): table to add new record to

    Returns:
        list: Table with a new record
    """

    # your code
    inputs  = ui.get_inputs(list_labels, title)
    # valid_values = []
    # for inpt in range(len(inputs)):
    #     valid_values.append(validators[inpt](inputs[inpt]))
    # if all(valid_values):
    table.append(inputs)
    return table


print(ui.print_table(add(table), list_labels))


def remove(table, id_):
    """
    Remove a record with a given id from the table.

    Args:
        table (list): table to remove a record from
        id_ (str): id of a record to be removed

    Returns:
        list: Table without specified record.
    """
    # your code
    for row in table:
        if row[0] == id_:
            table.remove(row)
    return table


def update(table, id_):
    """
    Updates specified record in the table. Ask users for new data.

    Args:
        table (list): list in which record should be updated
        id_ (str): id of a record to update

    Returns:
        list: table with updated record
    """

    # your code

    return table


# special functions:
# ------------------


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
    return round(find_profits(table)[str(year)] / counter, 2)
