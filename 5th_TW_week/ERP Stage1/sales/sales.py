""" Sales module

Data table structure:
    * id (string): Unique and random generated identifier
        at least 2 special characters (except: ';'), 2 number, 2 lower and 2 upper case letters)
    * title (string): Title of the game sold
    * price (number): The actual sale price in USD
    * month (number): Month of the sale
    * day (number): Day of the sale
    * year (number): Year of the sale
"""
import ui
import data_manager
import common

list_labels = ["id", "title", "price", "month", "day", "year"]
read_file = common.path() + "sales/sales.csv"
table = data_manager.get_table_from_file(read_file)
year_range_input_options = ["Month from", "Day from", "Year from", "Month to", "Day to", "Year to"]
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
    options = ["Show Table",
               "Add Item",
               "Remove Item",
               "Update Item",
               "Get lowest price item id",
               "Get items sold between"]

    ui.print_menu("Sales menu", options, "Back to main menu")


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
        ui.print_result(get_lowest_price_item_id(
            table), "Lowest price item id")
        return False
    elif inventory_option == "6":
        inputs = ui.get_inputs([x + ": " for x in year_range_input_options], "Please enter the date rage:")
        month_from, day_from, year_from, month_to, day_to, year_to = [int(x) for x in inputs]
        ui.print_result(get_items_sold_between(table, month_from, day_from, year_from, month_to, day_to, year_to), " Item list ")
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
    title_input = "Please insert new game: "
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


def get_lowest_price_item_id(table):
    """
    Question: What is the id of the item that was sold for the lowest price?
    if there are more than one item at the lowest price, return the last item by alphabetical order of the title

    Args:
        table (list): data table to work on

    Returns:
         string: id
    """
    price_list = []
    result = ""
    for item in table:
        price_list.append(int(item[2]))
    max_price = 500
    for price in price_list:
        if price < max_price:
            max_price = price
    lowest_price = str(max_price)
    for item in table:
        if item[2] == lowest_price:
            result = item[0]

    return result


def get_items_sold_between(table, month_from, day_from, year_from, month_to, day_to, year_to):
    """
    Question: Which items are sold between two given dates? (from_date < sale_date < to_date)

    Args:
        table (list): data table to work on
        month_from (int)
        day_from (int)
        year_from (int)
        month_to (int)
        day_to (int)
        year_to (int)

    Returns:
        list: list of lists (the filtered table)
    """
    data_in_year_range = []
    data_in_month_range = []
    result = []
    for row in table:
        if year_from <= int(row[-1]) <= year_to:
            data_in_year_range.append(row)
    for row in data_in_year_range:
        if month_from <= int(row[-3]) <= month_to:
            data_in_month_range.append(row)
    for row in data_in_month_range:
        if day_from <= int(row[-2]) <= day_to:
            result.append(row)
    return result


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
