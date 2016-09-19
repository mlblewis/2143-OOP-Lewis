"""
Name: Michael Lewis 
Email: mblewis1215@my.mwsu.edu
Assignment: Homework 1 - Lists and Dictionaries
Due: 19 Sep @ 1:00 p.m.
"""
"""
Answers for part A
"""
a = [1, 5, 4, 2, 3] 
print(a[0], a[-1])
# Prints: 1, 3

a[4] = a[2] + a[-2]
Print(a)
# Prints: [1, 5, 4, 2, 6]

print(len(a))
# Prints: 5

print(4 in a)
# Prints: True

a[1] = [a[1], a[0]]
print(a)
# Prints: [1, [5, 1], 4, 2, 3]

"""
Answer for part B
"""

def remove_all(el, lst):
    el = el
    lst = lst
    for x in range(len(lst)):
        if el in lst:
            lst.remove(el)  
        else:
            break
            
"""Removes all instances of el from lst. 
Given: x = [3, 1, 2, 1, 5, 1, 1, 7]
Usage: remove_all(1, x)
Would result in: [3, 2, 5, 7]
"""
#
#
"""
Answer for Part C
"""
def add_this_many(x, y, lst):
    u = len(lst)
    for z in range(u):
        if x in lst:
            lst.append(y)
""" Adds y to the end of lst the number of times x occurs in lst. 
Given: lst = [1, 2, 4, 2, 1]
Usage: add_this_many(1, 5, lst)
Results in: [1, 2, 4, 2, 1, 5, 5]
"""
#
#
"""
Answers for part D
"""
a = [3, 1, 4, 2, 5, 3]
print(a[:4])
# Prints: [3, 1, 4, 2]

print(a)
# Prints: [3, 1, 4, 2, 5, 3]

print(a[1::2])
# Prints: [1, 2, 3]

print(a[:])
# Prints: [3, 1, 4, 2, 5, 3]

print(a[4:2])
# Prints: []

print(a[1:-2])
# Prints: [1, 4, 2]

print(a[::-1])
# Prints: [3, 5, 2, 4, 1, 3]

"""
Answers for part E
"""
def reverse(lst):
    """ Reverses lst in place. 
Given: x = [3, 2, 4, 5, 1] 
Usage: reverse(x)
Results: [1, 5, 4, 2, 3]
"""
    i = 0            # first item
    j = len(lst)-1   # last item
    while i<j:
        lst[i],lst[j] = lst[j],lst[i]
        i += 1
        j -= 1
        
#  I would say the in place method is prefered because no one wants to write 
# this every time they need it like when they try to change the order in an array

"""
Answers for Part F
"""
def rotate(lst, k):
    """ Return a new list, with the same elements of lst, rotated to the right k.
Given: x = [1, 2, 3, 4, 5]
Usage: rotate(x, 3)
Results: [3, 4, 5, 1, 2]
"""
    return lst[k:] + lst[:k]

#
#
#
"""
Answers for part H
not sure what happened to G...but ok
"""
print('colin kaepernick' in superbowls)
#Prints: ??

print(len(superbowls))
#Prints: 4

print(superbowls['peyton manning'] == superbowls['joe montana'])
#Prints: false

superbowls[('eli manning', 'giants')] = 2
print(superbowls)
#Prints: ??

superbowls[3] = 'cat'
print(superbowls)
#Prints: ??


superbowls[('eli manning', 'giants')] =  superbowls['joe montana'] + superbowls['peyton manning']
print(superbowls)
#Prints: ??

superbowls[['steelers', '49ers']] = 11
print(superbowls)
#Prints: ??


"""
Answers part I
"""



