class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        prefixSums=defaultdict(int)
        suffixSums=defaultdict(int)

        for i in range(len(nums)):
            if(i==0):
                prefixSums[i]=nums[i]
            else:
                prefixSums[i]=nums[i] + prefixSums[i-1]

        for i in range(len(nums)-1,-1,-1):
            if(i==len(nums)-1):
                suffixSums[i]=nums[i]
            
            else:
                suffixSums[i]=nums[i] + suffixSums[i+1]

        for i in range(len(nums)):
            if(prefixSums[i] == suffixSums[i]):
                return i
        
        return -1

