"""
Given the root node of a binary search tree (BST) and a value. You need to find the node in the BST that the node's value equals the given value. Return the subtree rooted with that node. If such node doesn't exist, you should return NULL.
For example, 

Given the tree:
        4
       / \
      2   7
     / \
    1   3

And the value to search: 2
You should return this subtree:

      2     
     / \   
    1   3
In the example above, if we want to search the value 5, since there is no node with value 5, we should return NULL.

Note that an empty tree is represented by NULL, therefore you would see the expected output (serialized tree format) as [], not null.
"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left_child = None
        self.right_child = None


class BST:
    treeNode = TreeNode

    def __init__(self):
        self._root = None
        self._size = 0

    @property
    def size(self):
        return self._size

    def __len__(self):
        return self.size

    def insert(self, val):
        self._root = self._insert(self._root, val)

    def _insert(self, subtree_root, val):
        if subtree_root is None:
            self._size += 1
            return self.treeNode(val)

        if val < subtree_root.val:
            subtree_root.left_child = self._insert(
                subtree_root.left_child, val)
        else:
            subtree_root.right_child = self._insert(
                subtree_root.right_child, val)
        return subtree_root

    def find(self, data):
        return self._find_node_recursively(self._root, data)

    def _find_node_recursively(self, subtree_root, val):
        if subtree_root is None:
            return None
        print(subtree_root.val)
        if subtree_root.val == val:
            return subtree_root
        elif val > subtree_root.val:
            return self._find_node_recursively(subtree_root.right_child, val)
        else:
            return self._find_node_recursively(subtree_root.left_child, val)


def searchBST(bst: BST, search_val: int):
    return bst.find(search_val)


if __name__ == "__main__":
    bst = BST()
    values = [4, 2, 7, 1, 3]
    for elem in values:
        bst.insert(elem)

    print(searchBST(bst, 2))
