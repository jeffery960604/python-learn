#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 31 13:55:36 2026

@author: xiang
"""
# 無回傳值無參數值的函數
def greeting():
    print('Python歡迎你')
    print('謝謝')
    
# 有回傳值有參數值的函數
def plus(x1,x2):    # x1, x2 參數值
    y = x1 + x2   
    return y        # y 回傳值

# print(plus(3,5))

# 多回傳值有參數值的函數
def add_mul(x1,x2):    # x1, x2 參數值
    y1 = x1 + x2
    y2 = x1*x2
    return y1 , y2       # y1 y2回傳值

z1,z2 = add_mul(3,5)
print(z1)
print(z2)



