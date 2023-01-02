class Solution:
    def countBits(self, n: int) -> list:
        result = []
        for i in range(0, n + 1):
            s = '{:032b}'.format(i)
            count = 0
            for char in s:
                if char == '1':
                    count += 1
            result.append(count)
        return result

s = Solution()
print(s.countBits(5))