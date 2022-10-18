def pallindrome_next(n):
    n = n + 1
    while not is_pallindrome(n):
        n = n + 1
    return n


def is_pallindrome(n):
    return str(n) == str(n)[::-1]


if __name__ == "__main__":
    try:
        noc = int(input("enter no of cases you want check:\n"))
        integer = []
        for i in range(noc):
            # try:
            integer.append(int(input("enter the number:\n")))

        for t in integer:
            print(f"The next pallindrome of {t} is {pallindrome_next(t)}\n")
            # except:
            # print("invalid input")

    except:
        print("pleas enter number")
