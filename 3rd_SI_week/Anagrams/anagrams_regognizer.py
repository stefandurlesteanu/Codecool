def read_csv_file (path):
    with open(path, "r") as file:
        return [i.replace("\n", "") for i in file.readlines()]


def anagrams(file):
    final_list = []
    start_list = file
    while len(start_list)>0:
        new_list = []
        for i in start_list:
            if sorted(i) == sorted(start_list[0]):
                new_list.append(i)
        start_list.pop(0)
        final_list.append(new_list)
        for i in new_list:
            if i in start_list:
                start_list.remove(i)
    return final_list


def print_anagrams(list):
    for i in list:
        print ('Anagrams for {} are: {}'.format(i[0],', '.join(i[1:])))


def main():
    file = read_csv_file('/home/stefan/Codecool/Python/3rd_SI_week/Anagrams/anagrams.csv')
    list = anagrams(file)
    print_anagrams(list)

if __name__ == "__main__":
    main()
