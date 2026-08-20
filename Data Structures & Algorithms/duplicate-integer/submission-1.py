class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        existingNums = set()
        for i in nums:     
            existingNums.add(i)

        return len(existingNums) != len(nums)