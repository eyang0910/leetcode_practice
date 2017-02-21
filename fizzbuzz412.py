def fizzBuzz(n):
    m=[]
    for i in range(1,n+1):
        if i%3 == 0 and i%5 !=0:
            m.append('fizz')
        elif i%5 == 0 and i%3 !=0:
            m.append('buzz')
        elif i%5 == 0 and i%3 == 0:
            m.append('fizzbuzz')
        else:
            m.append('i')
    print m
fizzBuzz(16)

# print (not 3%3)*8
#
# class Solution(object):
#     def fizzBuzz(self, n):
#         """
#         :type n: int
#         :rtype: List[str]
#         """
#         m=[]
#         for i in range(1,n+1):
#             if i%3 == 0 and i%5 !=0:
#                 m.append('Fizz')
#             elif i%5 == 0 and i%3 !=0:
#                 m.append('Buzz')
#             elif i%5 == 0 and i%3 == 0:
#                 m.append('FizzBuzz')
#             else:
#                 m.append(str(i))
#         return m

# Given solution
# def fizzBuzz(self, n):
#     return ['Fizz' * (not i % 3) + 'Buzz' * (not i % 5) or str(i) for i in range(1, n+1)]