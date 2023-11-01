class Solution:
    def maxProduct(self, nums: list[int]) -> int:
        res = max(nums) # The greatest number in the array, which is also the containor for the greatest subarray product.
        mostPos, mostNeg = 1, 1 # The current most positive and negative numbers, which will keep being updated when traversing the array.

        for num in nums:
            mostPos, mostNeg = max(num * mostPos, num * mostNeg, num), min(num * mostPos, num * mostNeg, num) # Key algorithm of this problem!
            res = max(res, mostPos) # Always update the greatest subarray product.
        
        return res