def hasCycle(self, head: Optional[ListNode]) -> bool:
        map = {}
        cur = head
        map[cur] = 1
        nxt = 0
        if head:
         while  nxt != None:
            nxt = cur.next
            cur = nxt
            map[cur] = 1 + map.get(cur,0)
            if map[cur] == 2:
                return True
         return False
        else: return False



# first approach with hashmap
#floyd tortoise and hare
def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow,fast =head,head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False 