class Tree:
    def __init__(self, val=None, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def treeSum(tree):
    if tree is None:
        return 0
    else:
        left = treeSum(tree.left)
        right = treeSum(tree.right)
        return tree.val + left + right


tree = Tree(5, Tree(8, Tree(3, Tree(7, None, None), None),
                    Tree(4, None, None)), Tree(1, Tree(9, None, None), None))

print(treeSum(tree))
