print("This is age detector.In year you want")

print("Tell me your age or year of birth")
inpu = int(input("enter here:"))

if inpu < 120:
    print("this your age")
    print("your year of birth is", 2021 - inpu)
    print("you will turn hundred in year", 2021 - inpu + 100)

    m = 2021 - inpu

    print("now tell me in which year do you want to check your age")

    year = int(input("enter here:"))
    print("your age will be", year - m)
elif inpu < 1900:
    print("this your age")
    print("it seems that you are not human")
    m = 0
elif inpu < 2021:
    print("this your year of birth")
    print("your age is ", 2021 - inpu)
    print("you will turn  in ", inpu + 100)

    m = inpu
    print("now tell me in which year do you want to check your age")

    year = int(input("enter here:"))
    print("your age will be", year - m)
elif inpu > 2021:
    print("this is your year of birth")
    print("are you  time traveller ?")
    m = 0
