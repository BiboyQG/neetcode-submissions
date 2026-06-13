class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        glob_max_consecutive_ones = 0
        for i in range(len(nums)):
            if nums[i] == 1 and i < len(nums):
                max_consecutive_ones = 1
                j = i + 1
                while j < len(nums) and nums[j] == 1:
                    max_consecutive_ones += 1
                    j += 1
                if max_consecutive_ones > glob_max_consecutive_ones:
                    glob_max_consecutive_ones = max_consecutive_ones

        return glob_max_consecutive_ones