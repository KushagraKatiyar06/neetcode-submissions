class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        L_mul = 1
        R_mul = 1

        Left = [0] * n
        Right = [0] * n

        Left[0] = 1
        Right[n - 1] = 1

        i = 1
        j = n - 2
        
        while i < n:
            L_mul *= nums[i - 1]
            Left[i] = L_mul
            

            R_mul *= nums[j + 1]
            Right[j] = R_mul

            i += 1
            j -= 1

        result = [0] * n
        
        k = 0
        while k < n:
            result[k] = Left[k] * Right[k]
            k += 1

        return result