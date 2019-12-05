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


def album_by_album(list, input):
    a = []
    for i in list:
        if input == i[ALBUM]:
            a.append(i)
    return a


all_list = open_file('/home/pogar/cc_game_inventory/text_albums_data.txt')
ablum_input = str(input("Give the album name:"))
print(album_by_album(all_list, ablum_input))
