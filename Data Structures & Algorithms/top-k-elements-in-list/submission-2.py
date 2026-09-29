class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = defaultdict(int)
        res=[]
        for i in nums:
            if i not in d:
                d[i]=0
            d[i]+=1
            
        d= sorted(d,key= d.get, reverse=True)
        for i in range(k):
            res.append(d[i])
        
        return res