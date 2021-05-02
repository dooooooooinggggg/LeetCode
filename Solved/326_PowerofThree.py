# print(2**31-1)

# e = 3
# template = "2147483647"
# template = list("0000000000")

# integer_list = list("9876543210")

# target = 27

# for i in range(len(template)):
#     for j in integer_list:
#         template[i] = j
#         tmp = int("".join(template))
#         if tmp**e == target:
#             print("result: {}".format(tmp))
#         if tmp**e <= target:
#             continue


def is_three_power(n):
    if n % 3 == 0:
        return is_three_power(n//3)
    if n == 1:
        return True
    return False


print(is_three_power(81))


class Solution:
    def is_three_power(self, n):
        if n % 3 == 0:
            return self.is_three_power(n//3)
        if n == 1:
            return True
        return False

    def isPowerOfThree(self, n: int) -> bool:
        if n == 0:
            return False
        return self.is_three_power(n)
