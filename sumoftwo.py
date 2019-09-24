class Solution:
    def twoSum(self, nums, target):
        count = 0
        for num in nums:
            count += 1
            other_num = target - num
            if other_num in nums:
                return [nums.index(num), nums.index(other_num)]
