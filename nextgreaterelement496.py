
def nextGreaterElement(findNums, nums):
        """
        :type findNums: List[int]
        :type nums: List[int]
        :rtype: List[int]
        """
        solution = []
        for i in range(len(findNums)):
            m=0
            for j in range(len(nums)-1):
                if findNums[i] == nums[j]:
                    for k in range(j,len(nums)):
                        if nums[k] > findNums[i]:
                            solution.append(nums[k])
                            m=1
                            break
            if m==0:
                solution.append(-1)
        return solution

nextGreaterElement([4,2],[1,3,2])

# given solution
# d = {}
# st = []
# ans = []
# 
# for x in nums:
#     while len(st) and st[-1] < x:
#         d[st.pop()] = x
#     st.append(x)
#
# for x in findNums:
#     ans.append(d.get(x, -1))
#
# return ans