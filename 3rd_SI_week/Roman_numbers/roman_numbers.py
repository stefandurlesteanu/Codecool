def arabic():
    return input("Please insert a number: ")


def divider(num):
    x = len(num)
    y = int('1' + '0' * (x - 1))
    return y


def roman_nums(divider):
    romans = ['I', 'X', 'C', 'M']
    choice = romans[len(divider)-1]
    return choice


def roman_multiplier(arabic, divider):
    return arabic // divider


def main():
    final = []
    arabic_num = list(arabic())
    intermediar_romans = ['D','L','V']
    while len(arabic_num) > 0:
        divider_ = divider(arabic_num)
        x = roman_multiplier(int(''.join(arabic_num)), divider_)
        y = x * roman_nums(str(divider_))
        final.append(y)
        arabic_num.pop(0)
    for i in range(len(final)):
        if len(final[i]) == 5 and 'M' not in final[i]:
            final[i] = intermediar_romans[i-1]
        elif len(final[i]) == 4 and 'M' not in final[i]:
            final[i] = final[i][0] + intermediar_romans[i-1]
    print('Equivalenst of input number in Roman symbols is: {}'.format(''.join(final)))




if __name__ == "__main__":
    main()