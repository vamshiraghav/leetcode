# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        if not headA or not headB:
            return None
        curr=headA
        nset=set()
        la=0
        while curr:
            curr=curr.next
            la+=1
        lb=0
        curr=headB
        while curr:
            curr=curr.next
            lb+=1
        curra,currb=headA,headB
        if la>lb:
            for i in range(la-lb):
                curra=curra.next
        if lb>la:
            for i in range(lb-la):
                currb=currb.next
                 
        while curra!=currb:
            curra=curra.next
            currb=currb.next
        return curra
            
            
        
