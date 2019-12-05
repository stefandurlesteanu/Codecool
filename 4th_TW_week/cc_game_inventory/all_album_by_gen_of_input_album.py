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


def give_album(list):
    album = ''
    for i in list:
        if album_name == i[ALBUM]:
            album += str(i[ALBUM])
    return album


def album_genere(list, album):
    genre_album = ''
    for i in list:
        if i[ALBUM] == album:
            genre_album += str(i[GENRE])
            return genre_album


def similar_album(list, gen):
    similar_album_by_genre = []
    for i in list:
        if i[GENRE] == gen:
            similar_album_by_genre.append(i)
    return similar_album_by_genre


all_list = open_file('/home/pogar/cc_game_inventory/text_albums_data.txt')
album_name = str(input("Give the album name:"))
x = give_album(all_list)
y = album_genere(all_list, x)
print(album_genere(all_list, x))
print(similar_album(all_list, y))
