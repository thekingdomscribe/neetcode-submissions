class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        res = []
        for i, num in enumerate(nums):
            res.append([num, i])

        res.sort()
        i, j = 0, len(nums) - 1

        while i < j:
            current = res[i][0] + res[j][0]
            if current == target:
                return [min(res[i][1], res[j][1]),
                        max(res[i][1], res[j][1])]

            elif(current < target):
                i+=1
            else:
                j-=1
                
        return []