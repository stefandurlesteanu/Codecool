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


def album_by_given_artist(list, artist_name):
    found_result = []
    for i in list:
        if artist_name == i[ARTIST]:
            found_result.append(i)
    return found_result


all_list = open_file('/home/pogar/cc_game_inventory/text_albums_data.txt')
artist_name = str(input("Give the artist name:"))
print(album_by_given_artist(all_list, artist_name))
