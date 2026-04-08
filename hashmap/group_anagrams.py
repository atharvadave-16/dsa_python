def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
       map = {}
       output = []
       for i in strs:
        a = [0]*26
        for j in i:
           index = ord(j) - ord("a")
           a[index] += 1 
        b = tuple(a)
        map[b] = map.get(b,[])
        map[b].append(i)
       return list(map.values())