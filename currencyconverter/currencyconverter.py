with open(r'D:\CODING\Python Projects\Basic Projects\currencyconverter\currency.txt',mode='r') as f:
    result=f.readlines()


currencyvalue={}
for line in result:
    parsed=line.split("\t")
    currencyvalue[parsed[0]]=parsed[1]
    #print(currencyvalue)

while True:
    try:
        print("\nEnter amount you want to  convert in INR:")
        amount=int(input())
        print("Enter currency you want to convert in from following option:")
        [print(item)for item in currencyvalue.keys()]
        currency=input("\nEnter currency here:")
        print(f"{amount} INR = {amount*float(currencyvalue[currency])}{currency}")
    except :
        print("\nINVALID INPUT\n")

    try:
        after = input("Enter 'q' to quit and 'c' to continue: ")
        if after == 'q':
            print("\nTHANKS FOR USING OUR APP")
            exit()
        else:
            continue
    except:
        print("\nINVALID INPUT\n")