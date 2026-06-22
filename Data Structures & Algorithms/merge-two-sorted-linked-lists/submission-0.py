# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        merged_list = current = ListNode()
        while list1 and list2:
            print(f"current val: {current.val} - current next: {current.next.val if current.next else None}")
            print(f"merged_list val: {merged_list.val} - merged_list next: {merged_list.next.val if merged_list.next else None}")
            if list1.val < list2.val:
                current.next = list1
                list1 = list1.next
            else:
                current.next = list2
                list2 = list2.next
            current = current.next
        
        current.next = list1 or list2
        
        return merged_list.next

