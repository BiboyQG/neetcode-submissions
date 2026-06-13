class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        tmp = []
        for i in range(len(nums)):
            if nums[i] != val:
                tmp.append(nums[i])
        k = len(tmp)
        nums[:k] = tmp
        return k
