# -*- coding: utf-8 -*-
"""
Created on Fri May 28 13:37:35 2021

@author: Mac_1
"""

import turtle as t
import random as r

for i in range(30):
    length = r.randint(1, 100)
    t.forward(length)
    angle = r.randint(-100, 100)
    t.left(angle)
    
t.done()