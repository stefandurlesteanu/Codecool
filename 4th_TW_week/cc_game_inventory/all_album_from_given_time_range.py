def open_file(filename):
    new_list = []
    with open(filename) as opened:
        for i in opened:
            new_list.append(i.strip().split(","))
        return new_list


ARTIST = 0
ALBUM = 1
RELEASE_YEAR = 2
GENRE = 3
LENGTH = 4

all_list = open_file('/home/pogar/cc_game_inventory/text_albums_data.txt')


def all_album_from_given_time_range(lista, input1, input2):
    a = []
    for i in lista:
        if int(i[RELEASE_YEAR]) >= input1 and int(i[RELEASE_YEAR]) <= input2:
            a.append(i)
    return a


input1 = int(input("Give the first time range:"))
input2 = int(input("Give the second time range:"))
print(all_album_from_given_time_range(all_list, input1, input2))
