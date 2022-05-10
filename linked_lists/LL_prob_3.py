'''
Given an array of k singly-linked lists, each of whose values are in sorted order, 
combine all nodes (do not create new nodes) into one singly-linked list with all 
values in order.
'''

def mergeLists(list_1, list_2):
    head = new_list = node(0)
    #Create a head node to return head of merged list

    while(list_1 and list_2):
        if (list_1.val < list_2.val):
            new_list.next = list_1
            list_1 = list_1.next
        #Compare value of each pointer and put smaller value into merged linked list
        #update pointer
        else:
            new_list.next = list_2
            list_2 = list_2.next
        new_list = new_list.next
        #end of linked list
    new_list.next = list_1 or list_2
    #merging of linked lists
    return head.next