""" Common module
implement commonly used functions here
"""

import random


def get_table_from_file(file_name):
    """
    Reads csv file and returns it as a list of lists.
    Lines are rows columns are separated by ";"

    Args:
        file_name (str): name of file to read

    Returns:
         list: List of lists read from a file.
    """
    with open(file_name, "r") as file:
        lines = file.readlines()
    table = [element.replace("\n", "").split(";") for element in lines]
    return table

def generate_id():
    random_id = ''

    char1 = chr(random.randint(65, 90))
    char2 = chr(random.randint(97, 122))
    char3 = str(random.randint(10, 100))
    char4 = chr(random.randint(65, 90))
    char5 = chr(random.randint(97, 122))
    char6 = chr(random.randint(35, 38))
    char7 = chr(random.randint(35, 38))

    random_id = random_id + char1 + char2 + char3 + char4 + char5 + char6 + char7
    return random_id

def generate_random(table):
    """
    Generates random and unique string. Used for id/key generation:
         - at least 2 special characters (except: ';'), 2 number, 2 lower and 2 upper case letter
         - it must be unique in the table (first value in every row is the id)

    Args:
        table (list): Data table to work on. First columns containing the keys.

    Returns:
        string: Random and unique string
    """
    test_random = "eH34Ju#&"

    var = 1
    while var == 1:
        for line in table:
            if test_random == line[0]:
                test_random = generate_id()
            else:
                var = 0

    return test_random

def remove(table, id):
    for i in range(len(table)):
        if id == str(table[i][0]):
            table.remove(table[i])

    return table

def path(user = "stefan"):
    if user == "stefan":
        return "/home/stefan/Codecool/Python/5th_TW_week/ERP Stage1/"
    elif user == "alex":
        return "/Users/alexandruoriean/codecool/5_tw_week/erp/"
    elif user == "adi":
        return "/home/pogar/codecool/lightweight-erp-python-phoenix/lightweight-erp-python-phoenix/"
    elif user == "katy":
        return "/home/katy/Desktop/python projects/erpGit/lightweight-erp-python-phoenix/"
    elif user == "bogdan":
        bogdan_path = "C:/Users/Acasa/Desktop/git/lightweight-erp-python-phoenix/"
        return bogdan_path.replace("/", "\\")
    else:
        raise KeyError("There is no such option.")


def validate_years(year):
    if type(year) == str and year.upper()=="EXIT":
        raise ValueError
    else:
        valid_years = [str(x) for x in range(1700, 2020)]
        return year in valid_years
