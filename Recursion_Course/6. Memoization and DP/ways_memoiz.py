
def waysToClimb(n, possibleSteps, dp):
    key = str(n)
    if key in dp:
        return dp[key]
    elif n == 0:
        dp[key] = 1
        return dp[key]
    else:
        nbWays = 0
        for steps in possibleSteps:
            if (n-steps) >= 0:
                nbWays += waysToClimb(n-steps, possibleSteps, dp)
                dp[key] = nbWays
        return dp[key]


dp = {'1': 0}

ways = waysToClimb(10, [2, 4, 5, 8], dp )
print(dp)
print(ways)
