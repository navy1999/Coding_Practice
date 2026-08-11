class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashMap=defaultdict(lambda:-1)
        
        for i in range(len(nums)):
            if(hashMap[target-nums[i]]>-1):
                return [hashMap[target-nums[i]],i]
            hashMap[nums[i]]=i

        return []