'''
Given a string of digits 2 to 9 a user has pressed on a 
T9 “old school” telephone keypad, return a list of all 
letter combinations they could have been trying to type 
on the keypad.

Example execution 1:  t9_letters("23")  ⇒  
["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"])

Example execution 2:  t9_letters("4663")  ⇒  
["gmmd", …, "gone", …, "good", …, "home", …, "hood", …, "ioof"]
'''

#First define like old school telephone

input = "23"
results = []
lets_to_nums = {
    "2":"abc",
    "3":"def",
    "4":"ghi",
    "5":"jkl",
    "6":"mno",
    "7":"qprs",
    "8":"tuv",
    "9":"wwxyz",
}

def t9_letters()