def waysToClimb(n, possibleSteps, lookup):
  key = str(n)
  if key in lookup:
	return lookup[key]
  elif n == 0:
    lookup[key] = 1
    return lookup[key]
  else:
    nbWays = 0
    for steps in possibleSteps:
      if (n-steps) >= 0:
        nbWays += waysToClimb(n-steps, possibleSteps)
	lookup[key] = nbWays
    return lookup[key]