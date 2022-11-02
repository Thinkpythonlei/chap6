# -*- coding: utf-8 -*-
"""
Created on Mon Oct 31 19:27:14 2022

@author: Surface
"""

def b( z ) :
    prod = a (z , z )
    print (z , prod )
    return prod
def a(x , y ) :
    x = x + 1
    return x * y
def c(x , y , z ) :
    total = x + y + z
    square = b ( total ) **2
    return square
x = 1
y = x + 1
print (c (x , y +3 , x + y ) )

#规律就是第一个数等于输入的X数字乘以二再加上5，第二个数字等于第一个数字乘以自身加一的数字
#第三个数字为第二个数字的平方



def ack(m,n):
    if m==0:
        return n+1
    elif m>0 and n==0:
        return ack(m-1,1)
    elif m>0 and n>0:
        return ack (m-1,ack(m,n-1))

print(ack(3,4))





def first ( word ) :
    return word [0]   
def last ( word ) :
    return word[-1]
def middle ( word ) :
    return word [1:-1]


print(a,middle("ab"))




def is_palindrome(word):
    if len(word)<2:
        return True
    if first(word)==last(word) and is_palinderome(middle(word)):
        return True
    else:
        return False
    
    
    
    
def is_power(a,b):
    if a ==1:
        return True
    if a%b==0 and is_power(a//b,b):
        return True
    else:
        return False
print(is_power(9,3))
    




def gcd(a,b):
    if b==0:
        return a
    else:
        return gcd(b,a%b)
    
    
print(gcd(5,3))
        
    






























