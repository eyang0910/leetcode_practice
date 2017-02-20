
#Two sum
#https://leetcode.com/problems/two-sum/?tab=Description
#

def twoSum(nums, target):
    for i in range(0, len(nums) - 1):
        for j in range(i + 1, len(nums)):
            t = nums[i] + nums[j]
            if t == target:
                print i, j

twoSum([3,2,4],6)