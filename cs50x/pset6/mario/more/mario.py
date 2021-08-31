from cs50 import get_int

height = 0

while (height > 8 or height < 1):
    height = get_int("Height: ")

for i in range(1, int(height) + 1):
    print(" " * (int(height) - int(i)), end="")
    print("#" * i, end="")
    print("  ", end="")
    print("#" * i, end="")
    print("")