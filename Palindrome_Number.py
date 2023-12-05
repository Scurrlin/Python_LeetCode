# 9 Pseudocode

# Check if `x` is less than 0. If it is, return `False` because negative numbers cannot be palindromes.
# Convert `x` to a string.
# Compare the string with its reverse. If they are the same, return `True`. Otherwise, return `False`.

class Solution:
    def isPalindrome(self, x):
        if x < 0:
            return False
        str_x = str(x)
        return str_x == str_x[::-1]

sol = Solution()
print(sol.isPalindrome(121))  # Output: True
print(sol.isPalindrome(-121))  # Output: False

# This method works by first checking if `x` is less than 0. If it is, it returns `False` because negative numbers cannot be palindromes. It then converts `x` to a string and compares the string with its reverse. If they are the same, it returns `True`. Otherwise, it returns `False`.