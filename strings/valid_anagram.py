class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
     a = {}
     b ={}
     for i in s:
        if i not in a:
            a[i] = s.count(i)
     for j in t:
        if j not in b:
            b[j] = t.count(j)       
     return a == b

#using count in for loops makes it o(n*n)
# Pattern: HashMap frequency count
# Approach: count char frequency of both strings, compare maps
# Key trick: a.get(key, 0) + 1 to build frequency map
# Shortcut: Counter(s) == Counter(t)
# TC: O(n) | SC: O(n)
def isAnagram(self, s, t):
    if len(s) != len(t):
        return False
    a, b = {}, {}
    for i in range(len(s)):
        a[s[i]] = a.get(s[i], 0) + 1
        b[t[i]] = b.get(t[i], 0) + 1
    return a == b