from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]: # "Optional" indicates the variable can be none.
        head = ListNode()
        cur = head # This is how a pointer works in Python. Here cur is NOT a copy of head; cur IS head.
        carry = 0

        while l1 != None or l2 != None or carry == 1:

            # Check if l1 and l2 are none.
            if l1:
                val1 = l1.val
            else:
                val1 = 0
            if l2:
                val2 = l2.val
            else:
                val2 = 0    

            value = val1 + val2 + carry

            if value > 9:
                value = value % 10
                carry = 1
            else:
                value = value
                carry = 0
            
            node = ListNode(value) # Create a new ListNode whose val is value.
            cur.next = node # Since cur IS head, this equals head.next = node in the first loop.
            cur = node # Now cur IS the next ListNode.

            # Check if l1 and l2 are none to avoid the "TypeNone" error.
            if l1:
                l1 = l1.next
            else:
                l1 = None
            if l2:
                l2 = l2.next
            else:
                l2 = None
            
        return head.next