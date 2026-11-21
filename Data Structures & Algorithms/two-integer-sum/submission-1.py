class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        seen = {}
        solution = []

        for index, num in enumerate(nums):
            
            goal = target - num

            if goal in seen:
                solution.append(seen[goal])
                solution.append(index)
            else:
                seen[num] = index

        return solution


        
        
