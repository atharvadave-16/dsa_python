def palindrome(s):
 a = s.replace(" ", "")
 a = a.lower()
 c = ""
 for i in a:
  if i.isalnum():   
     c = c + i
 return (c == c[::-1])
print(palindrome("A man, a plan, a canal: Panama"))