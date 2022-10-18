try:
    a = int(input("Enter first number:\n"))
    b = int(input("Enter second number:\n"))
    maxnum = max(a, b)
    while True:
        if maxnum % a == 0 and maxnum % b == 0:
            break
        maxnum = maxnum + 1

    print(f"\nLCM OF {a} and {b} is {maxnum}.\n")

except:
    print("\nINVALID INPUT\n")
