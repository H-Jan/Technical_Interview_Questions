'''
Given a sorted array of strings, write a recursive function to find 
the index of the first and last occurrence of a target string. 
If the target string is not found in the array, report that.
'''

instructors = ['Adriana', 'Adriana', 'Alan', 'Alan', 'Alan', 'Alan', 
'Alan', 'Braus', 'Braus', 'Braus', 'Braus', 'Dan', 'Dan', 'Dan', 'Dan', 'Dan', 
'Dani', 'Dani', 'Jess', 'Meredith', 'Milad', 'Milad', 'Mitchell', 'Mitchell', 
'Mitchell', 'Mitchell']

#Sample Out: find_indexes(instructors, 'Braus')  ⇒  (7, 10)

def find_indexes(array, name):
    out_array = []
    i = 0
    def recursive_sol(index):
        if array[i] == name:
            out_array.append(i)
        elif array[i] != name:
            i+1
        elif len(out_array)-1 == i:
            return
        i+1
    return find_indexes(array, name)

#recursive loop formed
print(find_indexes(instructors, 'Alan'))
