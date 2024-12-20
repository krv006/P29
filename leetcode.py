# 3136
# word = 'aya'
# a = ('a', 'e', 'i', 'o', 'u')
#
# if sum(char.isalpha() for char in word) >= 2 and all(char.isalnum() for char in word):
#     return True
# else:
#     return False
#
# from collections import Counter
# from curses.ascii import isdigit
# from lib2to3.btm_utils import reduce_tree

# 3174
# s = "a8f"
# class Solution:
#     def clearDigits(self, s: str) -> str:
#         stack = deque()
#         for ch in s:
#             if ch.islower(): stack.append(ch)
#             else: stack.pop()
#
#         return ''.join(stack)

# 541
# class Solution:
#     def reverseStr(self, s: str, k: int) -> str:
#         s = list(s)
#         for i in range(0, len(s), 2 * k):
#             s[i:i + k] = reversed(s[i:i + k])
#         return ''.join(s)

# 520
# class Solution:
#     def detectCapitalUse(self, word: str) -> bool:
#         return (word == word.capitalize() or
#                 word == word.upper()      or
#                 word == word.lower()        )

# 415
# sys.set_int_max_str_digits(10000)
# class Solution:
#     def addStrings(self, num1: str, num2: str) -> str:
#         return str(int(num1)+int(num2))

# 160
# class Solution:
#     def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
#         one = headA
#         two = headB
#
#         while one != two:
#             one = headB if one is None else one.next
#             two = headA if two is None else two.next
#         return one

# 387
# from collections import Counter
# class Solution:
#     def firstUniqChar(self, s: str) -> int:
#         count = Counter(s)
#         for i in range(len(s)):
#             if count[s[i]] == 1:
#                 return i
#         return -1

# 4
# nums1 = [1,3]
# nums2 = [2]
# nums1.append(nums2)
# print()

# 26
# class Solution:
#     def removeDuplicates(self, nums: List[int]) -> int:
#         nums[:] = sorted(set(nums))
#         return len(nums)

# 27
# class Solution:
#     def removeElement(self, nums: List[int], val: int) -> int:
#         while val in nums:
#             nums.remove(val)
#         return len(nums)


# 35
# class Solution:
#     def searchInsert(self, nums: List[int], target: int) -> int:
#         nums.append(target)
#         nums.sort()
#         return (nums.index(target))


# 66
# dilda = 1
# for i in range(len(digits) - 1, -1, -1):
#     digits[i] += dilda
#     if digits[i] > 9:
#         dilda = 1
#         digits[i] %= 10
#     else:
#         dilda = 0
# else:
#     if dilda:
#         digits.insert(0, dilda)
# return digits

# 88
# class Solution:
#     def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
#         nums1[m:] = nums2
#         nums1.sort()

# todo ======================================================

# 242
# class Solution:
#     def isAnagram(self, s: str, t: str) -> bool:
#         if len(s) != len(t):
#             return False
#         return sorted(s) == sorted(t)

# 268
# class Solution:
#     def missingNumber(self, nums: List[int]) -> int:
#         n = len(nums)
#         return (n * (n + 1) // 2) - sum(nums)

# 349
# class Solution:
#     def intersection(self, nums: List[List[int]]) -> List[int]:
#         my_list=[]
#         for i in nums:
#             my_list.extend(i)
#         c=Counter(my_list)
#         res=[]
#         for k, v in c.items():
#             if v>=len(nums):
#                 res.append(k)
#         return sorted(res)\

# 350
# class Solution:
#     def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
#         return list((Counter(nums1) & Counter(nums2)).elements())
#         # n = Counter(nums1)
#         # n1 = Counter(nums2)
#         # s = n & n1
#         # return list(s.elements())
#
#         # return (Counter(nums1)&Counter(nums2)).elements()


# 414
# l = list(set(nums))
# l.sort()
# if len(l) >= 3:
#     print(l[len(l) - 3])
# print(max(l))


# s = "SALOM UMIDA XITOYLIK"
# print(s)
#
# a = 5
# b = 12
# print(a + b)


# 1903
# num = "4306"
# for i in range(len(num) - 1, -1, -1):
#     if num[i] in "13579":
#         print(num[:i + 1])
# print("")
