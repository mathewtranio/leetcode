# ============================================================
#  LeetCode Solutions - Python
#  Author : Tranio Mathew T
#  Topics : Arrays, Strings, HashMap, Two Pointers, Stack,
#            Linked List, Binary Search, Dynamic Programming
# ============================================================


# ─────────────────────────────────────────────────────────────
# 1. Two Sum  (LeetCode #1)  —  Easy
#    Given an array of integers and a target, return indices
#    of the two numbers that add up to target.
# ─────────────────────────────────────────────────────────────
def two_sum(nums: list[int], target: int) -> list[int]:
    seen = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            return [seen[complement], i]
        seen[num] = i
    return []

# Example
print("1. Two Sum:", two_sum([2, 7, 11, 15], 9))          # [0, 1]


# ─────────────────────────────────────────────────────────────
# 2. Valid Parentheses  (LeetCode #20)  —  Easy
#    Check if the input string has valid opening/closing
#    brackets in the correct order.
# ─────────────────────────────────────────────────────────────
def is_valid(s: str) -> bool:
    stack = []
    mapping = {')': '(', '}': '{', ']': '['}
    for char in s:
        if char in mapping:
            top = stack.pop() if stack else '#'
            if mapping[char] != top:
                return False
        else:
            stack.append(char)
    return not stack

# Example
print("2. Valid Parentheses:", is_valid("()[]{}"))         # True
print("2. Valid Parentheses:", is_valid("(]"))             # False


# ─────────────────────────────────────────────────────────────
# 3. Best Time to Buy and Sell Stock  (LeetCode #121)  —  Easy
#    Find the maximum profit from one buy-sell transaction.
# ─────────────────────────────────────────────────────────────
def max_profit(prices: list[int]) -> int:
    min_price = float('inf')
    max_profit_val = 0
    for price in prices:
        if price < min_price:
            min_price = price
        elif price - min_price > max_profit_val:
            max_profit_val = price - min_price
    return max_profit_val

# Example
print("3. Max Profit:", max_profit([7, 1, 5, 3, 6, 4]))   # 5


# ─────────────────────────────────────────────────────────────
# 4. Reverse Linked List  (LeetCode #206)  —  Easy
#    Reverse a singly linked list iteratively.
# ─────────────────────────────────────────────────────────────
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reverse_list(head: ListNode) -> ListNode:
    prev = None
    curr = head
    while curr:
        next_node = curr.next
        curr.next = prev
        prev = curr
        curr = next_node
    return prev

# Helper to build and print linked list
def build_list(vals):
    dummy = ListNode(0)
    cur = dummy
    for v in vals:
        cur.next = ListNode(v)
        cur = cur.next
    return dummy.next

def list_to_arr(head):
    result = []
    while head:
        result.append(head.val)
        head = head.next
    return result

print("4. Reverse Linked List:", list_to_arr(reverse_list(build_list([1, 2, 3, 4, 5]))))  # [5,4,3,2,1]


# ─────────────────────────────────────────────────────────────
# 5. Maximum Subarray  (LeetCode #53)  —  Medium
#    Find the contiguous subarray with the largest sum.
#    (Kadane's Algorithm)
# ─────────────────────────────────────────────────────────────
def max_subarray(nums: list[int]) -> int:
    max_sum = nums[0]
    current_sum = nums[0]
    for num in nums[1:]:
        current_sum = max(num, current_sum + num)
        max_sum = max(max_sum, current_sum)
    return max_sum

# Example
print("5. Max Subarray:", max_subarray([-2, 1, -3, 4, -1, 2, 1, -5, 4]))  # 6


# ─────────────────────────────────────────────────────────────
# 6. Climbing Stairs  (LeetCode #70)  —  Easy
#    You can climb 1 or 2 steps at a time.
#    In how many distinct ways can you reach the top (n steps)?
# ─────────────────────────────────────────────────────────────
def climb_stairs(n: int) -> int:
    if n <= 2:
        return n
    a, b = 1, 2
    for _ in range(3, n + 1):
        a, b = b, a + b
    return b

# Example
print("6. Climbing Stairs:", climb_stairs(5))              # 8


# ─────────────────────────────────────────────────────────────
# 7. Binary Search  (LeetCode #704)  —  Easy
#    Given a sorted array and target, return its index or -1.
# ─────────────────────────────────────────────────────────────
def binary_search(nums: list[int], target: int) -> int:
    left, right = 0, len(nums) - 1
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1

# Example
print("7. Binary Search:", binary_search([-1, 0, 3, 5, 9, 12], 9))  # 4


# ─────────────────────────────────────────────────────────────
# 8. Contains Duplicate  (LeetCode #217)  —  Easy
#    Return True if any value appears at least twice.
# ─────────────────────────────────────────────────────────────
def contains_duplicate(nums: list[int]) -> bool:
    return len(nums) != len(set(nums))

# Example
print("8. Contains Duplicate:", contains_duplicate([1, 2, 3, 1]))    # True
print("8. Contains Duplicate:", contains_duplicate([1, 2, 3, 4]))    # False


# ─────────────────────────────────────────────────────────────
# 9. Longest Common Prefix  (LeetCode #14)  —  Easy
#    Find the longest common prefix string among an array
#    of strings.
# ─────────────────────────────────────────────────────────────
def longest_common_prefix(strs: list[str]) -> str:
    if not strs:
        return ""
    prefix = strs[0]
    for s in strs[1:]:
        while not s.startswith(prefix):
            prefix = prefix[:-1]
            if not prefix:
                return ""
    return prefix

# Example
print("9. Longest Common Prefix:", longest_common_prefix(["flower", "flow", "flight"]))  # "fl"


# ─────────────────────────────────────────────────────────────
# 10. 3Sum  (LeetCode #15)  —  Medium
#     Find all unique triplets in the array that sum to zero.
#     Uses sorting + two-pointer technique.
# ─────────────────────────────────────────────────────────────
def three_sum(nums: list[int]) -> list[list[int]]:
    nums.sort()
    result = []
    for i in range(len(nums) - 2):
        if i > 0 and nums[i] == nums[i - 1]:
            continue  # skip duplicates
        left, right = i + 1, len(nums) - 1
        while left < right:
            total = nums[i] + nums[left] + nums[right]
            if total == 0:
                result.append([nums[i], nums[left], nums[right]])
                while left < right and nums[left] == nums[left + 1]:
                    left += 1
                while left < right and nums[right] == nums[right - 1]:
                    right -= 1
                left += 1
                right -= 1
            elif total < 0:
                left += 1
            else:
                right -= 1
    return result

# Example
print("10. 3Sum:", three_sum([-1, 0, 1, 2, -1, -4]))      # [[-1,-1,2],[-1,0,1]]
