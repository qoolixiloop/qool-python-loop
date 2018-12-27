#-*- coding: utf-8 -*-
# PCL 1 Tutorat 09 Demo Code
# Author: Cazim Hysi
# cazim dot hysi at uzh dot ch
# 03.12.2015

import operator as op
import functools as ft

class IntVector(object):
    """
    Class representing a vector of positive integers.
    This version is implemented in a more "functional" style.
    
    You can compare it with the more standard version to see a few alternative
    ways to do things in Python -- especially recommended for everyone who
    used operator.itemgetter in previous exercises ;)

    If you're interested, feel free to read the Python docs on the topic.
    Be warned that this is comparatively esoteric and won't help you
    for the exam, so don't do that unless you have free capacities.
    """

    def __init__(self, start, end):
        """
        Initializer method.
        Creates a private list spanning the positive integers from start to end
        via list comprehension.

        Raises:
            Exception: if any of the arguments passed are negative or end 
                       is less than start
        """
        if start < 0 or end < 0:
            raise Exception("IntVector object cannot contain a negative value")
        elif end < start:
            raise Exception("IntVector object can only contain a sequence "
            "of ascending numbers")
        self._lst = range(start, end+1)

    def __len__(self):
        """
        Implements the len() builtin. Returns the length of the internal list.
        """
        return len(self._lst)
    
    def __add__(self, val):
        """
        Implements the + operator. The semantics of add for IntVector, Integer
        are:
            extend the IntVector by Integer elements
        """
        # slightly less convenient implementation to demonstrate the fact
        #   that in Python, you can also map functions that have no
        #   sensible return value... and methods!
        #   
        #   Haskell hackers please forgive me
        map(self._lst.append, (i for i in xrange(self.last+1, self.last+val+1)))

    def __sub__(self, val):
        """
        Implements the - operator. This truncates the list by val elements,
        removing them from the end
        """
        if val >= len(self._lst):
            self._lst = [0]
        else:
            self._lst = self._lst[:-val]

    def __rshift__(self, val):
        """
        Implements the >> operator. This shifts the entire vector right on the
        number line, which in practice means adding val to every element.

        Raises:
            Exception: if val < 0
        """
        if val < 0:
            raise Exception("Shift operand must be 0 or greater")
        else:
            # functools.partial creates a partially applied function
            # so we go from operator.add(a, b) -> a + b
            # to a function (b) -> a + b
            # that takes an argument and adds a to it
            # operator.add is just + in function form
            self._lst = map(ft.partial(op.add, val), self._lst)

    def __lshift__(self, val):
        """
        Implements the << operator. This shifts the entire vector left
        on the number line, which in practice means subtracting val from 
        every element.

        Raises:
            Exception: if val < 0
        """
        if val < 0:
            raise Exception("Shift operand must be 0 or greater")
        elif val > self._lst[0]:
            raise Exception("Cannot shift first element below zero")
        else:
            # same story as >>
            # can you figure out why I didn't map op.sub instead?
            self._lst = map(ft.partial(op.add, -(val)), self._lst)

    def __repr__(self):
        return "IntVector({}, {})".format(self.first, self.last)

    def __str__(self):
        return self._lst.__str__()

    def __iter__(self):
        """
        Implements for loops over the IntVector.

        Returns:
            a generator over all elements of the internal list.
        """
        return (i for i in self._lst)

    # @property is fancy syntax for disguising a method as an attribute
    # we need this because first and last can change
    # but they should feel like attributes

    @property
    def first(self):
        """
        Implements the attribute self.first

        Returns:
            the current start of the IntVector
        """
        return self._lst[0]

    @property
    def last(self):
        """
        Implements the attribute self.last

        Returns:
            the current end of the IntVector
        """
        return self._lst[len(self._lst)-1]
