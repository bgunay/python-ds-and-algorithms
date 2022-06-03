# https://www.udemy.com/course/learn-recursion/learn/lecture/23949960#overview


# method 1:
def rec(arr, i, phrase, output):
  if i == len(arr):
    output.append(' '.join(phrase))
  else:
    for word in arr[i]:
      phrase.append(word)
      rec(arr, i+1, phrase, output)
      # backtrack
      phrase.pop()

def phrases1(arr):
  output = []
  rec(arr, 0, [], output)
  return output


# method 2:
def phrases2(arr, i=0):
  if i == len(arr):
    return ['']
  else:
    fromNext = phrases2(arr, i+1)
    output = []
    print("fromNext {}".format(fromNext))
    for word in arr[i]:
      for phrase in fromNext:
        output.append(word + (' ' if len(phrase) > 0 else '') + phrase)
    return output
	
arr = [['I', 'You', 'They'], ['love', 'hate'], ['food', 'games']]
print(phrases1(arr))

#print(phrases2(arr,0))
