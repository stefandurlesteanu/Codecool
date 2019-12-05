""" Store module

Data table structure:
    * id (string): Unique and random generated identifier
        at least 2 special characters (except: ';'), 2 number, 2 lower and 2 upper case letters)
    * title (string): Title of the game
    * manufacturer (string)
    * price (number): Price in dollars
    * in_stock (number)
"""
import ui
import data_manager
import common

list_labels = ["id", "title", "manufacturer", "price", "in_stock"]
read_file = common.path() + "store/games.csv"
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
               "Count by manufacturers",
               "Average by manufacturer"]

    ui.print_menu("Store menu", options, "Back to main menu")


def choose():
    inventory_option = ui.get_inputs(["Please select option: "], "")[0]
    if inventory_option == "1":
        show_table(table)
        return False
    elif inventory_option == "2":
        add_new_table = add(table)
        show_table(add_new_table)
        save(add_new_table)
        return False
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
        ui.print_result(get_counts_by_manufacturers(table), "Games / manufacturer")
        return False
    elif inventory_option == "6":
        manufacturer = ui.get_inputs([x + ": " for x in ["Manufacturer"]], "")[0]
        ui.print_result(get_average_by_manufacturer(table, manufacturer), "Average games in stock / manufacturer")
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


def get_counts_by_manufacturers(table):
    """
    Question: How many different kinds of game are available of each manufacturer?

    Args:
        table (list): data table to work on

    Returns:
         dict: A dictionary with this structure: { [manufacturer] : [count] }
    """
    my_dict = {}
    for i in table:
        my_dict.setdefault(i[2], []).append(i[1:3])
    new_dict = {}
    for j in my_dict:
        new_dict[j] = len(my_dict[j])
    return new_dict


def get_average_by_manufacturer(table, manufacturer):
    """
    Question: What is the average amount of games in stock of a given manufacturer?

    Args:
        table (list): data table to work on
        manufacturer (str): Name of manufacturer

    Returns:
         number
    """
    while True:
        try:
            counter = 0
            stock = 0
            for item in table:
                if item[2] == manufacturer:
                    counter += 1
                    stock += int(item[-1])
            average = (int(stock/counter))
            return average
        except ZeroDivisionError:
            ui.print_error_message("Stock 0 for this manufacturer")
            break


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
