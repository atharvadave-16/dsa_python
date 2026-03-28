def lengthOfLongestSubstring(self, s: str) -> int:
        stack = []
        value = 0
        a = []
        for i in s:
            if i not in a:
                a.append(i)
                value = value + 1
                stack.append(value)
            else:
                while i in a:
                    a.pop(0)
                    
                a.append(i)
                value = len(a) 
        if stack: return(max(stack)) 
        else: return 0   

#brute force applied first learned concept sliding window 
# below is the correct and efficient structure, used set for o(1) per operation 
def lengthOfLongestSubstring(self, s: str) -> int:
        set1 = set()
        length  = 0
        l = 0
        for r in range(len(s)):
            while s[r] in set1:
                set1.remove(s[l])
                l = l + 1
            set1.add(s[r])
            length = max(length,r-l+1)    
        return(length)         