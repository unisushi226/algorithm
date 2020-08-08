#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 28 09:04:58 2020

@author: osushi
"""
import time
import numpy as np

def main():
    n = 20
    bef_list = make_list(n)
    aft_list = [s for s in bef_list]
    
    #time_sta = time.time() # 時間計測開始
    k=1    
    aft_list = MargeSort(aft_list, k)
    #time_end = time.time() # 時間計測終了
    #tim = time_end- time_sta
    #print('timecount>>{}s'.format(tim))
    output_list(bef_list, aft_list)

    return

# マージソートする
def MargeSort(namelist, k):
    size = len(namelist)
    mid = size // 2
    #print(k)
    k += 1
    if size > 1:
        
        
        left_list = MargeSort(namelist[:mid], k)
        right_list = MargeSort(namelist[mid:], k)
        
        #print(left_list)
        #print(right_list)
        namelist = []
        while len(left_list) != 0 and len(right_list) != 0:
         
            l = min(len(left_list[0]), len(right_list[0]))
                
            if (left_list[0][:l] < right_list[0][:l]) or (left_list[0][:l] == right_list[0][:l] and len(left_list[0]) < len(right_list[0])):
                namelist.append(left_list.pop(0))           
            else:
                namelist.append(right_list.pop(0)) 
        
        # left, right のいずれかが空になったときに、残ってる方をそのまま全部追加
        # 残ってる部分は、既にソート済み？⇒left, right　双方の中ではソート済み
        if len(left_list) != 0:
            namelist.extend(left_list)
        elif len(right_list) != 0:
            namelist.extend(right_list)
                
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


