#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import time

def zmierz(f, n=100):
    t0 = time.time()
    
    w = f(n)
    
    t1 = time.time()
    return t1 - t0