# Last updated: 27/10/2026, 10:43:33 am
class Solution:
    def check(self,arr):
        for i in range(len(arr)):
            arr[i][0] = "."
        
        for j in range(len(arr[0])):
            arr[len(arr)-1][j]="."


    def createGrid(self, m: int, n: int) -> list[str]:
        arr = []
        for i in range(m):
            st = ""
            for j in range(n):
                st+="#"
            arr.append(list(st))
        self.check(arr)
        z = ["".join(i) for i in arr ]

        # print(z)
        return z
        