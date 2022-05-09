'''
Given two arrays a and b of numbers and a target value t, 
find a number from each array whose sum is closest to t.
Example: a=[9, 13, 1, 8, 12, 4, 0, 5],  b=[3, 17, 4, 14, 6],  t=20  ⇒  
[13, 6] or [4, 17] or [5, 14]
'''

a = [9, 13, 1, 8, 12, 4, 0, 5]
b = [3, 17, 4, 14, 6]

t = 20


def closestPairing(list_one, list_two, target):
    for i in range(len(list_one)):
        for j in range(len(list_two)):
            temp_one = 0
            temp_two = 0
            #need basecase values to begin check
            if abs(list_one[i] + list_two[j] - target) < abs(list_one[temp_one] + list_two[temp_two] - target):
                temp_two = i
                temp_two = j
                #Update our basecase values to test again with next set of values
    print(list_one[temp_one], list_two[temp_two])

closestPairing(a, b, t)