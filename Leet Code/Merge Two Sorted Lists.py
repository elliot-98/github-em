# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        newList = ListNode()
        pt = newList
        
        while (list1!=None) & (list2!=None) : 
            if list1.val < list2.val :
                pt.next = list1
                list1 = list1.next
            else :
                pt.next = list2
                list2 = list2.next
            pt = pt.next
        if list1 : 
            pt.next = list1
        if list2 : 
            pt.next = list2
        return newList.next
