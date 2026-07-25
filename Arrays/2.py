#seives prime number
def sieve(n): #10
    prime = [True]*(n+1) #[t,t,t,t,t,t,t,t,t,t,t]
    prime[0]=prime[1]=False #[f, f , t t f t f t f f f]
    p=2
    while p*p <=n: #4
        if prime[p]:
            for i in range(p*p, n+1, p):
                prime[i]=False
        p+=1 #4
    res = []
    for i in range(2, n+1):
        if prime[i]:
            res.append(i)
    return res
n= int(input())#10
print(sieve(n))
                