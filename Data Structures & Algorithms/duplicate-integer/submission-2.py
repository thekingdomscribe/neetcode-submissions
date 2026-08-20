class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        unique = {}

        for i in nums:
            try:
                if(unique[i]):
                    return True
            except:
                unique[i] = True

        return False