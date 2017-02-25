class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        counter = 0
        c=[]
        nums.append(0)
        print nums
        for i in range(len(nums)):
            if nums[i] == 1:
                counter += 1
            else:
                c.append(counter)
                counter = 0
        return max(c)
#
# class Solution(object):
#     def findMaxConsecutiveOnes(self, nums):
#         cnt = 0
#         ans = 0
#         for num in nums:
#             if num == 1:
#                 cnt += 1
#                 ans = max(ans, cnt)
#             else:
#                 cnt = 0
#         return ans