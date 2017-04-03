# def reverseString(s):
#     m=''
#     for i in range(len(s)):
#         print i,len(s)
#         m= m +(s[len(s)-i-1])
#     print m
# reverseString('hello')

class Solution(object):
    def reverseString(self, s):
        """
        :type s: str
        :rtype: str
        """
        return s[::-1]