#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul 25 19:15:51 2020

@author: osushi
"""

import time
import numpy as np

def main():
    n = 20
    bef_list = make_list(n)
    aft_list = [s for s in bef_list]
    #bef_list = ['zzz', 'aa', 'aabbb', 'biij', 'mooji', 'mo', 'zkocj', 'zz', 'a', 'b']
    aft_list = [s for s in bef_list]
    #time_sta = time.time() # 時間計測開始    
    aft_list = QuickSort(aft_list)
    #time_end = time.time() # 時間計測終了
    #tim = time_end- time_sta
    #print('timecount>>{}s'.format(tim))
    output_list(bef_list, aft_list)
    return

# クイックソートする
def QuickSort(namelist):
    left = 0
    right = len(namelist) - 1
    if right - left <=0:
        return namelist
    
    pivot_index = (right - left)//2
    pivot = namelist[pivot_index]
    namelist[pivot_index], namelist[right] = namelist[right], namelist[pivot_index]
    
    i = left
    for j in range(left, right):
        l = min(len(namelist[j]), len(pivot))
        if (namelist[j][:l] < pivot[:l]) or (namelist[j][:l] == pivot[:l] and len(namelist[j]) < len(pivot)):
            namelist[i], namelist[j] = namelist[j], namelist[i]
            i += 1
    
    namelist[i], namelist[right] = namelist[right], namelist[i]
    
    namelist[:i] = QuickSort(namelist[:i])
    namelist[i+1:] = QuickSort(namelist[i+1:])
    
    return namelist
    
    
# とにかく名前をいっぱいつくる
def make_list(n):
    namelist = []
    for i in range(n):
        len_name = np.random.randint(3, 7)
        num_list = np.random.randint(97, 123, (len_name))
        new_name = ''.join([chr(i) for i in num_list])
        namelist.append(new_name)
    return namelist

def output_list(list1, list2):
    print('<before>         <after>')
    for i in range(len(list1)):
        space1 = ' '*(len(str(len(list1)+1)) - len(str(i+1))+1)
        space2 = ' '*(11-len(list1[i]))
        print('({}){}{}{}({}){}{}'.format(i+1, space1, list1[i], space2, i+1, space1, list2[i]))
    return

if __name__=='__main__':
    main()
