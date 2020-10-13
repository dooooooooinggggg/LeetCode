# class Solution:
#     def firstUniqChar(self, s: str) -> int:

#         if len(s) == 0:
#             return -1
#         if len(s) == 1:
#             return 0

#         for char_index in range(len(s)-1):
#             is_repeat = 0

#             this_s = s[char_index:len(s)]
#             find_char = this_s[0]

#             for c in range(1,len(this_s)):
#                 if this_s[c] == find_char:
#                     is_repeat = 1
#                     break

#             if is_repeat:
#                 continue
#             else:
#                 return char_index

#         return -1
class Solution:
    def firstUniqChar(self, s: str) -> int:
        return -1
