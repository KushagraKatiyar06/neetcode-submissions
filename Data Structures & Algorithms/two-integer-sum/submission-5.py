class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        solution = []  
        seen = {}

        for index, num in enumerate(nums):
            search = target - num
            if search in seen:
                solution.append(seen[search])
                solution.append(index)
                return solution
            else:
                seen[num] = index

        return solution