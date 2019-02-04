import numpy as np
import sympy as sp
import math 
from fractions import Fraction as fr 

known_fibonacci={0:0, 1:1}
known_square = {1:1}
known_triangle = {0:0,1:1,2:3}
known_triangle_and_square = {1:1,2:36}


def nth_fibonacci(n):
    """Originally from Think Python 2. 
    returns the nth fibonacci number
    Uses a dictionary to store know fibonacci
    numbers to exponentially speed up computation"""
    if n in known_fibonacci:
        return known[n]
    
    result = nth_fibonacci(n-1)+nth_fibonacci(n-2)
    known_fibonacci[n] = result
    return result

# Function to demonstrate printing pattern triangle 
def triangle(n): 
    """ripped from geeks for geeks, Using/modding this to
    provide geometric proof of a number being a triangle."""
    # number of spaces 
    k = 2*n - 2
  
    # outer loop to handle number of rows 
    for i in range(0, n): 
      
        # inner loop to handle number spaces 
        # values changing acc. to requirement 
        for j in range(0, k): 
            print(end=" ") 
      
        # decrementing k after each loop 
        k = k - 1
      
        # inner loop to handle number of columns 
        # values changing acc. to outer loop 
        for j in range(0, i+1): 
          
            # printing stars 
            print("* ", end="") 
      
        # ending line after each row 
        print("\r") 
  
def print_triangle_number(n):
    if n in known_triangles.values():
        triangle(n)
    else:
        print ("not a triangle")

def nth_triangle(n):
    """Taking the same strategy as the nth fibonacci
    generates a dictionary of known triangles"""
    if n in known_triangle:
        return known_triangle[n]
    result = n+nth_triangle(n-1)
    known_triangle[n]=result
    return result

def nth_square(n):
    """Taking the same strategy as the nth fibonacci
    generates a dictionary of known squares"""
    if n in known_square:
        return known_square[n]
    result = nth_square(n-1)+(2*(n-1)+1)
    known_square[n]=result
    return result

def nth_triangle_and_square(n):
    """I'll figure this out somehow"""
    if n in known_triangle_and_squares:
        return known[n]
    
    result = nth_fibonacci(n-1)+nth_fibonacci(n-2)
    known_fibonacci[n] = result
    return result

def euclidean_algorithm(x,y):
     m= max(x,y)
     n= min(x,y)
     while n != 0:
        r=m%n
        m=n
        n=r
     return m

if __name__=="__main__":
    nth_triangle(20)
    nth_square(20)
    print ("the first 20 triangles are: ")
    print(sorted(known_triangle.items(), key=lambda x: x[0]))
    print ("the first 20 squares are: ")
    print(sorted(known_square.items(), key=lambda x: x[0]))
