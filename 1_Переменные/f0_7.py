#  -*- coding: utf-8 -*-
from math import *

x = 10   # горизонтальное положение
y = 10   # вертикальное положение

angle = x+sin(y/x)
angle1 = sin(y/x)/pi+cos(x)
print("s=",angle1*180) 