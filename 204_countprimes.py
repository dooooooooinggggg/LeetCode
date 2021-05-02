class Solution:
    def isPrime(self, n):
        for i in range(2, int(n**(1/2))+1):
            if n % i == 0:
                return False
        return True

    def countPrimes(self, n: int) -> int:
        primeCount = 0
        if n == 0 or n == 1:
            return primeCount
        for i in range(2, n):
            if (self.isPrime(i)):
                primeCount += 1
        return primeCount


aiueo = 1500000
# print(aiueo)
# print(aiueo**(1/2))
# print(int(aiueo**(1/2)))


def isPrimeTmp(n):
    for i in range(2, int(n**(1/2))+1):
        if n % i == 0:
            return False
    return True


testRes = 0
for i in range(2, aiueo):
    # print("{}: {}".format(i, isPrimeTmp(i)))
    if (isPrimeTmp(i)):
        testRes += 1

print(testRes)
