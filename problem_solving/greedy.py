#greedy search:we choose the option  that looks best at the  current moment.
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

