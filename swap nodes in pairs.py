class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None or head.next == None:
            return head
        else:
            p1,p2 = head, head.next
            p1.next = self.swapPairs(p2.next)
            p2.next = p1
        return p2

Problem Link: https://leetcode.com/problems/swap-nodes-in-pairs/

Solved using recursion