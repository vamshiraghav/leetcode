class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
	test
        """
        st=""
        st=''.join(e for e in s if e.isalnum()).lower()
        if st==st[::-1]:
            return True
        else:
            return False
        
        
        
