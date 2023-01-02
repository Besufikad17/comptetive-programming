class Solution:
    def missingNumber(self, nums: list) -> int:
        for i in range(len(nums) + 1):
            if nums.count(i) == 0:
                return i

s = Solution()
print(s.missingNumber([3,0,1]))