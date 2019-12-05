all_list = [['Pink Floyd', 'The Dark Side Of The Moon', '1973', 'progressive rock', '43:00'],
            ['Britney Spears', 'Baby One More Time', '1999', 'pop', '42:20'],
            ['The Beatles', 'Revolver', '1966', 'rock', '34:43'],
            ['Deep Purple', 'Machine Head', '1972', 'hard rock', '37:25'],
            ['Old Timers', 'Old Time', '966', 'ancient', '123:45'],
            ['Pink Floyd', 'Wish You Were Here',
                '1975', 'progressive rock', '44:28'],
            ['Boston', 'Boston', '1976', 'hard rock', '37:41'],
            ['Monika Brodka', 'Granada', '2010', 'pop', '37:42'],
            ['David Bowie', 'Low', '1977', 'rock', '38:26'],
            ['rock', 'rock', '966', 'pop', '13:37'],
            ['Massive Attack', 'Blue Lines', '1991', 'hip hop', '45:02']]

ARTIST = 0
ALBUM = 1
RELEASE_YEAR = 2
GENRE = 3
LENGTH = 4


def album_by_given_artist(list, genre_input):
    found_result = []
    for i in list:
        if genre_input == i[GENRE]:
            found_result.append(i)
    return found_result


def view_all_artist(list, categori):
    a = ""
    for i in list:
        a += (i[categori] + "\n")
    return a


#genre_input = str(input("Give the genre:"))
# artist_name = str(input("Give the artist name:"))
#print(album_by_given_artist(all_list, genre_input))
# print(view_all_artist(all_list, ARTIST))
# print(view_all_artist(all_list, GENRE))
# print(view_all_artist(all_list, ALBUM))
# print(view_all_artist(all_list, RELEASE_YEAR))


# As a user I want to view all similar music genres albums
# when searching for particular album(Like in spotify, where user
# receives context suggestions regarding similar bands or tracks)


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


# album_name = str(input("Give the album name:"))
# x = give_album(all_list)
# y = album_genere(all_list, x)
# print(album_genere(all_list, x))
# print(similar_album(all_list, y))


'''As a user I want to find all albums from given time range'''


def all_album_from_given_time_range(lista, input1, input2):
    a = []
    for i in lista:
        if int(i[RELEASE_YEAR]) >= input1 and int(i[RELEASE_YEAR]) <= input2:
            a.append(i)
    return a


input1 = int(input("Give the first time range:"))
input2 = int(input("Give the second time range:"))
print(all_album_from_given_time_range(all_list, input1, input2))
