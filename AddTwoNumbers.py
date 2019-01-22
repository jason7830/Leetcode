# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def addTwoNumbers(self, l1, l2):
        l = root = ListNode(0)
        carry = 0  
        while 1:
            if not l1 and not l2 :
                if carry :
                    l.next = ListNode(carry)
                root = root.next
                return root
            if l1 :
                carry += l1.val
                l1 = l1.next
            if l2:
                carry += l2.val
                l2 = l2.next
            l.next = ListNode(carry % 10)
            carry //= 10
            l = l.next

l1 = ListNode(5)
l2 = ListNode(5)
ll = Solution().addTwoNumbers(l1,l2)
while ll !=None:
    print(ll.val)
    ll = ll.next