#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jul 19 19:47:19 2020

@author: osushi

バブルソート
要素の数をnとすると、 n(n - 1)/2 回のスキャンが必要
要素数が少ない簡単なリストで用いることが好ましいアルゴリズム
というか使い道なさそう
他のソートの基礎的な扱い？
"""
import time
import numpy as np

def main():
    bef_list = make_list(200)
    
    aft_list = [s for s in bef_list]
    #time_sta = time.time() # 時間計測開始    
    aft_list = bubblesort(aft_list)
    #time_end = time.time() # 時間計測終了
    #tim = time_end- time_sta
    #print('timecount>>{}s'.format(tim))
    output_list(bef_list, aft_list)
    return

# バブルソートする
def bubblesort(namelist):
    for i in range(len(namelist)-1):
        for j in range(len(namelist)-1):
            n_j = namelist[j]
            n_j1 = namelist[j+1]
            l = min(len(n_j), len(n_j1))
            
            if (n_j[:l] > n_j1[:l]) or (n_j[:l] == n_j1[:l] and len(n_j) > len(n_j1)):
                namelist[j], namelist[j+1] = namelist[j+1], namelist[j]
                
        
    
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
        space2 = ' '*(10-len(list1[i]))
        print('({}){}{} {}({}){}{}'.format(i+1, space1, list1[i], space2, i+1, space1, list2[i]))
    return

if __name__=='__main__':
    main()