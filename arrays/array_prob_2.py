'''
Two Sum II - Input Array Is Sorted. 

Given a 1-indexed array of integer numbers that are already sorted in non-decreasing 
order, find two numbers such that they add up to a specific target number. 
Let these two numbers be numbers[index1] and numbers[index2] where 1 <= index1 < index2 <= numbers. 
'''

# a is our 1-indexed array of integer numbers, sorted
# t is our target number
a = [3, 5, 7, 12]
target = 10

def twoSumTwo(nums, t):
    head = 0
    tail = len(nums) - 1
    while head < tail:
        summation= nums[head] + nums[tail]
        if summation > t:
            tail -= 1
        #while the head of the list at 0 is less than the tail, or decreasing value of the list index
        # if the total of those two values is greater than our target
        #we decrease by a factor of 1
        elif summation < t:
            head += 1
        #If the summation of the two values is less than our target
        # We increase by a factor of one
        else:
            return [head, tail]
        # if neither above cases are true, we achieve our target value

print(twoSumTwo(a, target))

#Note - solution returns the index value in our list. In this case, the returned value of [0,2]
#refers to values 3 and 7, which equate to 10

