def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        a = []
        map = {"}":"{","]":"[",")":"("}
        for  i in s:
            if i in map:
                if a and a[-1] == map[i]:
                    a.pop()
                else:return False
            else: a.append(i)
        return True if not a else False