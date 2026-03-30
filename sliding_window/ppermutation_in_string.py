def checkInclusion(self, s1: str, s2: str) -> bool:
        l = 0
        count1 ={}
        count2 ={}
        a = len(s1)
        for i in s1:
            count1[i] = 1 + count1.get(i,0)
        for r in range(len(s2)):
            count2[s2[r]] = 1 + count2.get(s2[r], 0)
            if r - l + 1 > len(s1):
             count2[s2[l]] = count2[s2[l]] - 1
             if count2[s2[l]] == 0:
                del count2[s2[l]]
             l += 1       
            if count1 == count2:
                    return True           
        return False 