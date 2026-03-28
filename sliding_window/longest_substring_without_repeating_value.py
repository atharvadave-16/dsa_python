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