# https://leetcode.com/problems/hamming-distance/?tab=Description
def hammingDistance( x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        x2=bin(x)[2:].zfill(32)
        y2=bin(y)[2:].zfill(32)
        hamming = 0
        # print x2,y2
        for i in range (32) :
            # print i
            if x2[i]!= y2[i] :
                hamming+=1
                # print i
        print hamming
hammingDistance(56,23)


# class Solution(object):
#     def hammingDistance(self, x, y):
#         """
#         :type x: int
#         :type y: int
#         :rtype: int
#         """
#         x2=bin(x)[2:].zfill(32)
#         y2=bin(y)[2:].zfill(32)
#         hamming = 0
#         # print x2,y2
#         for i in range (32) :
#             # print i
#             if x2[i]!= y2[i] :
#                 hamming+=1
#                 # print i
#         return hamming