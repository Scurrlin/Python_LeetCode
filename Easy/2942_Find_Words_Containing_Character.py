# 2942 Pseudocode

# 1. Initialize an empty list to store the indices.
# 2. Iterate over the `words` array with a for loop, for each word:
#   - Check if the character `x` is in the word.
#   - If it is, append the index of the word to the list.
# 3. Return the list of indices.

class Solution:
    def findWordsContaining(self, words, x):
        indices = []
        for i, word in enumerate(words):
            if x in word:
                indices.append(i)
        return indices

sol = Solution()
print(sol.findWordsContaining(["apple", "banana", "cherry", "date"], 'a'))  # Output: [0, 1, 2]

# This method works by iterating over the `words` array and checking if the character `x` is in each word.
# If it is, it appends the index of the word to the `indices` list.
# Finally, it returns the `indices` list.