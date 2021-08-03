# -*- coding: utf-8 -*-
"""
Created on Sun Aug  1 19:06:52 2021

@author: djvoe


Example setup:

1. generate random list

    generated_list = list_gen(20, 100, 1, 100)

2. ask user what number they would like to find

    user_response = int(input("What number would you like to find? "))
    
3. search list for number
    
    index_of_user_response = search(generated_list, user_response)
    
4. respond to user accordingly
    
    print(respond(index_of_user_response, user_response))
"""

#must import both of these
from random import randint
from math import floor

#generates a new list of unique integers of specified length and number range
def list_gen(min_size, max_size, min_num, max_num):
    i = []
    for x in range(randint(min_size, max_size)):
        i.append(randint(min_num, max_num))
    i = list(set(i))
    i.sort()
    return i

#uses binary search to search for x in list l and returns index of number if found in list
def search(l, x):
    bounds = [0, len(l)-1]  
    done = False
    while done == False:
        if bounds[1]-bounds[0] > 1:
            if l[floor(bounds[0]+(bounds[1]-bounds[0])/2)] > x: bounds[1] = floor(bounds[0]+(bounds[1]-bounds[0])/2)
            elif l[floor(bounds[0]+(bounds[1]-bounds[0])/2)] < x: bounds[0] = floor(bounds[0]+(bounds[1]-bounds[0])/2)
            else:
                index = floor((bounds[0]+(bounds[1]-bounds[0])/2))
                done = True
        else:
            if l[bounds[1]] == x: index = bounds[1]
            elif l[bounds[0]] == x: index = bounds[0]
            else: index = "none"
            done = True
    return index

#returns whether given number was found and the index of the number in the list given
def respond(pos, num):
    if pos == "none": i = str("The number " + str(num) + " is not in the list.")
    else: i = str("The number " + str(num) + " is at position " + str(pos+1)+ " in the list.")
    return i