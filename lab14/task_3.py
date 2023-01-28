"""
Check for balanced parentheses
Given an expression string, write a python program to find whether a given string has balanced parentheses or not.
Input : {[]{()}}
Output : Balanced
Input : [{}{}(]
Output : Unbalanced
Input : {][{()}}
Output : Unbalanced
"""
open_list = ["[","{","("]
close_list = ["]","}",")"]
  
open_symbols = ["[","{","("]
close_symbols = ["]","}",")"]


def check_balanced(symbols: list)-> str:
    stack = []
    for el in symbols:
        if el in open_symbols:
            stack.append(el)
        elif el in close_symbols:
            close_elem = close_symbols.index(el)
            if ((len(stack) > 0) and
                (open_symbols[close_elem] == stack[len(stack)-1])):
                stack.pop()
            else:
                return "Unbalanced"
    if len(stack) == 0:
        return "Balanced"
    else:
        return "Unbalanced"
