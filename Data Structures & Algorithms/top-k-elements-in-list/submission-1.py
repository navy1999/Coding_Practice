class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashMap= defaultdict(int)

        for n in nums:
            hashMap[n] +=1
        
        sorted_freq=sorted(hashMap,key=lambda x: hashMap[x],reverse=True)

        return sorted_freq[:k]
