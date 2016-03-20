# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        new_head = None
        while head:
            next = head.next
            head.next = new_head
            new_head = head
            head = next
        return new_head

        '''
        while head:
            node = head
            head = head.next
            node.next = new_head
            new_head = node
        '''