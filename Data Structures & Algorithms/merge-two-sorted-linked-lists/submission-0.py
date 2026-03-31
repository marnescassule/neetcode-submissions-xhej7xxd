class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1 or not list2: return list1 or list2
        dummy = ListNode()
        current = dummy
        first_list = list1
        second_list = list2
        
        while first_list and second_list:
            if first_list.val > second_list.val:
                current.next = second_list
                second_list = second_list.next
            else:
                current.next = first_list
                first_list = first_list.next
            current = current.next
        
        current.next = first_list or second_list
        return dummy.next