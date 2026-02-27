class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        s, c = 0, 0
        rs = []

        # Continue while either list has nodes
        while l1 is not None or l2 is not None:
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0

            s = v1 + v2 + c          # include carry in sum
            c = s // 10              # correct carry calculation
            s = s % 10               # remainder is the digit to store

            rs.append(s)

            if l1: l1 = l1.next
            if l2: l2 = l2.next

        # if carry remains after the last addition
        if c > 0:
            rs.append(c)

        # Now, build linked list from rs instead of joining strings
        dummy = ListNode(0)
        cur = dummy
        for num in rs:
            cur.next = ListNode(num)
            cur = cur.next

        return dummy.next
