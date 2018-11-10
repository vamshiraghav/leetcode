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
        arr=[]
        if not head:return head
        curr=head
        while curr:
            arr.append(curr.val)
            curr=curr.next
        arr=arr[::-1]
        h=None
        for i in arr:
            if not h:
                h=ListNode(i)
                a=h
            else:
                h.next=ListNode(i)
                h=h.next
        return a
            
