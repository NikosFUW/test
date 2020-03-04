#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def silnia(n):
    if n>1:
        return n * silnia(n-1)
    else:
        return 1
    
def silnia2(n):
    wynik = 1
    for i in range(1,n+1):
        wynik *= n
    return wynik