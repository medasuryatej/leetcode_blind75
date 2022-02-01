class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        currSum = nums[0]
        maxSum = nums[0]
        for index, value in enumerate(nums[1:]):
            currSum += value
            if currSum < value:
                currSum = value
            maxSum = max(maxSum, currSum)
        return maxSum