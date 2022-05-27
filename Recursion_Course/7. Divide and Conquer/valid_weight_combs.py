# 1st method:
def rec(weights, maxWeight, i, combs, comb):
    if maxWeight < 0:
        return
    elif i == len(weights):
        combs.append(comb.copy())
    else:
        comb.append(i)
        rec(weights, i+1, maxWeight-weights[i], combs, comb)
        comb.pop()
        rec(weights, i+1, maxWeight, combs, comb)

def getCombsRec(weights, maxWeight):
    combs = []
    rec(weights, maxWeight, 0, combs, [])
    return combs
	
# 2nd method:
def getCombs(weights, maxWeight, i=0):
  if i == len(weights):
    return [[]]
  else:
    fromNext = getCombs(weights, maxWeight, i+1)
    combs = []
    for comb in fromNext:
      combs.append(comb.copy())
      if (sum([weights[item] for item in comb])+weights[i]) <= maxWeight:
        comb.append(i)
        combs.append(comb.copy())
    return combs


print(getCombs([4,7,2,1],7,0)) 
print(getCombsRec([4,7,2,1],7))

