from collections import defaultdict


def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
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


#sorted approach
def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        groups = defaultdict(list)

        for s in strs:
            key = ''.join(sorted(s))
            groups[key].append(s)

        return list(groups.values())