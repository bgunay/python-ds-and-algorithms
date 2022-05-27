class Tree:
    def __init__(self, val=None, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def treeSum(tree):
    stack = []
    output = [None]
    stack.append(('call', tree, output, [None], [None]))
    while stack:
        action, node, ret, left, right = stack.pop()
        if action == 'call':
            if node is None:
                ret[0] = 0
            else:
                stack.append(('resume', node, ret, left, right))
                stack.append(('call', node.right, left, [None], [None]))
                stack.append(('call', node.left, right, [None], [None]))
        else:
            ret[0] = node.val+left[0]+right[0]
    return output[0]

tree = Tree(5,Tree(4,Tree(3)),Tree(7,Tree(6)))
print(treeSum(tree))