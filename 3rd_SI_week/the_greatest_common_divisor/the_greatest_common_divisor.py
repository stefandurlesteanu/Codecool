def input_nums():
    first_num = int(input("Please insert first number: "))
    second_num = int(input("Please insert second number: "))
    return first_num, second_num


def gretear_common_divisor():
    nums = sorted(input_nums(),reverse=True)
    while nums[-2] % nums[-1] != 0:
        new_num = nums[-2] % nums[-1]
        nums.append(new_num)
    return nums[-1]

print(gretear_common_divisor())
