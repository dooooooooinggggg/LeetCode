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

        for i in range(len(points)):
            if len(points) == 1:
                return 1
            for j in range(i+1, len(points)):
                x1 = points[i].x
                y1 = points[i].y
                x2 = points[j].x
                y2 = points[j].y
                x_diff = x1 - x2
                y_diff = y1 - y2

                count = 1

                if x_diff != 0:
                    a = y_diff / x_diff
                    b = y1 - a * x1
                    print('y = %fx + %f' % (a, b))
                else:
                    a = x1
                    print('x = %f' % (a))

                if points[i] == points[j]:
                    # count += 1
                    for k in range(1, len(points)):
                        if x_diff != 0:
                            if points[k].y == ((a * x_diff) * points[k].x + ((x_diff * y1) - y_diff * x1)) / x_diff:
                                count += 1
                        else:
                            if points[k].x == a:
                                count += 1
                        print('now_count is %d and x:%s, y:%s' %
                              (count, points[k].x, points[k].y))
                else:
                    for k in range(j, len(points)):
                        if x_diff != 0:
                            if points[k].y == ((a * x_diff) * points[k].x + ((x_diff * y1) - y_diff * x1)) / x_diff:
                                count += 1
                        else:
                            if points[k].x == a:
                                count += 1
                        print('now_count is %d and x:%s, y:%s' %
                              (count, points[k].x, points[k].y))

                if self.max_count < count:
                    self.max_count = count
        return self.max_count
