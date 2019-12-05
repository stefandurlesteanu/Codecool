import sys
import os

ARTIST = 0
ALBUM = 1
RELEASE_YEAR = 2
GENRE = 3
DURATION = 4
header = ("ARTIST", "ALBUM", "RELEASE YEAR", "GENRE", "DURATION")
separator = " | "
char1 = "="
char2 = "–"
path = "text_albums_data.txt"


def import_music(filename=path):
    try:
        with open(filename, "r") as raw_data:
            music_list = []
            for line in raw_data:
                music_list.append(line)
            music_list = [line.strip().split(",") for line in music_list]
            for album in music_list:
                album[RELEASE_YEAR] = int(album[RELEASE_YEAR])
            return music_list
    except FileNotFoundError:
        return "File not found!"


music_list = import_music()


# convert the duration from "mm:ss" to seconds
def get_duration(album):
    (mm, ss) = album[DURATION].split(":")
    return int(mm) * 60 + int(ss)


# find the longest item in list for printing column width


def find_shortest_longest(music=music_list):
    lst = sorted(music, key=lambda x: get_duration(x))
    app_header()  # header
    print("1. for shortest\n2. for longest" "")  # content
    horizontal_line()
    option = input("Please enter your option: ")  # user input
    while option not in ["1", "2"]:
        option = input("Please enter 1 or 2: ")
    if option == "1":
        return [lst[0]]
    else:
        return [lst[-1]]


def find_shortest(music=music_list):
    lst = sorted(music, key=lambda x: get_duration(x))
    return [lst[0]]


def find_longest(music=music_list):
    lst = sorted(music, key=lambda x: get_duration(x))
    return [lst[-1]]


def find_newest(value_list=music_list):
    oldestValue = [value_list[0]]
    for i in value_list:
        if i[RELEASE_YEAR] > oldestValue[0][RELEASE_YEAR]:
            oldestValue = []
            oldestValue.append(i)
        if (
            i[RELEASE_YEAR] == oldestValue[0][RELEASE_YEAR]
            and i[ALBUM] != oldestValue[0][ALBUM]
        ):
            oldestValue.append(i)
    return oldestValue


def find_oldest(value_list=music_list):
    newestValue = [value_list[0]]
    for i in value_list:
        if i[RELEASE_YEAR] < newestValue[0][RELEASE_YEAR]:
            newestValue = []
            newestValue.append(i)
        if (
            i[RELEASE_YEAR] == newestValue[0][RELEASE_YEAR]
            and i[ALBUM] != newestValue[0][ALBUM]
        ):
            newestValue.append(i)
    return newestValue


def count_albums_by_artist(value_list=music_list):
    unique_artists = set()
    for album in value_list:
        unique_artists.add(album[ARTIST])
    result = []
    for artist in unique_artists:
        counter = 0
        for album in value_list:
            if artist == album[ARTIST]:
                counter += 1
        result.append([artist, counter])
    return result


def count_albums_by_genre(value_list=music_list):
    unique_genre = set()
    for album in value_list:
        unique_genre.add(album[GENRE])
    result = []
    for genre in unique_genre:
        counter = 0
        for album in value_list:
            if genre == album[GENRE]:
                counter += 1
        result.append([genre, counter])
    return result


def all_album_from_given_time_range(lista, input1, input2):
    a = []
    for i in lista:
        if int(i[RELEASE_YEAR]) >= input1 and int(i[RELEASE_YEAR]) <= input2:
            a.append(i)
    return a


def genre_input_result_all_by_genre(list, genre_input):
    found_result = []
    for i in list:
        if genre_input.lower() == i[GENRE].lower():
            found_result.append(i)
    return found_result


def album_by_given_artist(list, artist_name):

    found_result = []
    for i in list:
        if artist_name.lower() == i[ARTIST].lower():
            found_result.append(i)
    return found_result


def album_by_album(list, input):
    a = []
    for i in list:
        if input.lower() == i[ALBUM].lower():
            a.append(i)
    return a


def give_album(list):
    album = ''
    for i in list:
        if album_name.lower() == i[ALBUM].lower():
            album += str(i[ALBUM])
    return album



# album by gem
def give_album(list):
    album = ''
    for i in list:
        if album_name.lower() == i[ALBUM].lower():
            album += str(i[ALBUM])
    return album


def album_genere(list, album):
    genre_album = ''
    for i in list:
        if i[ALBUM].lower() == album.lower():
            genre_album += str(i[GENRE])
            return genre_album


def similar_album(gen, list=music_list):
    similar_album_by_genre = []
    for i in list:
        if i[GENRE].lower() == gen.lower():
            similar_album_by_genre.append(i)
    return similar_album_by_genre

def similar_album(gen, list=music_list):

    similar_album_by_genre = []
    for i in list:
        if i[GENRE].lower() == gen.lower():
            similar_album_by_genre.append(i)
    return similar_album_by_genre
