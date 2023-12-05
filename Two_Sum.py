# 1 Pseudocode

# The function `twoSum` is designed to find two numbers in an array that add up to a specific target number. It does this by using a dictionary to keep track of the numbers it has seen so far and their indices.

# Here's a step-by-step breakdown:

# 1. The function starts by initializing an empty dictionary `num_dict`.

# 2. It then enters a loop where it iterates over the `nums` array. For each number, it does the following:

#   - It calculates the difference between the target number and the current number. This difference is the number we need to find in the array to ensure that the current number and this difference add up to the target.

#   - It checks if this difference is already in the dictionary. If it is, that means we have found two numbers that add up to the target. The function then returns a list containing the index of the difference (which we get from the dictionary) and the index of the current number.

#   - If the difference is not in the dictionary, that means we haven't encountered the required number in the array yet. So, the function adds the current number and its index to the dictionary and continues to the next iteration.

# This process continues until the function finds a pair of numbers that add up to the target, or until it has checked all the numbers in the array.

# The reason this solution is efficient is that it only needs to iterate over the array once, making it a linear O(n) solution. The use of a dictionary allows for fast lookups to check if a number has been seen before.

class Solution:
    def twoSum(self, nums, target):
        num_dict = {}
        for i, num in enumerate(nums):
            if target - num in num_dict:
                return [num_dict[target - num], i]
            num_dict[num] = i

sol = Solution()
print(sol.twoSum([2, 7, 11, 15], 9))  # Output: [0, 1]