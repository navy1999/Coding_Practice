class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashMap=defaultdict(list)

        for s in strs:
            sorted_key = "".join(sorted(s))

            hashMap[sorted_key].append(s)

        
        return list(hashMap.values())
