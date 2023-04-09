# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
from typing import Optional
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # 片方が0 or 両方が場合
        if list1 is None:
            return list2
        elif list2 is None:
            return list1
        
        merge = ListNode()
        cur = merge
        while list1 is not None and list2 is not None:
            if list1.val > list2.val:
                cur.next = list2
                list2 = list2.next
            else:
                cur.next = list1
                list1 = list1.next
            cur = cur.next

            if list1 is None:
                cur.next = list2
                return merge.next
            elif list2 is None:
                cur.next = list1
                return merge.next
        return merge.next