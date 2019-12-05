import music_reports
import os
import sys
import file_operations as fo
import copy

ARTIST = 0
ALBUM = 1
RELEASE_YEAR = 2
GENRE = 3
DURATION = 4
header = ("ARTIST", "ALBUM", "RELEASE YEAR", "GENRE", "DURATION")
separator = " | "
char1 = "="
char2 = "–"
path = "Codecool/4th_TW_week/cc_game_inventory/text_albums_data.txt"
BACK_UP_COPY = fo.open_albums("Codecool/4th_TW_week/cc_game_inventory/text_albums_data.txt")


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


def find_longest_item(index, value_list=music_list):
    length = len(header[index])
    for line in value_list:
        if len(str(line[index])) >= length:
            length = len(str(line[index]))
    return length


lengths = [find_longest_item(i) for i in range(len(header))]
row_length = sum(lengths) + len(separator) * (len(lengths) - 1)


def horizontal_line(char=char1):
    print(char * row_length)


def app_header(char=char1):
    # os.system("clear")
    horizontal_line(char)
    print("music library".upper().center(row_length))
    horizontal_line(char)


def menu_header(sep=separator, char=char2):
    app_header(char1)
    print(
        header[ARTIST].capitalize().rjust(lengths[ARTIST])
        + sep
        + header[ALBUM].capitalize().rjust(lengths[ALBUM])
        + sep
        + header[RELEASE_YEAR].capitalize().rjust(lengths[RELEASE_YEAR])
        + sep
        + header[GENRE].capitalize().rjust(lengths[GENRE])
        + sep
        + header[DURATION].capitalize().rjust(lengths[DURATION])
    )
    horizontal_line(char)


def view_music(value_list=music_list, sep=" | ", char="="):
    os.system("clear")
    # menu header
    menu_header()

    # content
    for line in value_list:
        print(
            line[ARTIST].rjust(lengths[ARTIST])
            + sep
            + line[ALBUM].rjust(lengths[ALBUM])
            + sep
            + str(line[RELEASE_YEAR]).rjust(lengths[RELEASE_YEAR])
            + sep
            + line[GENRE].rjust(lengths[GENRE])
            + sep
            + line[DURATION].rjust(lengths[DURATION])
        )

    # footer
    horizontal_line(char)


def first_page_menu():
    app_header()
    print("MENU".center(row_length))
    horizontal_line(char2)
    print("1.  View all imported albums")
    print("2.  Find all albums by genre")
    print("3.  Find all albums from given time range")
    print("4.  Find shortest and longest albums")
    print("5.  Find all albums created by given artist")
    print("6.  Find album by album name")
    print("7.  Full report")
    print("8.  Find all similar music genres albums when searching from particular album")
    print("9.  Add new alum")
    print("10. Edit albums")
    print("11. Exit")
    horizontal_line()


# view_music(music_reports.import_music(filename=path))


def main():
    os.system('clear')
    option = 0
    

    while option == 0:
        os.system('clear')
        first_page_menu()
        option = int(input("Enter the command: "))
        while option == 1:

            os.system('clear')
            view_music(import_music(filename=path))
            option = int(input("For exit, press 0: "))
        while option == 2:
            os.system('clear')
            genre_input = input("Enter the genre: ")
            all_by_genre = music_reports.genre_input_result_all_by_genre(
                music_list, genre_input)

            view_music(all_by_genre, sep=" | ", char="=")
            option = int(input("For exit, press 0: "))
        while option == 3:
            input1 = int(input("Give the start year: "))
            input2 = int(input("Give the end year: "))
            time_range = music_reports.all_album_from_given_time_range(
                music_list, input1, input2)
            view_music(time_range, sep=" | ", char="=")
            option = int(input("For exit, press 0: "))
        while option == 5:
            artist_name = str(input("Give the artist name: "))
            artista = music_reports.album_by_given_artist(
                music_list, artist_name)
            view_music(artista, sep=" | ", char="=")
            option = int(input("For exit, press 0: "))
        while option == 6:
            album = str(input("Give the album name: "))
            album_by_album = music_reports.album_by_album(music_list, album)
            view_music(album_by_album, sep=" | ", char="=")
            option = int(input("For exit, press 0: "))
        # while option == 8:
        #     album = str(input("Give the album name: "))
        #     album_by_genre = music_reports.album_genere(music_list, album)
        #     view_music(album_by_genre, sep=" | ", char="=")
        #     option = int(input("For exit, press 0: "))
        while option == 9:
            fo.add_new_album(
                "/home/stefan/Python/Codecool/4th_TW_week/cc_game_inventory/text_albums_data.txt")
            print("Album added to the library!")
            option = int(input("For exit, press 0 or 9 to add a new album: "))

        if option == 10:

            os.system('clear')

            fo.print_open_album(
                "Codecool/4th_TW_week/cc_game_inventory/text_albums_data.txt")
            # fo.album_index(
            #     "Codecool/4th_TW_week/cc_game_inventory/text_albums_data.txt")
            fo.edit_album("Codecool/4th_TW_week/cc_game_inventory/text_albums_data.txt")
            option = int(input("For exit, press 0 or 10 to edit antoher album: "))


        


main()

print (BACK_UP_COPY)