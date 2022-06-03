# https://www.udemy.com/course/learn-recursion/learn/lecture/23999446#overview

def getSubsequences(str):
    subsequences = []

    def rec(str, i, subsequence):
        if i == len(str):
            subsequences.append(subsequence)
        else:
            # take ith element
            rec(str, i+1, subsequence + str[i])
            # dont take
            rec(str, i+1, subsequence)
    rec(str, 0, "")
    return subsequences


print(getSubsequences('bra'))
