class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = float("inf")
        l, r = 0, len(nums) - 1
        while l <= r:
            if nums[l] < nums[r]:
                res = min(res, nums[l])
                break
            m = l + (r-l) // 2
            res = min(res, nums[m])
            if nums[m] >= nums[l]:
                # left sorted portion - search in right portion
                l = m + 1
            else:
                # right sorted portion - search in left portion 
                r = m - 1
        
        return res