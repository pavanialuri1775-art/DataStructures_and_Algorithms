#
#knapsack----------

def kn(wt,vl,ca):#[2,3,4],[12,20,30],5

    n = len(wt)#3

    dp = [[0]*(ca+1) for i in range(n+1)]#mat

    for i in range(1,n+1):#i=1,2,3

        for w in range(1,ca+1):#w=1..4,5

            if wt[i-1]<=w:# 4<=5

                take = vl[i-1]+dp[i-1][w-wt[i-1]] # vl[2]+dp[2][5-4]=30+0=30

                skip = dp[i-1][w] #dp[2][5]=32

                dp[i][w] = max(take, skip)#max(30,32)

            else:

                dp[i][w] = dp[i-1][w] #
    print(n,ca)

    return dp[n][ca]

wts = [2,3,4]
vls = [12,20,10]

ca = 7

print(kn(wts, vls, ca))