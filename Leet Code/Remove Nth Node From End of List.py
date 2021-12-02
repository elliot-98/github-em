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

        while end.next != None : 
            end = end.next
            length += 1    #On prend la longueur de la liste chaînée pour savoir le nombre d'incrémentations à faire 
        end = head         
        if n==length : 
            return (debut.next)
        
        for i in range(length-n-1):
            debut = debut.next
            end = end.next
        end = end.next     #On doit le faire une fois de plus avec le end pour sauter le noeud à enlever 
        debut.next = end.next    #On set la suite de la liste comme étant la liste normale, mais sans le nombre à retirer 
        debut = head   #On ramène la liste au début 
        return(debut)
