# Parameters:
#  s: str
# return type: str

from distutils.errors import CCompilerError


def reverseStrMy(s, i, cc):
    if i == len(s)+1:
        return cc
    nthChar = s[-i]
    return reverseStrMy(s, i+1,  cc + nthChar)

# solution 1:
def reverse1(str):
	if str == '':
		return ''
	else:
		return reverse1(str[1:]) + str[0]

# solution 2:
def reverse2(str):
  if len(str) <= 1:
    return str
  else:
    mid = len(str)//2
    leftPart = str[0:mid]
    rightPart = str[mid:] 
    return reverse2(rightPart)+reverse2(leftPart)

# solution 3:
def rec(str, rev, i=0):
  if i == len(str):
    return
  else:
    rec(str, rev, i+1)
    rev.append(str[i])

def reverse3(str):
  rev = []
  rec(str, rev)
  return ''.join(rev)


print(reverseStrMy("burhan", 1, ""))
print(reverse1("burhan"))
print(reverse2("burhan"))
print(reverse3("burhan"))