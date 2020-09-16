Problem Statement:
https://leetcode.com/problems/middle-of-the-linked-list/


class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        if head is None:
            return head
        slow = head
        fast = head
        while(fast is not None  and fast.next is not None):
            slow = slow.next
            fast = fast.next.next
        return slow

#Here we are using two point algorithm where we have 2 pointers slow and fast. Slow traverses one step ahead at a time and fast pointer traverses 2 step ahead at a time. So, when we are the end of the list(i.e Fastpointer) we have our middle of the list(i.e Slowpointer)