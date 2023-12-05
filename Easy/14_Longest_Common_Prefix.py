# 14 Pseudocode

# 1. If the array is empty, return an empty string.
# 2. Initialize the common prefix as the first string in the array.
# 3. Iterate over the rest of the strings in the array. For each string:
#   - While the string does not start with the common prefix, remove the last character from the common prefix.
# 4. Return the common prefix.

class Solution:
    def longestCommonPrefix(self, strs):
        if not strs:
            return ""
        common_prefix = strs[0]
        for s in strs[1:]:
            while not s.startswith(common_prefix):
                common_prefix = common_prefix[:-1]
        return common_prefix

sol = Solution()
print(sol.longestCommonPrefix(["flower","flow","flight"]))  # Output: "fl"
print(sol.longestCommonPrefix(["dog","racecar","car"]))  # Output: ""

# This method works by initializing the common prefix as the first string in the array and then iterating over the rest of the strings. For each string, it checks if the string starts with the common prefix. If it doesn't, it removes the last character from the common prefix. Finally, it returns the common prefix. If there is no common prefix, it returns an empty string.