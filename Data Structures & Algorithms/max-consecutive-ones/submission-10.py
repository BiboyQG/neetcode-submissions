class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        n, res, cnt = len(nums), 0, 0
        for i in range(n):
            if nums[i] == 0:
                res = max(res, cnt)
                cnt = 0
            else:
                cnt += 1

        return max(res, cnt)