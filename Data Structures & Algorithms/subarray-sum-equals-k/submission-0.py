class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:

        res=0
        prefixSum={0:1}
        currSum=0
        for i in nums:
            currSum+=i
            res+= prefixSum.get(currSum -k,0)
            prefixSum[currSum]=prefixSum.get(currSum,0) +1
        
        return res
