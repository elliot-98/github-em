# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        debut = head
        end = head
        length = 1

        while end.next is not None:
            end = end.next
            # Computing length of linked list to get the number of
            # increments to do
            length += 1
        end = head
        if n == length:
            return debut.next

        for i in range(length - n - 1):
            debut = debut.next
            end = end.next
        # Need to do it once more with the end to skip the node to drop
        end = end.next
        # Setting the remaining of the list as the regular list, but without
        # the number to drop
        debut.next = end.next
        # Bring back the list to the beginning
        debut = head
        return debut
