from idna import valid_contextj


class Tree:
	def __init__(self, val=None, left=None, right=None):
		self.val = val
		self.left = left
		self.right = right

def dfs(tree):
	if tree is None:
		return
	else:
		print(tree.val)
		dfs(tree.left)
		dfs(tree.right)

left = Tree(3,None,None)
right = Tree(5,None,None)
tree = Tree(4,left,right)

dfs(tree)