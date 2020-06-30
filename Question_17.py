#!/bin/env/usr python

""" Write a Python program to make a chain of function decorators (bold, italic, underline etc.) in Python. """

# Method 1

def make_bold(fn):
    def wrapped():
        return "<b>" + fn() + "</b>"
    return wrapped

def make_italic(fn):
    def wrapped():
        return "<i>" + fn() + "</i>"
    return wrapped

def make_underline(fn):
    def wrapped():
        return "<u>" + fn() + "</u>"
    return wrapped

@make_bold
@make_italic
@make_underline

def hello():
    return "Hello world"
print(hello()) ## returns "<b><i><u>hello world</u></i></b>"