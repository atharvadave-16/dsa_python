# Definition for singly-linked list.
class ListNode(object):
     def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: Optional[ListNode]
        :type l2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        dummy = ListNode(0)
        curr = dummy
        c = 0
        while l1 or l2 :
         if l1 is None:
          a =  l2.val
          b = ((a+c)%10)
          c = (a+c)//10
          l2 = l2.next
          
         elif l2 is None:
            
          a = l1.val 
          b = ((a+c)%10)
          c = (a+c)//10
          l1 = l1.next
         else :
          a = l1.val + l2.val
          b = ((a+c)%10)
          c = (a+c)//10
          l1 = l1.next
          l2 = l2.next 
         nxt = ListNode(b)
         curr.next = nxt
         curr = nxt
        if c :
         nxt = ListNode(c)
         curr.next = nxt
         curr = nxt

          

        return dummy.next
    

# more cleaner code but slower
def addTwoNumbers(self, l1, l2):
        """
        :type l1: Optional[ListNode]
        :type l2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        dummy = ListNode(0)
        curr = dummy
        c = 0

        while l1 or l2 or c:
         v1 = l1.val if l1 else 0
         v2 = l2.val if l2 else 0

         total = v1 + v2 + c
         b = total % 10
         c = total // 10

         curr.next = ListNode(b)
         curr = curr.next

         if l1: l1 = l1.next
         if l2: l2 = l2.next

        return dummy.next