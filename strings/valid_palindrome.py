def palindrome(s):
 a = s.replace(" ", "")
 a = a.lower()
 c = ""
 for i in a:
  if i.isalnum():   
     c = c + i
 return (c == c[::-1])

class Solution:
    def isPalindrome(self, s: str) -> bool:
      l = 0
      r = len(s)-1
      while l<r:
        while l<r and not s[l].isalnum():
            l = l + 1
        while l<r and not s[r].isalnum():
            r = r-1
        if s[l].lower() != s[r].lower():
            return False
        l = l+1
        r = r-1
      return True




# Pattern: Two Pointers
# Approach 1: clean string → compare with reverse → O(n) space
# Approach 2: two pointers, skip non-alnum → O(1) space
# Key trick: isalnum() filters spaces/punctuation, lower() handles case
# TC: O(n) | SC: O(1) for two pointer approach