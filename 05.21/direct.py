# -*- coding: utf-8 -*-
"""
Created on Fri May 21 14:42:26 2021

@author: Mac_1
"""

import turtle as t

t.width(3)
t.shape("turtle")
t.shapesize(3,3)

while True:
    command = t.textinput("방향결정", "l나 r일력")
if command == "l":
        t.left(90)
        t.forward(100)
if command == "r":
        t.left(90)
        t.forward(100)
