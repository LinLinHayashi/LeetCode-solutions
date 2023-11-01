''' Binary search. '''
class Solution:
    def findMin(self, nums: list[int]) -> int:
        
        # The recursion base case.
        if len(nums) <= 3:
            return min(nums)

        n = len(nums) // 2 # Always select the middle of the array as the pivot.

        # If the pivot happens to be the min.
        if nums[n - 1] > nums[n] and nums[n] < nums[n + 1]:
            return nums[n]
        
        # Split the array into two halves.
        left = nums[:n]
        right = nums[n:]

        if left[0] > left[-1]: # The left half is not sorted, which indicates the min is here.
            return self.findMin(left)
        elif right[0] > right[-1]: # The right half is not sorted, which indicates the min is here.
            return self.findMin(right)
        else: # Both halves are sort so the entire array is sorted.
            return left[0]