# -*- coding: utf-8 -*-
"""
Created on Fri May 21 14:52:57 2021

@author: Mac_1
"""

import turtle as t
t.shape("turtle")
while True:
    
    s = t.textinput("","도형을 입력하세요:")
    t.reset()
    if s == "사각형":
        sw = t.textinput("","가로")
        w = int(sw)
        sh = t.textinput("","세로")
        h = int(sh)
        t.forward(w)
        t.left(90)
        t.forward(h)
        t.left(90)
        t.forward(w)
        t.left(90)
        t.forward(h)
        
    elif s == "삼각형":
        sl= t.textinput("","길이를 입력하세여요")
        l = int(sl)
        t.forwardl(l)
        t.left(120)
        t.forwardl(l)
        t.left(120)
        t.forwardl(l)
        t.left(120)
        
    elif s == "원":
        sr= t.textinput("","반지름을 입력하세요")
        r = int(sr)
        t.circle(r)
    else:
        t.write("사각형","삼각형","원중에 입력하세요")
    
