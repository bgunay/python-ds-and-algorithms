from typing import Any


class Tree:
    def __init__(self, val: Any = None, children=None):
        if children is None:
            children = []
        self.val = val
        self.children = children


def dfs(tree):
    if tree is None:
        return
    else:
        print(tree.val)
        for child in tree.children:
            dfs(child)


def getTreeSum(tree):
    if tree is None:
        return 0
    else:
        treeSum = tree.val
        for child in tree.children:
            treeSum += getTreeSum(child)
        return treeSum


def getTreeMax(tree):
    if tree is None:
        return float('-inf')
    else:
        treeMax = tree.val
        for child in tree.children:
            treeMax = max(treeMax, getTreeMax(child))
        return treeMax


def getTreeHeight(tree):
    if tree is None:
        return -1
    else:
        maxHeight = 0
        for child in tree.children:
            maxHeight = max(maxHeight, getTreeHeight(child))
        return 1+maxHeight


tree = Tree(10, [Tree(8, [Tree(3, [Tree(2)]), Tree(4)]),
            Tree(18, [Tree(15), Tree(21)])])


"""
                10
          8           18
       3     4     15    21
    2
"""

print("Sum: {}".format(getTreeSum(tree)))
print("Max: {}".format(getTreeMax(tree)))
print("Height {}".format(getTreeHeight(tree)))
print("dfs:")
dfs(tree)
