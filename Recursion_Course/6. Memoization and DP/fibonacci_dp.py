def fib(n):
    dp = [0]*(n+1)  # dp[i] represents Ui
    dp[0] = 0
    dp[1] = 1
    for i in range(2, len(dp)):
        dp[i] = dp[i-1]+dp[i-2]
    return dp[n]


print(fib(13))
