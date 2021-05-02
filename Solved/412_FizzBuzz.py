class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        r = []
        for i in range(1, n+1):
            if i % 15 == 0:
                tmp = "FizzBuzz"
            elif i % 3 == 0:
                tmp = "Fizz"
            elif i % 5 == 0:
                tmp = "Buzz"
            else:
                tmp = str(i)
            r.append(tmp)
        return r
