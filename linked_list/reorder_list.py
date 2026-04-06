from typing import Optional
# Definition for singly-linked list.
class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        
        count = 0
        curr = head

        while curr: 
          count += 1
          curr = curr.next
 
        curr = head
        l = count // 2

        while l:
         curr = curr.next
         l -= 1

        a = curr.next
        curr.next = None


        prev = None
        curr = a   

        while curr:
         next_temp = curr.next
         curr.next = prev
         prev = curr
         curr = next_temp


        first, second = head, prev
        while second:
         tmp1 = first.next
         tmp2 = second.next

         first.next = second
         second.next = tmp1

         first = tmp1
         second = tmp2
