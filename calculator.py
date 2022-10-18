import replit
while True:
    num1=float(input("enter a first number:"))
    op=input("enter a operator:")
    num2=float(input("enter a second number:"))


    if op=="+":  
        print(num1+num2)
    elif op=="-":
        print(num1-num2)
    elif op=="*":
        print(num1*num2)
    elif op=="/":
        print(num1/num2)
    else :
        print("invalid operator")
    
    a = input("\nEnter c to continue:")
    if(a.lower()=="c"):
        replit.clear()
        continue
    else:
        quit()
