class PrimeNumbers:
    def __init__(self, start, stop):
        self.start = start
        self.stop = stop
    def isPrimeNum(self, k):
        if k < 2:
            return False
        for i in range(2, k):
            if k % i == 0:
                return False
        return True
    def __iter__(self):
        for k in range(self.start, self.stop + 1):
            if self.isPrimeNum(k):
                yield k
for x in PrimeNumbers(1, 20):
    print(x)