import sys

print(str(sys.argv))
print(len(sys.argv))
print(sys.argv[0])
if sys.argv[1] == '+':
    print(int(sys.argv[2]) + int(sys.argv[3]))
else:
    print("Mai incearca!")
