"""
Calculate the sum of two integers a and b, but you are not allowed to use the operator + and -.

Example:
Given a = 1 and b = 2, return 3.

"""


# def getSum(a, b):
#     """
#     :type a: int
#     :type b: int
#     :rtype: int
#     """
#     # n = []
#     # MAX_INT = 0x7FFFFFFF
#     MIN_INT = 0x80000000
#     mask = 0x100000000
#     max_value = 0x7fffffff
#     if a < max_value and b < max_value:
#         print  (a ^ b) & mask, ((a & b) << 1) & mask
# getSum(3,5)

def getSum(a, b):
    """
    :type a: int
    :type b: int
    :rtype: int
    """
    # 32 bits integer max
    MAX = 0x7FFFFFFF
    # 32 bits interger min
    MIN = 0x80000000
    # mask to get last 32 bits
    mask = 0xFFFFFFFF
    while b != 0:
        # ^ get different bits and & gets double 1s, << moves carry
        print '.........',a,b
        a, b = (a ^ b) & mask, ((a & b) << 1) & mask
        print a,b
    # if a is negative, get a's 32 bits complement positive first
    # then get 32-bit positive's Python complement negative
    print a if a <= MAX else ~(a ^ mask)
getSum(3,5)