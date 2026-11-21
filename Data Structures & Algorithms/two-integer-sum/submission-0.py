class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        num_map = {}
        solution = []
        for i in range(len(nums)):

            goal = target - nums[i] 
            if goal in num_map:
                solution.append(num_map[goal])
                solution.append(i)
                return solution
                
            num_map[nums[i]] = i
            
                     