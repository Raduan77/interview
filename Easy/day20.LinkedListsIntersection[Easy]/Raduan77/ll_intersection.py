class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


def ll_length(head):
    counter = 0
    while head:
        counter += 1
        head = head.next
    return counter


def ll_intersection(head1: Node, head2: Node)->Node:
    l1 = ll_length(head1)
    l2 = ll_length(head2)
    final_length = l1
    if l1 > l2:
        diff = l1 - l2
        for _ in range(diff):
            head1 = head1.next
        final_length = l2
    elif l1 < l2:
        diff = l2-l1
        for _ in range(diff):
            head2 = head2.next
        final_length = l1
    for _ in range(final_length):
        if head1 == head2:
            return head1
        head1 = head1.next
        head2 = head2.next
    return None


if __name__ == '__main__':
    # test case 1
    '''
    node11 = Node(3)
    node12 = Node(7)
    node3 = Node(15)
    node4 = Node(10)
    node21 = Node(99)
    node22 = Node(10)
    node11.next = node12
    node12.next = node3
    node3.next = node4
    node21.next = node22
    node22.next = node3
    '''
    # test case 2
    node11 = Node(3)
    node12 = Node(7)
    node13 = Node(98)
    node14 = Node(35)
    node3 = Node(322)
    node4 = Node(10)
    node21 = Node(99)
    node22 = Node(10)
    node11.next = node12
    node12.next = node13
    node13.next = node14
    node14.next = node3
    node3.next = node4
    node21.next = node22
    node22.next = node3

    intersection_node = ll_intersection(node11, node21)
    print(intersection_node.value)
