'''
Given a singly-linked list and an integer k, 
find the value in the kth-to-last node.
'''

def kth_last_node(k, head):
    i = 0
    kth_to_last = head
    while(head and head.next):
        head = head.next
        if i == k-1:
            kth_to_last = kth_to_last.next
        else:
            i += 1
    return kth_to_last
