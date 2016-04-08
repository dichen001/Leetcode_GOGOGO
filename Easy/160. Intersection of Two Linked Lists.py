"""
Write a program to find the node at which the intersection of two singly linked lists begins.


For example, the following two linked lists:

A:          a1 → a2
                   ↘
                     c1 → c2 → c3
                   ↗
B:     b1 → b2 → b3
begin to intersect at node c1.


Notes:

If the two linked lists have no intersection at all, return null.
The linked lists must retain their original structure after the function returns.
You may assume there are no cycles anywhere in the entire linked structure.
Your code should preferably run in O(n) time and use only O(1) memory.
"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

## just realized this smart idea. if two lists are going to merge, they will have the same part from the end anyway.
## by letting one running all the way to the end, and switch to the other list's head, these two list can compare the same part.
## say len(A) == a, len(B) == b. b>a, then b-a when A switch to B's head,
## then when B switch to A's head, there lefts B: a, A: b-(b-a)==a nodes to compare

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        if not headA or not headB:
            return None
        A,B = headA,headB
        while A != B:
            if A == None:
                A = headB
            else:
                A = A.next
            if B == None:
                B = headA
            else:
                B = B.next
        return A
