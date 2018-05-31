# You are given an array x of n positive numbers. You start at point(0, 0) and moves x[0] metres to the north,
# then x[1] metres to the west, x[2] metres to the south, x[3] metres to the east and so on.
# In other words, after each move your direction changes counter-clockwise.
# Write a one-pass algorithm with O(1) extra space to determine, if your path crosses itself, or not.


class Point:
    def __init__(self, a=0, b=0):
        self.x = a
        self.y = b


class Solution:
    def isSelfCrossing(self, x):
        """
        :type x: List[int]
        :rtype: bool
        """

        experienced = []
        pos = Point()
        movingPoint = Point()

        for i in range(len(x)):
            movingPoint = pos
            print(pos.x, pos.y)
            if i % 4 == 0:
                for j in range(x[i]):
                    movingPoint.y += 1
                    if movingPoint in experienced:
                        print("OK", movingPoint.x, movingPoint.y)
                        return True
                    experienced.append(movingPoint)
            elif i % 4 == 1:
                for j in range(x[i]):
                    movingPoint.x -= 1
                    if movingPoint in experienced:
                        print("OK", movingPoint.x, movingPoint.y)
                        return True
                    experienced.append(movingPoint)
            elif i % 4 == 2:
                for j in range(x[i]):
                    movingPoint.y -= 1
                    if movingPoint in experienced:
                        print("OK", movingPoint.x, movingPoint.y)
                        return True
                    experienced.append(movingPoint)
            elif i % 4 == 3:
                for j in range(x[i]):
                    movingPoint.x += 1
                    if movingPoint in experienced:
                        print("OK", movingPoint.x, movingPoint.y)
                        return True
                    experienced.append(movingPoint)

            pos.x = movingPoint.x
            pos.y = movingPoint.y

        for i in experienced:
            print(i.x, i.y)
        return False
