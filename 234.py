# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        st=[]
        curr=head
        while curr:
            st.append(curr.val)
            curr=curr.next
        if st==st[::-1]:
            return True
        else:
            return False
        
