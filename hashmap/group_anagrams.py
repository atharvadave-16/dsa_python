class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
       a = {}
       for i in strs:
          key = "".join(sorted(i))
          if key not in a:
             a[key] = []      
             a[key].append(i) 
          else:
                  a[key].append(i)

       return list(a.values())

# Pattern: HashMap with sorted key
# Approach: sort each word → use as key, group words with same key
# Key trick: "".join(sorted(word)) gives same key for all anagrams
# Shortcut: defaultdict(list) avoids checking if key exists
# TC: O(n * k log k) where k = max word length | SC: O(n)    