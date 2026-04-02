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