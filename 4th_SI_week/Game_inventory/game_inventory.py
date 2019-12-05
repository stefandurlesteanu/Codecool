inv = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}
dragon_loot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']


def display_inventory(inventory):
    for i in inventory:
        print(i.rjust(11), '|', (str(inventory[i])).rjust(3))


def add_to_inventory(inventory, added_items):
    for i in added_items:
        if i in inventory:
            inventory[i] += 1
        else:
            inventory[i] = 1
    return inventory

def print_table(inventory, order):
    max_len = 17
    if order == 'count, desc':
        list_of = sorted(inv.items(), key=lambda x: x[1], reverse=True)
    elif order == 'count, asc':
        list_of = sorted(inv.items(), key=lambda x: x[1])
    else:
        list_of = list(inv.items())
    list_of = [('item name', 'count')] + list_of
    for i in list_of:
        if len(i[0])+len(str(i[1])) > max_len:
            max_len = len(i[0])+len(str(i[1]))

    print(('-' * max_len).rjust(20), '\n', 'item name'.rjust(11), '|', 'count'.rjust(5), '\n',('-' * max_len).rjust(19))



add_to_inventory(inv, dragon_loot)

print_table(inv, input("Please choose one --> \"count, desc\", \"count, asc\" or leave empty: "))
display_inventory(inv)
