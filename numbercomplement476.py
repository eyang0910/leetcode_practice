# class Solution(object):
#     def findComplement(self, num):
#         """
#         :type num: int
#         :rtype: int
#         """
#         numbin = bin(num)[2:]
#         # print numbin
#         # comp=[0 for j in range(len(numbin))]
#         comp = 0
#         for i in range(len(numbin)):
#             comp = (1 - int(numbin[i])) * 2 ** (len(numbin) - i - 1) + comp
#             print comp, i
#         # comp[i]=1-int(numbin[i])
#         # comp=int(comp)
#         return comp


# class Solution(object):
#     def findComplement(self, num):
#         """
#         :type num: int
#         :rtype: int
#         """
#         numbin = bin(num)[2:]
#         return (2 ** len(numbin) -1) ^ num


# option1 ; calculation
def findComplement( num):
    """
    :type num: int
    :rtype: int
    """
    numbin = bin(num)[2:]
    # print numbin
    # comp=[0 for j in range(len(numbin))]
    comp = 0
    for i in range(len(numbin)):
        comp = (1 - int(numbin[i])) * 2 ** (len(numbin) - i - 1) + comp
    print comp
findComplement (5)


#option2 : move
def findComplement2(num):
        numbin = bin(num)[2:]
        print (2 ** len(numbin) -1) ^ num
findComplement2(5)
