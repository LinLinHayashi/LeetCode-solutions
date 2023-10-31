''' Sliding window algorithm. '''

class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        l = 0 # Current left number, the start of a subarray.
        r = 1 # Current right number, the end of a subarray.
        sum = nums[l] # Sum of a subarray.
        maximum = nums[l] # Maximum of sum of a subarray.
        
        while r < len(nums):

            # If the sum of a subarray prior to the current right number is non-positive and not greater than the current right number, discard it and start a new subarray at the current right number.
            if sum <= 0 and sum <= nums[r]:
                sum = nums[r]
                l = r

            # Otherwise, keep working on the current subarray. 
            else:
                sum = sum + nums[r]

            maximum = max(maximum, sum) # Always make sure we have the maximum.
            r += 1 # Move to the next right number.

        return maximum
