class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        hashMap = {}
        for eachValue in nums:
            if eachValue in hashMap:
                return True
            else:
                hashMap[eachValue] = 1
        return False