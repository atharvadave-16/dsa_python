def isAnagram(self, s: str, t: str) -> bool:
      if len(s) != len(t):
        return False
      else:  
       for ch in s:
        if s.count(ch) != t.count(ch):
         return False
       return True