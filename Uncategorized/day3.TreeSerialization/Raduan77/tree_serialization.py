'''
Given the root to a binary tree, implement serialize(root),
which serializes the tree into a string,
and deserialize(s), which deserializes the string back into the tree.

For example, given the following Node class

class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
The following test should pass:

node = Node('root', Node('left', Node('left.left')), Node('right'))
assert deserialize(serialize(node)).left.left.val == 'left.left'

'''


class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    index = 0

    def serialize(self, node):
        result = [node.val]
        result += self.serialize(node.left) if node.left else ["null"]
        result += self.serialize(node.right) if node.right else ["null"]
        return result

    def deserialize(self, tree, index=0, start=True):
        if start:
            self.index = 0
        if tree[index] != 'null':
            val = tree[index]
            self.index += 1
            left_val = self.deserialize(tree, index=self.index, start=False)
            right_val = self.deserialize(tree, index=self.index, start=False)
            return Node(val, left_val, right_val)
        else:
            self.index += 1
            return None


if __name__ == '__main__':
    node = Node('1', Node('2'), Node('3', Node('4'), Node('5')))
    sol = Solution()
    print(" ".join(sol.serialize(node)))
    print(sol.serialize(sol.deserialize(sol.serialize(node))))
    node = Node('root', Node('left', Node('left.left')), Node('right'))
    assert sol.deserialize(sol.serialize(node)).\
        left.left.val == 'left.left'
    print("tests passed!")
