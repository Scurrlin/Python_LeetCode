# 20 Valid Parentheses

# 1. Initialize an empty stack.
# 2. Iterate over the characters in the string. For each character:
#   - If the character is an open bracket, push it onto the stack.
#   - If the character is a close bracket, check if the stack is empty. If it is, return `False` because there's no corresponding open bracket.
#   - If the stack is not empty, pop the top element from the stack and check if it matches with the close bracket. If it doesn't, return `False`.
# 3. After the iteration, check if the stack is empty. If it's not, return `False` because there are some open brackets that are not closed.
# 4. If none of the above conditions are met, return `True`.

class Solution:
    def isValid(self, s):
        stack = []
        bracket_map = {")": "(", "}": "{", "]": "["}
        for char in s:
            if char in bracket_map:
                top_element = stack.pop() if stack else '#'
                if bracket_map[char] != top_element:
                    return False
            else:
                stack.append(char)
        return not stack

sol = Solution()
print(sol.isValid("()[]{}"))  # Output: True
print(sol.isValid("(]"))  # Output: False

# This method works by using a stack to keep track of the open brackets.
#  For each character in the string, if it's an open bracket, it pushes it onto the stack.
# If it's a close bracket, it checks if the stack is empty or if the top element of the stack doesn't match with the close bracket.
# If either condition is met, it returns `False`.
# After the iteration, it checks if the stack is empty.
# If it's not, it returns `False`.
# If none of the above conditions are met, it returns `True`.