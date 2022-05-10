'''
Rotate a given singly-linked list counter-clockwise by k nodes, 
where k is a given integer.
'''
#original, individual solution
def originalRotatingLL(head, k):
    for i in range(k)
        start = 0
        node = head.next 
        current = current.next 
        #jump to the next node head 
        node = current
        current.next = None
        return node


#Colaborated solution
def rotatingLL(head, k):
    for i in range(k)
        node = head.next
        temp_head = head.next
        head.next = None
        while node.next != None:
            node = node.next
            node.next = head
            head = temp_head
    print(temp_head)