def waysToClimb(n, possibleSteps):
  dp = [0]*(n+1)
  dp[0] = 1
  for i in range(1, len(dp)):
    nbWays = 0
    for steps in possibleSteps:
      if (i-steps) >= 0:
        nbWays += dp[i-steps]
    dp[i] = nbWays
  return dp[n]