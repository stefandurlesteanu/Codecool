import re
import os
import copy

# Covert .txt file into a list, for futher operations
def open_albums (filename):

    new_list = []
    with open(filename) as opened:
        for i in opened:
            new_list.append(i.strip().split(","))
    return new_list


#BACK_UP_COPY = tuple (open_file) 
#BACK_UP_COPY =  open_albums ("/home/stefan/Python/Codecool/4th_TW_week/cc_game_inventory/text_albums_data.txt")

# add a new album





def add_new_album (filename):
    artist_name = str(input("Artist name: "))
    album_name = str(input("Album name: "))
    while True :
        try:
            album_year = str(input("Album release year: "))
            assert 0 < int(album_year) < 2050
            break
        except (AssertionError, ValueError):
            print("Use a valid year!")
    album_genre = str(input("Album genre: "))
    regex = '[0-9]+\:[0-5][0-9]{1,1}$'        
    while True:
        album_length = str(input ("Album length (minutes:seconds): "))
        if (re.search(regex, album_length)):
            break
        else:
            print ("Please use this format --> mm:ss")
    with open (filename, "a") as appending:
        appending.write (f"\n{artist_name},{album_name},{album_year},{album_genre},{album_length}")


#add_new_album("/home/stefan/Python/Codecool/4th_TW_week/cc_game_inventory/text_albums_data.txt")

#print(open_file ("/home/stefan/Python/Codecool/4th_TW_week/cc_game_inventory/text_albums_data.txt"))




def print_open_album (open_albums):
    output = []
    for index, line in enumerate (open_albums, 1):
        output.append("{}.{}".format(index, ', '.join(line)))
    return '\n'.join(output)
   



# edit already existing albums

def album_index (filename):

    new_list = open_albums(filename)

    print(print_open_album(new_list), '\nFor EXIT press 0')

    # ask album to be edited
    while True:
        try:
            ablum_index = int(input("\nPlease type the idex of the album you would like to edit: "))
            assert 0 <= ablum_index < len (new_list)
            break 
        except (AssertionError, ValueError):
            os.system('clear')
            print(print_open_album(new_list))
            print("Please choose a valid index: 1 - {}".format(len(new_list)))
    return ablum_index

def edit_album (filename):
    global BACK_UP_COPY
    index = album_index(filename)
    new_list = open_albums (filename)
    
    os.system('clear')
    allowed_changes = {"ARTIST": 0, "ALBUM": 1, "YEAR": 2, "GENRE": 3, "DURATION": 4}

    #Output
    x = ' | '.join(new_list[index-1])
    print(" | ".join([x for x in allowed_changes.keys()]) + "\n" + "=" * len(x) + "\n" + x + "\n" + "=" * len(x))


    # intermediary list is created, to be used in "save or not function"
    intermediary_list = copy.deepcopy(new_list)

    change_more = "Y"
    while change_more == "Y":
        while True:
            try:
                # ask for album atribute to be edited
                atribute = allowed_changes[(input("What would you like to change?: ").upper())]
                new_value = input("What you want instead of \"{}\"?: ".format(new_list[index-1][atribute]))   
                intermediary_list[index-1][atribute] = new_value
                
                break
            except KeyError:
                choice_list = ", ".join([x for x in allowed_changes.keys()])
                print (f"Please choose from: {choice_list}")
        change_more = str(input("Change more? (Y/n): "))

    os.system('clear')


    # modify atribute only in intermediary list

    y = "|".join(intermediary_list[index-1])
    print(" | ".join([x for x in allowed_changes.keys()]) + "\n" + "=" * len(y) + "\n" + y + "\n" + "=" * len(y))
    #print(intermediary_list)

    #final = '\n'.join([','.join(i) for i in new_list])

    #print (final)

    # #save or no changes
    save_Y_or_n = input(str("Do you want to save this? (Y/n): "))

    if save_Y_or_n == "n":
        with open (filename, "w") as writing:
            writing.write('\n'.join([','.join(i) for i in new_list]))
    else:
        with open (filename, "w") as writing:
            writing.write('\n'.join([','.join(i) for i in intermediary_list]))
        BACK_UP_COPY = intermediary_list
        return BACK_UP_COPY
    

    

#edit_album ("/home/stefan/Python/Codecool/4th_TW_week/cc_game_inventory/text_albums_data.txt")

    # return memorise_albums


# Save or not function



def final_save(filename):
    global BACK_UP_COPY
    save_new = str(input("Save (Y/n)"))
    
    if save_new == "n":
        with open (filename, "w") as writing:
            writing.write('\n'.join([','.join(i) for i in BACK_UP_COPY]))
    

#add_new_album("/home/stefan/Python/Codecool/4th_TW_week/cc_game_inventory/text_albums_data.txt")
#final_save ("/home/stefan/Python/Codecool/4th_TW_week/cc_game_inventory/text_albums_data.txt")

