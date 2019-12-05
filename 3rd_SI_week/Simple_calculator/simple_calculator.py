import operator

allowed_operators = {"+": operator.add, "-": operator.sub, "*": operator.mul, "/": operator.truediv}

while True:
    try:

        num1 = input("Enter a number (or a letter to exit): ")
        if num1.isalnum() == False:
            raise ValueError
        elif num1.isalpha() == True:
            break
        else:
            input_operator = input("Enter an operator: ")
            num2 = input(str("Enter another number: "))
            operator = allowed_operators[input_operator]

        def calculator (num1, num2, operator):
            return operator(int(num1),int(num2))

        print ("Result: ", calculator(num1,num2,operator))
    
    except ValueError:
        print("Please insert a valid integer!")
    except KeyError:
        print("Please insert a valid operator!")