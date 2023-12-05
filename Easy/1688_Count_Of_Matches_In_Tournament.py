# 1688 Pseudocode

# 1. Initialize a variable `matches` to 0.
# 2. While `n` is more than 1:
#   - If `n` is even, add `n/2` to `matches` and update `n` to `n/2`.
#   - If `n` is odd, add `(n-1)/2` to `matches` and update `n` to `(n-1)/2 + 1`.
# 3. Return `matches`.

class Solution:
    def numberOfMatches(self, n):
        matches = 0
        while n > 1:
            if n % 2 == 0:
                matches += n // 2
                n //= 2
            else:
                matches += (n - 1) // 2
                n = (n - 1) // 2 + 1
        return matches

sol = Solution()
print(sol.numberOfMatches(7))  # Output: 6
print(sol.numberOfMatches(14))  # Output: 13

# This method works by using a while loop to simulate the tournament. If the number of teams is even, it adds `n/2` to `matches` and updates `n` to `n/2`. If the number of teams is odd, it adds `(n-1)/2` to `matches` and updates `n` to `(n-1)/2 + 1`. It continues this process until there's only one team left, which is the winner. Finally, it returns the total number of matches played.