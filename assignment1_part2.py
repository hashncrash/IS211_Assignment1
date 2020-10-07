#!/usr/bin/env python
# -*- coding: utf-8 -*-
"IS 211 Assignment 1, part 2. Dave Soto"


class Book(object):
    author = " "
    title = " "

"Book Class information"
    def __init__(self, author, title):

        self.author = author
        self.title = title

"Function to dsiplay the book author and title"
    def display(self):

        bookinfo = '"{}, written by {}"'.format(self.title, self.author)
        print bookinfo

BOOK_1 = Book('John Steinbeck', 'Of Mice and Men')

BOOK_2 = Book('Harper Lee', 'To Kill a Mockingbird')

BOOK_1.display()
BOOK_2.display()
