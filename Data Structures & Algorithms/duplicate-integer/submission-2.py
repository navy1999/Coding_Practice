class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hashMap = defaultdict(int)

        for n in nums:
            if hashMap[n] <1:
                hashMap[n] +=1
            
            else: 
                return True

        return False