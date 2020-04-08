from lib import ListNode


class Solution:
    """
    876. Middle of the Linked List.

    :see https://leetcode.com/problems/middle-of-the-linked-list/
    """

    def middleNode(self, head: ListNode) -> ListNode:
        length, node = 0, head
        while node:
            length += 1
            node = node.next

        middle = length // 2
        node = head
        for i in range(middle):
            node = node.next
        return node
