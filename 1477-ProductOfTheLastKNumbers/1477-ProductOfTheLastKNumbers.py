# Last updated: 23/11/2026, 10:01:16 am
class ProductOfNumbers:

    def __init__(self):
        # self.arr = []
        self.nums = [1]

    def add(self, num: int) -> None:
        # self.nums.append(num)
        # self.arr.append(None)
        if(num == 0):
            self.nums = [1]
        else:
            self.nums.append(self.nums[-1]*num)

    def getProduct(self, k: int) -> int:
        ans = 1
        n = len (self.nums)
        if k >= n:
            return 0
        return self.nums[-1] // self.nums[-1-k]
            
        
        



# Your ProductOfNumbers object will be instantiated and called as such:
# obj = ProductOfNumbers()
# obj.add(num)
# param_2 = obj.getProduct(k)