class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        output = [1] * n

        # Prefix pass: output[i] = product of everything left of i
        prefix = 1
        for i in range(n):
            output[i] = prefix
            prefix *= nums[i]

        # Suffix pass: multiply by product of everything right of i
        suffix = 1
        for i in range(n - 1, -1, -1):
            output[i] *= suffix
            suffix *= nums[i]

        return output
        