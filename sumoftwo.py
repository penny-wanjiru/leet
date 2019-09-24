class Solution:
    def twoSum(self, nums, target):
        count = 0
        for num in nums:
            count += 1
            other_num = target - num
            if other_num in nums[count:]:
                return [count-1, nums[count:].index(other_num)+count]
