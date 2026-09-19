#top-down approach
def fib(n,memo={}):#6,m-5,4
    if n<=1:
        return n
    if n in memo:
        return memo[n]

    memo[n] = fib(n-1, memo)+fib(n-2,memo)#{6:

    return memo[n]

print(fib(6))

#tabulation bottom-up approach
def fib(n):
    if n<=1:
        return n
    dp=[0]*(n+1)
    dp[0]=0
    dp[1]=1
    for i in range(2,n+1):
        dp[i]=dp[i-1]+dp[i-2]
    return dp[n]
print(fib(6))

##climbing stairs-------
'''
n steps = 100
at a time u can climb 1 or 2 steps

1s- 1w
2s - 1+1,2- 2w
3s - 1+1+1, 2+1, 1+2 - 3w
4s - 1+1+1+1, 1+2+1, 1+1+2, 2+2, 2+1+1 - 5w
5s - 1+1+1+1+1, 1+1+1+2, 1+1+2+1, 1+2+1+1,2+1+1+1, 2+2+1, 1+2+2, 2+1+2 - 8w'''

def climbing_stairs(n):
    if n<=1:
        return 1
    dp=[0]*(n+1)
    dp[0]=1
    dp[1]=1
    for i in range(2,n+1):
        dp[i]=dp[i-1]+dp[i-2]
    return dp[n]
print(climbing_stairs(5))

