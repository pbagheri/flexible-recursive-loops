# -*- coding: utf-8 -*-
"""
Created on Tue Dec 19 15:21:15 2017

@author: Payam
"""

def loop_rec(y):
    if y > 1:
        for x in range(y):
            print(y, x)
            loop_rec(y-1)
            

y=2, x=0
y=1, x=0
y=2, x=1
y=1, x=0

a = 1
for b in range(a):
    print(a, b)


y=3, x=0 (x=0,1,2)
y=2, x=0 (x=0,1)
y=1, x=0
y=2, x=1
y=1, x=0
y=3, x=1
y=2, x=0
y=1, x=0
y=2, x=1
y=1, x=0
y=3, x=2
y=2, x=0
y=1, x=0
y=2, x=1
y=1, x=0

y=3, x=0 
y=2, x=0
y=2, x=1
y=3, x=1
y=2, x=0
y=2, x=1
y=3, x=2
y=2, x=0
y=2, x=1

         

loop_rec(3)

   
    
def loop_rec(y, n):
    if n >= 1:
        for x in range(y):
            loop_rec(y, n - 1)
            print('A', n)
    else:
       print('B', n)

loop_rec(3, 2)

  


def fac(n):
    print(n)
    return 1 if (n < 1) else n * fac(n-1)

fac(6)


def fib(n,x):
    return x if n < x else n + fib(n-2,x)

fib(1,2)
fib(2,1)
fib(4,3)
fib(7,6)
fib(9,8)
fib(1,0)
fib(2,1)
fib(24,23)
