# class Solution:
#     def removeDuplicates(self, nums: List[int]) -> int:
#         index = 0
#         one_before = -1
#         while(True):
#             if index >= len(nums)-1:
#                 return len(nums)

#             if nums[index] == one_before:
#                 nums = nums[:index]+nums[index+1:]
#             else:
#                 one_before = nums[index]
#                 index += 1

# できているはずなのに通らない
# Pythonのポインタ、どうなってるんだ

def tmp(nums):
    index = 0
    one_before = -1
    while(True):
        print("{}:: {} -> {}".format(index, len(nums), nums))
        # print(nums)

        # print("{}: {}".format(index, nums))
        if index >= len(nums)-1:
            break

        if nums[index] == one_before:
            nums = nums[:index]+nums[index+1:]
        else:
            one_before = nums[index]
            index += 1
    print(nums)
    return len(nums)


l = [0, 1, 1, 3, 3, 4, 5]
l = [1, 1, 2]
l = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]

# print(l[0:])
# print(l[1:])
# print(l[:1])

print(tmp(l))
print(l)
