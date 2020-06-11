class Solution:
    # def fib(self, N: int) -> int:
    def fib(self, N: int):
        f = []
        f.append(0)
        f.append(1)
        if N < 2:
            return f[N]
        for i in range(2, N+1):
            f.append(f[i-1]+f[i-2])

        return f[-1]
