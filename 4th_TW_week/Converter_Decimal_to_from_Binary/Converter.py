
def convert_numbers(num_to_be_converted):

    try:

        new_list = []
        decimal = 0
        complementary_1_list = []
        if base == 10:
            if num_to_be_converted > 0:
                while num_to_be_converted != 0:
                    new_list.append(str(num_to_be_converted % 2))
                    num_to_be_converted = num_to_be_converted // 2
                x = ''.join(new_list[::-1])

                return "0" + x

            elif num_to_be_converted == 0:

                return 0
            
            else:
                num_to_be_converted = abs(num_to_be_converted)
                while num_to_be_converted != 0:
                    new_list.append(str(num_to_be_converted % 2))
                    num_to_be_converted = num_to_be_converted // 2
                x = new_list[::-1]
                for i in x:
                    if int(i) == 1:
                        i = 0
                        complementary_1_list.append(i)
                    else:
                        i = 1
                        complementary_1_list.append(i)
                z = 1
                while z == 1:
                    for i in range(len(complementary_1_list)-1,-1,-1):
                        if complementary_1_list [i] + z == 1:
                            complementary_1_list [i] = 1
                            z = 0
                            break
                        elif complementary_1_list [i] + z == 2:
                            complementary_1_list [i] = 0
                        else:
                            complementary_1_list [i] = 1
                            z = 0
                int_list_to_str_list = [str(i) for i in complementary_1_list]
                return ''.join(int_list_to_str_list)
            


        elif base == 2:
            
            l = len(str(num_to_be_converted)) - 1
            
            for index in str(num_to_be_converted):
                index = int(index) * pow(2,l)
                decimal += index
                l -= 1
            return decimal

        else: raise IndexError

    except (IndexError, ValueError):
        print("Please insert values as in example!")
