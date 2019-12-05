




def edit_albums(filename):
    import os
    import copy
    new_list = []
    with open(filename) as opened:
        for i in opened:
            new_list.append(i.strip().split(","))
    for index, line in enumerate (new_list, 1):
        print ("{}.{}".format(index, ', '.join(line)))

    ablum_index = int(input("\nPlease type the idex of the album you would like to edit: "))
    os.system('clear')
    allowed_changes = {"ARTIST": 0, "ALBUM": 1, "YEAR": 2, "GENRE": 3, "DURATION": 4}

    #Output
    x = ' | '.join(new_list[ablum_index-1])
    print(" | ".join([x for x in allowed_changes.keys()]) + "\n" + "=" * len(x) + "\n" + x + "\n" + "=" * len(x))

    allowed_changes = {"ARTIST": 0, "ALBUM": 1, "YEAR": 2, "GENRE": 3, "DURATION": 4}
    atribute = allowed_changes[(input("What would you like to change?: ").upper())]

        
    new_value = input("What you want instead of \"{}\"?: ".format(new_list[ablum_index-1][atribute]))   

    os.system('clear')
    intermediary_list = copy.deepcopy(new_list)

    intermediary_list[ablum_index-1][atribute] = new_value
    y = "|".join(intermediary_list[ablum_index-1])
    print(" | ".join([x for x in allowed_changes.keys()]) + "\n" + "=" * len(y) + "\n" + y + "\n" + "=" * len(y))
    print(intermediary_list)
    print (new_list)
    return intermediary_list[ablum_index-1][atribute]

    # return memorise_albums



print(edit_albums("/home/stefan/Python/Codecool/4th_TW_week/cc_game_inventory/text_albums_data.txt"))