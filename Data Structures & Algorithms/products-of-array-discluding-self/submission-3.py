class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = [1] * len(nums)
        result[0] = 1
        result[len(result) - 1] = 1

        for i in range (1, len(result)):
            result[i] = result[i-1] * nums[i-1]

        suffix = 1
        for i in range (len(result) - 1, -1, -1):
            result[i] = result[i] * suffix
            suffix = suffix * nums[i]

        return result


