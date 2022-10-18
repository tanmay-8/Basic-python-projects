def oddeven(n):
    for i in range(0,n+1):
        if i%2==0:
            print(i,"is even")
        else :
            print(i,"is odd")
    


oddeven(int(input("enter a number:")))