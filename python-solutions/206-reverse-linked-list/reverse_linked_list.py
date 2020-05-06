"""
Reverse a singly linked list.

Example:

Input: 1->2->3->4->5->NULL
Output: 5->4->3->2->1->NULL
Follow up:

A linked list can be reversed either iteratively or recursively. Could you implement both?
"""
# Definition for singly-linked list.


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


# iterative approach
def reverseList(head: ListNode) -> ListNode:
    if head is None:
        return None
    prev = None
    cur = head
    while cur:
        cur.next, prev, cur = prev, cur, cur.next
    return prev


if __name__ == "__main__":
    l_node = ListNode()
