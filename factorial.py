def factorial(x):
    num=1
    for i in range(1,x+1):
        num=i*num
    return num

def rfactorial(num):
    if num==0 or num==1:
        return 1
    else:
        while num>1:
            return num*rfactorial(num-1)

while True:
    x=int(input("Enter a number here:"))
    result=factorial(x)
    print(result)

    rresult=rfactorial(x)
    print(rresult)