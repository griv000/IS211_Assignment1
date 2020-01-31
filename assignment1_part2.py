#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''Week 1 Assignment Assign 1 Part II ­ Simple Class'''


class Book:
    '''Takes attributes author and title, sets them to object variables,
        prints out a string representing the book.  
    '''

    author=''
    title=''

    def __init__(self,author,title):
        '''Takes in an author and a title, and sets them to the object variables.

        Args:
            author (str): name of author
            title (str): title of book

        Returns:
            None
        '''
        
        self.author=author
        self.title=title

    def display(self):
        '''
        Args:
            None

        Returns:
            Concatenated string.
        '''
        print(self.title+', written by author',self.author)


Book1=Book('John Steinbeck','Of Mice and Men')
Book2=Book('Harper Lee','To Kill a Mockingbird')

Book.display(Book1)
Book.display(Book2)
