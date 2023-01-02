class Solution:
    def hammingWeight(self, n: int) -> int:
        s = '{:032b}'.format(n)
        count = 0
        for char in s:
            if char == '1':
                count += 1
        return count

s = Solution()
print(s.hammingWeight(11))