#93.Check whether a number is prime.
def prime(n):
    if n<2:
        print("false")
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            print("Not prime")
            break
    else:
        print("prime")
prime(5)
    

        