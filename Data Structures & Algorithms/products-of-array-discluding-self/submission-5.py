class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # prefix

        solution = [1] * len(nums)

        for i in range(1, len(solution)):
            solution[i] = nums[i - 1] * solution[i - 1]

        multiple = 1
        for i  in range(len(solution) - 2, -1, -1):
            multiple = multiple * nums[i + 1]
            solution[i] = solution[i] * multiple

        return solution
