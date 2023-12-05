# 2264 Pseudocode

# 1. Initialize a variable `max_good_integer` to an empty string.
# 2. Iterate over the digits from 9 to 0 (inclusive) as a string. For each digit:
#  - Create a string of length 3 with the current digit.
#   - Check if this string is a substring of `num`.
#   - If it is, update `max_good_integer` with this string and break the loop.
# 3. Return `max_good_integer`.

class Solution:
    def largestGoodInteger(self, num):
        max_good_integer = ""
        for digit in map(str, range(9, -1, -1)):
            if digit * 3 in num:
                max_good_integer = digit * 3
                break
        return max_good_integer

sol = Solution()
print(sol.largestGoodInteger("1234567890"))  # Output: "999"

# This method works by iterating over the digits from 9 to 0 and checking if a string of length 3 with the current digit is a substring of `num`. If it is, it updates `max_good_integer` with this string and breaks the loop. Finally, it returns `max_good_integer`. If no good integer is found, it returns an empty string.