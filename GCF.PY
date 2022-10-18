while True:
    try:
        a = int(input("Enter first number:\n"))
        b = int(input("Enter second number:\n"))
        mn = min(a, b)

        for i in range(1, mn + 1):
            if a % i == 0 and b % i == 0:
                gcf = i

        print(f"\nGCF of {a} and {b} is {gcf}\n")
        break

    except:
        print("\nINVALID INPUT\n")
        continue