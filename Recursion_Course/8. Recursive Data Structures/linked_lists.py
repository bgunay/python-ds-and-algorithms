from typing import Any


class LLNode:
    def __init__(self, val: Any = None, next=None):
        self.val = val
        self.next = next


class LinkedList:
    def __init__(self, head=None):
        self.head = head

# recursive:
def printLList(node: LLNode):
    if node is None:
        return
    else:
        print(node.val)
        printLList(node.next)


def contains(node: LLNode, val: Any):
    if node is None:
        return False
    elif node.val == val:
        return True
    else:
        return contains(node.next, val)

# iterative:
def printLList(node):
    while node is not None:
        print(node.val)
        node = node.next


def contains(node, val):
    while node is not None:
        if node.val == val:
            return True
        node = node.next
    return False
