'''
Given a singly-linked list, rearrange the nodes by interleaving the first half 
of the linked list with the second half.

Example: If the given linked list is A → B → C → D → E, nodes should be 
modified/rearranged so the list becomes E → D → C → B → A.
'''

def rearrange_linked_list(head) -> None:
    if not head and not head.next:
        return

    prev = None
    slow = head
    fast = head

    while fast and fast.next:
        prev = slow
        slow = slow.next
        fast = fast.next.next

    right = reverse(slow) 
    prev.next = None # Unlink
    left = head
    
    while left and right:
        temp = left.next
        left.next = right
        left = left.next
        right = temp