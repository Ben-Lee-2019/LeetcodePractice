class Solution:
    def arrayNesting(self, nums):
        ans, n = 0, len(nums)
        vis = [False] * n
        for i in range(n):
            cnt = 0
            while not vis[i]:
                vis[i] = True
                i = nums[i]
                cnt += 1
            ans = max(ans, cnt)
        return ans

if __name__ == "__main__":
    nums = [5,4,0,3,1,6,2]
    s = Solution()
    print(s.arrayNesting(nums))
