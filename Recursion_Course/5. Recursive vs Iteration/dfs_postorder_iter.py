class Tree:
	def __init__(self, val=None, left=None, right=None):
		self.val = val
		self.left = left
		self.right = right

def postorder(tree):
    stack = []
    stack.append(('call', tree))
    while stack:
        action, node = stack.pop()
        if action == 'call':
            if node is None:
                pass
            else:
                stack.append(('resume', node))
                stack.append(('call', node.right))
                stack.append(('call', node.left))
        else:
            print(node.val)