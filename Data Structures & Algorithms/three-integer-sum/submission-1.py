class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        solution = []

        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:
                continue

        # pointer = i
        # pointer = i + 1
        # pointer = len(nums) - 1

            l = i + 1
            r = len(nums) - 1

            while l < r:
                currentSum = nums[i] + nums[l] + nums[r]

                if currentSum == 0:
                    solution.append([nums[i], nums[l], nums[r]])

                    r -= 1
                    while (l < r) and (nums[r] == nums[r + 1]):
                        r -= 1

                elif currentSum < 0:
                    l += 1
                else:
                    r -= 1

        return solution



        
        