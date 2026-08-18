class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n= len(nums)
        prefix=[1]*n
        suffix=[1]*n
        res=[]

        for i in range(1,len(nums)):
            prefix[i] = nums[i-1]*prefix[i-1]
        
        for i in range (len(nums)-2, -1,-1):
            suffix[i] = suffix[i+1]*nums[i+1]


        for i in range(n):
            res.append(prefix[i]*suffix[i])

        
        return res