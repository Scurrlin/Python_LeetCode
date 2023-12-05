# 21 Pseudocode

# 1. Create a dummy node and a current node pointing to the dummy node.
# 2. While both `list1` and `list2` are not `None`:
#   - If the value of `list1` is less than or equal to the value of `list2`, move the next pointer of the current node to `list1` and move `list1` to its next node.
#   - Otherwise, move the next pointer of the current node to `list2` and move `list2` to its next node.
#   - Move the current node to its next node.
# 3. If `list1` is not `None`, move the next pointer of the current node to `list1`.
# 4. If `list2` is not `None`, move the next pointer of the current node to `list2`.
# 5. Return the next node of the dummy node.

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def mergeTwoLists(self, l1, l2):
        temp = ListNode(0)
        current = temp
        while l1 and l2:
            if l1.val <= l2.val:
                current.next = l1
                l1 = l1.next
            else:
                current.next = l2
                l2 = l2.next
            current = current.next
        current.next = l1 if l1 else l2
        return temp.next

# This method works by creating a dummy node and a current node pointing to the temp node.
# It then enters a loop where it compares the values of `l1` and `l2`.
# If the value of `l1` is less than or equal to the value of `l2`, it moves the next pointer of the current node to `l1` and moves `l1` to its next node.
# Otherwise, it moves the next pointer of the current node to `l2` and moves `l2` to its next node.
# It then moves the current node to its next node.
# After the loop, if `l1` or `l2` is not `None`, it moves the next pointer of the current node to `l1` or `l2`.
# Finally, it returns the next node of the temp node, which is the head of the merged linked list.