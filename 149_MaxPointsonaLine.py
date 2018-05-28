# Input: [[1, 1], [3, 2], [5, 3], [4, 1], [2, 3], [1, 4]]
# Output: 4
# Explanation:
# ^
# |
# |  o
# |     o        o
# |        o
# |  o        o
# +------------------->
# 0  1  2  3  4  5  6

# Definition for a point.
# class Point:
#     def __init__(self, a=0, b=0):
#         self.x = a
#         self.y = b


class Solution:
    def __init__(self):
        self.max_count = 0

    def maxPoints(self, points):
        """
        :type points: List[Point]
        :rtype: int
        """

        i = 0

        if len(points) == 1:
            return 1

        while i < len(points) - 1:
            this_x = points[i].x
            this_y = points[i].y

            line_flag = 0
            next_index = 0

            while line_flag == 0:
                next_index += 1
                next_x = points[i+next_index].x
                next_y = points[i+next_index].y
                if (this_y - next_y)**2 + (this_x - next_x)**2 != 0:
                    line_flag = 1
                if i + next_index >= len(points) - 1 and line_flag == 0:
                    return len(points)

            x1 = this_x
            y1 = this_y
            x2 = next_x
            y2 = next_y
            x_diff = x1 - x2
            y_diff = y1 - y2

            if x_diff != 0:
                a = y_diff / x_diff
                b = y1 - a * x1
            else:
                a = x1

            counter = 0
            for k in range(len(points)):

                if x_diff != 0:
                    if points[k].y == ((a * x_diff) * points[k].x + ((x_diff * y1) - y_diff * x1)) / x_diff:
                        counter += 1
                else:
                    if points[k].x == a:
                        counter += 1
            i += next_index

            if self.max_count < counter:
                self.max_count = counter
        return self.max_count
