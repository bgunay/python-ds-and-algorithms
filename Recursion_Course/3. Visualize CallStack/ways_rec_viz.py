from typing import List
from anyio import Any


class Tree:
    def __init__(self):
        self.call: str = ''
        self.returned: Any = None
        self.children: List[Tree] = []


def waysToClimb(n, possibleSteps, tree):
    tree.call = 'f('+str(n)+')'
    if n == 0:
        tree.returned = 1
        return 1
    if n == 1:
        tree.returned = 0
        return 0
    else:
        nbWays = 0
        for steps in possibleSteps:
            if (n-steps) >= 0:
                child = Tree()
                tree.children.append(child)
                nbWays += waysToClimb(n-steps, possibleSteps, child)
        tree.returned = nbWays
        return nbWays


def printTree(tree, indent=''):
    INDENT_SIZE = 6
    if tree is None or len(tree.children) == 0:
        print(tree.call + ' returned ' + str(tree.returned) + str(" (base)"))
    else:
        print(tree.call + ' returned ' + str(tree.returned))
        for child in tree.children[:-1]:
            print(indent + '|' + '-' * INDENT_SIZE, end='')
            printTree(child, indent + '|' + ' ' * INDENT_SIZE)
        child = tree.children[-1]
        print(indent + '└' + '-' * INDENT_SIZE, end='')
        printTree(child, indent + '  ' * INDENT_SIZE)

#drive
tree = Tree()
waysToClimb(10, [2, 4, 5, 8],tree)
printTree(tree)