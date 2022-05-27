
from typing import Any


class GraphNode:
    def __init__(self, val: Any = None, neighbors=None):
        if neighbors is None:
            neighbors = []
        self.val = val
        self.neighbors = neighbors

def dfs(node, visited):
    if node is None or node in visited:
        return
    else:
        print(node.val)
        visited.add(node)
        for neighbor in node.neighbors:
            dfs(neighbor)
