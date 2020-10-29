class Solution:
    def reverse(self, x: int) -> int:
        last_x = 1
        if x < 0:
            last_x = -1
        ab_value = x * last_x
        ab_value_str = ''.join(list(reversed(str(ab_value))))
        r = int(ab_value_str)*last_x
        minimum = 2**31 * -1
        maximum = 2**31 - 1
        if r < minimum or r > maximum:
            return 0

        return r
