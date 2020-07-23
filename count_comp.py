#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 22 08:55:04 2020

@author: osushi
"""
import time

def main():
    
    n=500000000
    print('{}回'.format(n))
    time_int(n)
    time_str(n)

def time_str(n):
    
    time_sta = time.time() # 時間計測開始
    for i in range(n):
        if 'a' > 'b':
            True
            
    time_end = time.time() # 時間計測終了
    
    tim = time_end- time_sta    
    print('str>>{}'.format(tim))


def time_int(n):
    a=1
    b=2

    time_sta = time.time() # 時間計測開始
    for i in range(n):
        if a > b:
            True 
    
    time_end = time.time() # 時間計測終了
    
    tim = time_end- time_sta
    print('int>>{}'.format(tim))

if __name__=='__main__':
    main()