class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        prefix = []
        postfix = []
        for i in range(len(nums)):
            if not prefix:
                prefix.append(nums[i])
            else:
                prefix.append(prefix[-1] * nums[i])
                
        for i in range(len(nums)-1, -1, -1):
            if not postfix:
                postfix.insert(0, nums[i])
            else:
                postfix.insert(0, postfix[0] * nums[i])
        print(prefix)
        print(postfix)
        output = []
        for i in range(len(nums)):
            if i == 0:
                output.append(1 * postfix[i+1])
            elif i == len(nums) - 1:
                output.append(prefix[i-1] * 1)
            else:
                output.append(prefix[i-1] * postfix[i+1])
        return output
        
        