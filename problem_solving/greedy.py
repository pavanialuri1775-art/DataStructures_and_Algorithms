# greedy search:we choose the option  that looks best at the  current moment.
def coin_cnt(amount,coins):
    res=[]
    for coin in coins:
        while  amount>=coin:
            amount=amount-coin
            res.append(coin)
    return res
coins=list(map(int,input().split()))
amt=int(input())
print(coin_cnt(amt,coins))


def fib(n,memo={}):#6,m-5,4
    if n<=1:
        return n
    if n in memo:
        return memo[n]

    memo[n] = fib(n-1, memo)+fib(n-2,memo)#{6:

    return memo(n)

print(fib(6))