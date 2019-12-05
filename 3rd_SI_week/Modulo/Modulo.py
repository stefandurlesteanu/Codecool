counter = 0 
for num in range(100,999):
    if num % 7 == 0 and num % 9 == 0 and counter < 25:
        print(num)
        counter += 1

     