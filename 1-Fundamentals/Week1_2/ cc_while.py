
x = 0
while x != 10:
    x = x + 1
    if x != 6 and x > 4:
        if x >= 5 and x < 9:
            print(
                "x is bigger then or equal to 5, and less then or equal to 8, but not 6. It is:", x)

        elif x > 7:
            print("x is bigger than 8. It is:", x)
    else:
        print(x)
