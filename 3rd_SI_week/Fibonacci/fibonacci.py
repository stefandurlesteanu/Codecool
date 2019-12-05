
fibonacci_numbers = []
n = 0
lenght_of_sequence = int(input("How long the Fibonacci sequence should be?: "))


if lenght_of_sequence <= 0:
    print("Please enter a number > o!")
elif lenght_of_sequence == 1:
    fibonacci_numbers.append(0)

elif lenght_of_sequence == 2:
    fibonacci_numbers.extend([0,1])

else:
    fibonacci_numbers.extend([0,1])
    while n < (lenght_of_sequence - 2):
        next_num = fibonacci_numbers[n]+fibonacci_numbers[n+1]
        fibonacci_numbers.append(next_num)
        n += 1

print(fibonacci_numbers)