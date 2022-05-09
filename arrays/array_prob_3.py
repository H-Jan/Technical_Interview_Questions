'''
Given an array a of n numbers and a count k find the k largest values in the array a.
Example: a=[5, 1, 3, 6, 8, 2, 4, 7], k=3  ⇒  [6, 8, 7]
''' 

a = [5, 1, 3, 6, 8, 2, 4, 7]
k_element = 3

def kLargestElements (list, k):
    sorted_list = list.sort()
    start = len(list)
    stop = len(list) - k
    step = -1
    #We are sorting our list and then iterating backwards from the endpoint of our 
    # list to the endpoint - k of our list, which should "separate" out desired values
    for i in range(start, stop, step):
        print(i)

kLargestElements(a, k_element)



