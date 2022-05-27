
def waysToClimb(n, possibleSteps):
    print("n is {}".format(n)  if n<2 else "" )
    if n == 0:
        return 1
    if n == 1:
        return 0
    else:
        nbWays = 0
        for steps in possibleSteps:
            if (n-steps) >= 0:
                nbWays += waysToClimb(n-steps, possibleSteps)
        return nbWays


print(waysToClimb(10, [2, 4, 5, 8]))
