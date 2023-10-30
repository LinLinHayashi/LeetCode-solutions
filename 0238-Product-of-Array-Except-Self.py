''' Handle 0's in the array. '''

class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        productTotal = 1
        zeros = [] # An array to contain the indexes of 0's in nums.

        # Find indexes of 0's in nums and store them in zeros. Also, find the product of all non-zero elements in nums.
        for i in range(len(nums)):
            if nums[i] == 0:
                zeros.append(i)
                continue
            productTotal =  productTotal * nums[i]
        
        products = [] # The result array.

        # If there are more than one 0's in nums, then return an all-zero array.
        if len(zeros) > 1:
            for _ in nums:
                products.append(0)
            return products
        
        # If there is no 0 in nums, then remove the current element from the product.
        elif len(zeros) == 0:
            for _ in nums:
                products.append(int(productTotal / _))
            return products
        
        # If there is one 0 in nums, find its index and handle it.
        else:
            for i in range(len(nums)):
                if i == zeros[0]:
                    products.append(productTotal)
                else:
                    products.append(0)
            return products