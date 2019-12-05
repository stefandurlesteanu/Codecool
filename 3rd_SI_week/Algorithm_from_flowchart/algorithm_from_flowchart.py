def list_to_be_sorted():
    list_of_nums = (input("Please insert numbers separated by space: ")).split()
    list_of_nums = list(map(int, list_of_nums))
    return list_of_nums


def sorting(numbers):
    iterations = 1
    N = len(numbers)
    while iterations < N:
        j = 0
        while j <= N-2:
            if numbers[j] > numbers[j+1]:
                temp = numbers[j+1]
                numbers[j+1] = numbers[j]
                numbers[j] = temp
                j += 1
            else:
                j += 1
        iterations += 1
    return numbers


def printing_result(sorted_list):
    print ('Your sorted list is: {}'.format(sorted_list))


def main():
    first_list = list_to_be_sorted()
    sorted_list = sorting(first_list)
    return printing_result(sorted_list)

if __name__ == "__main__":
    main()