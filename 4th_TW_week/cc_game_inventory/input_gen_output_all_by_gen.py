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


def genre_input_result_all_by_genre(list, genre_input):
    found_result = []
    for i in list:
        if genre_input == i[GENRE]:
            found_result.append(i)
    return found_result


all_list = open_file('/home/pogar/cc_game_inventory/text_albums_data.txt')
genre_input = str(input("Give the genre:"))
print(genre_input_result_all_by_genre(all_list, genre_input))
