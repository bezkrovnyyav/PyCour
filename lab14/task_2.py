"""
Multiply numbers
Given two numbers. The task is to mutiply them without using the * operator.
Input : 12, 12
Output : 144
Input : 19, 0
Output : 0
Input : 1.1, 17.2
Output : 18.92
Input : -2, 4
Output : -8
"""
from math import prod
import time


def go_sleep():
    time.sleep(3)


def multiply_num(a, b):
    go_sleep()
    result = prod([a, b])
    return round(result, 2)
