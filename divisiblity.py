def fizzbuzz(a):
    if a%3==0 and a%5==0 :
        print("fizz buzz")
    elif a%3==0 :
        print("fizz")
    elif a%5==0 :
        print("buzz")
    else:
        print("none")
         
         
fizzbuzz(float(input("enter number:")))