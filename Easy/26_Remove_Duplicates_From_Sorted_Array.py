# 26 Pseudocode

# 1. If the array is empty, return 0.
# 2. Initialize a variable `i` to 0.
# 3. Iterate over the array starting from the second element. For each element:
#   - If the current element is not equal to the element at index `i`, increment `i` and update the element at index `i` with the current element.
#4. Return `i + 1`.

class Solution:
    def removeDuplicates(self, nums):
        if not nums:
            return 0
        i = 0
        for j in range(1, len(nums)):
            if nums[j] != nums[i]:
                i += 1
                nums[i] = nums[j]
        return i + 1

sol = Solution()
print(sol.removeDuplicates([1,1,2]))  # Output: 2
print(sol.removeDuplicates([0,0,1,1,1,2,2,3,3,4]))  # Output: 5

# This method works by using two pointers `i` and `j`.
# `i` is the slow-runner while `j` is the fast-runner.
# As long as `nums[i] == nums[j]`, we increment `j` to skip the duplicate.
# When we encounter `nums[j] != nums[i]`, the duplicate run has ended so we must copy its value to `nums[i + 1]`.
# `i` is then incremented and we repeat the same process again until `j` reaches the end of array.