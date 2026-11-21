class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        seen = {}
        result = []

        for index, num in enumerate(nums):
            goal = target - num
            if goal in seen:
                result.append(seen[goal])
                result.append(index)
            else:
                seen[num] = index

        return result
        