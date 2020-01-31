#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''Week 1 Assignment Part 1 ­ Functions and Exceptions'''

def listDivide(numbers=[],divide=2):
    '''Returns the number of elements in the numbers list that are divisible by divide.

    Args:
        numbers (list): list of numbers to check.
        divide (int): number to divide with.

    Returns:
        The number of elements in the numbers list that are divisible by divide.
    '''
    
    x = 0
    for listitem in numbers:
        if listitem % divide == 0:
            x += 1
    return x


class ListDivideException(Exception):
    '''Class for other exceptions'''   
    pass


def testListDivide():
    '''Prints from function listDivide with sample values.

    Args:
        None

    Returns:
        None
    '''
        
    print(listDivide([1,2,3,4,5]))
    print(listDivide([2,4,6,8,10]))
    print(listDivide([30, 54,63,98,100], divide=10))
    print(listDivide([]))
    print(listDivide([1,2,3,4,5],1))  

testListDivide()
