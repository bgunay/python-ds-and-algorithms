def rec(a, b):
  if a <= 0 or b <= 0:
    return 1
  elif a == b:
    return rec(a-1, b-1) + rec(a-2, b-2)
  else:
    return rec(a-1, b) + rec(a, b-1)