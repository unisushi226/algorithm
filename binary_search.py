#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jul 19 17:25:22 2020

@author: osushi

二分探索

参考URL< https://codezine.jp/article/detail/9900?p=2 >

1.1　128個の名前が含まれたソート済みのリストがあり、
二分探索を使って名前を探しているとしよう。ステップ数は最大でいくつになるか。

1.2　このリストのサイズを2倍にした場合、ステップ数は最大でいくつになるか。


---------------------------------------------
リストの要素数 n が、（1）を満たすときステップ数は k である。
(1) 2^k <= n 2^(k+1), k:正の整数
---------------------------------------------


"""
import bubble_sort as bb


def main():
    n =129
    l, ans = bubble_binary(n)
    print(ans)
    for i in range(n):
        space = ' '*(len(str(len(l)+1)) - len(str(i+1))+1)
        print('{}{}{}'.format(i+1, space, l[i]))
    
    return

def bubble_binary(n):
    l = bb.make_list(n)
    l = bb.bubblesort(l)
    ans = binary_search(l, 'binary')
    return l, ans

def binary_search(list, item):
    step = 0
    low = 0                        # lowとhighを使ってリストの検索部分を追跡
    high = len(list) - 1
    while low <= high:             # 1つの要素に絞り込まれるまでの間は...
        step += 1
        mid = (low + high) // 2
        guess = list[mid]          # 真ん中の要素を調べる
        if guess == item:          # アイテムを検出
            return [mid, step]
        if guess > item:           # 推測した数字が大きすぎた
            high = mid - 1
        else:                      # 推測した数字が小さすぎた
            low = mid + 1
    return [None, step]                    # アイテムが存在しない


if __name__=='__main__':
    main()
