# 1 Pseudocode

# 1. Initialize an empty dictionary.
# 2. Iterate over the array with enumeration. For each index and number:
#   - Calculate the complement of the number with respect to the target.
#   - If the complement is in the dictionary, return the index of the complement and the current index.
#   - Otherwise, add the number and its index to the dictionary.
# 3. If no two numbers add up to the target, return an empty list.

class Solution:
    def twoSum(self, nums, target):
        num_map = {}
        for i, num in enumerate(nums):
            complement = target - num
            if complement in num_map:
                return [num_map[complement], i]
            num_map[num] = i
        return []

sol = Solution()
print(sol.twoSum([2, 7, 11, 15], 9))  # Output: [0, 1]
print(sol.twoSum([3, 2, 4], 6))  # Output: [1, 2]

# This method works by using a dictionary to keep track of the numbers it has seen so far and their indices.
# For each number, it calculates the complement with respect to the target and checks if the complement is in the dictionary.
# If it is, it returns the index of the complement and the current index.
# Otherwise, it adds the number and its index to the dictionary.
# If no two numbers add up to the target, it returns an empty list.