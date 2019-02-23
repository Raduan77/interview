class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def is_unival(root):
    if root == None:
        return (0, True)
    left_count, left_is_unival = is_unival(root.left)
    right_count, right_is_unival = is_unival(root.right)
    is_unival_node = True
    if not (left_is_unival or right_is_unival):
        is_unival_node = False
    if root.left != None and root.left.value != root.value:
        is_unival_node = False
    if root.right != None and root.right.value != root.value:
        is_unival_node = False
    if is_unival_node:
        return (left_count+right_count+1, True)
    else:
        return (left_count+right_count, False)


if __name__ == "__main__":
    assert is_unival(Node(1, Node(1), Node(1)))[0] == 3
    assert is_unival(Node(0, Node(1),
                          Node(0, Node(1, Node(1), Node(1)), Node(0))))[0] == 5
    assert is_unival(Node(3, None,
                          Node(3, None, Node(3, None, Node(3)))))[0] == 4
    print("All tests hass passed!")
