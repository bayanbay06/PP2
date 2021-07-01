class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        ans = 0
        summ = 0
        for i in gain:
            summ += i
            if summ > ans:
                ans = summ
        return ans


