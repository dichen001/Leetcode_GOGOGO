'''
Merge two sorted linked lists and return it as a new list.
The new list should be made by splicing together the nodes of the first two lists.
'''

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        '''
        if not l1:
            return l2
        if not l2:
            return l1
        if l1.val <= l2.val:
            head = l1
            node = l1
            other = l2
        else:
            head = l2
            node = l2
            other = l1
        while node and other:
            if node.next == None:
                node.next = other
                return head
            elif node.next.val < other.val:
                node = node.next
            else:
                save = node.next
                node.next = other
                node = node.next
                other = save
        return head
        '''

        if not l1:
            return l2
        if not l2:
            return l1
        if l1.val < l2.val:
            head = l1
            l1.next = self.mergeTwoLists(l1.next,l2)
        else:
            head = l2
            l2.next = self.mergeTwoLists(l1,l2.next)
        return head

x = Solution()
x.mergeTwoLists(ListNode(1),ListNode(2))
print x