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

def euclidean_algorithm(x,y,verbose=True):
     """in the euclidean algorithm given 2 values x and y, let m and n be the
     larger and smaller value respectively. there exists a q and r such that
     m=(q x n)+r. Then, so long as n is not 0, m is the previous value for n
     and n is the previous value for r."""
     m= max(x,y)
     n= min(x,y)
     if verbose is True:
         print("Finding the gcd of {} and {} using the euclidean algorithm".format(x,y))
     while n != 0:
        q=m//n
        r=m%n
        if verbose is True:
            print(m , "= (", q, " x ", n, ") + ", r)
        m=n
        n=r
     if verbose is True:
         print ("hence, the gcd is ", m)
     return m

def smallest_linear_solution(x,y,verbose=True):
     """given a linear equation ax+by, the smallest positive solution is equal
     to the gcd(a,b). the following is a way of solving for that value."""
     known_subs={}#this is going to
     m= max(x,y)
     m_1=m
     n= min(x,y)
     n_1=n
     a,b,u,v=sp.symbols('a b u v')
     known_subs[m]=a
     known_subs[n]=b
     if verbose is True:
         print("Finding the smallest possible solution to {}x+{}y".format(x,y))
     while n != 0:
        q=m//n
        r=m%n
        if r is 0:
            m=n
            break
        expr=u-q*v
        expr=expr.subs([(u,known_subs[m]),(v,known_subs[n])])
        known_subs[r]=expr
        if verbose is True:
            print(r , "= ",known_subs[r])
        m=n
        n=r
     if verbose is True:
         print ("hence, the smallest linear solution is: ", known_subs[n], " = ", n)
         print ("where a = ", m_1, " and b = ",n_1)
     if verbose is True:
         check=((known_subs[n]).subs([(a,m_1),(b,n_1)])==m)
         if check is True:
             print("QED")
         else:
             print("oops, something fucked up")

     return known_subs[n],m

def lcm(a,b):
    gcd=euclidean_algorithm(a,b,False)
    m = max(a,b)
    n = min(a,b)
    q=m//gcd
    lcm=q*n
    return lcm

def all_solutions(x,y,expr,g):
    m=max(x,y)
    n=min(x,y)
    a,b,k,u,v=sp.symbols('a b k u v')
    print("finding the first 100 solutions for: ")
    linear_equation=m*a+n*b
    print(linear_equation)
    substitutions={a:k*(n//g),b:k*(m//g)}
    components=expr.args
    print(components)
    solution_form={}
    solution_y=linear_equation
    for expression in components:
        if expression.args[1].name is 'a':
            solution_form['x']=(expression.args[0]+((expression.args[1]).subs(substitutions)))
        elif expression.args[1].name is 'b':
            solution_form['y']=(expression.args[0]-((expression.args[1]).subs(substitutions)))
    print("via the linear equation theorem, all possible solutions can be find via the formulas:")
    print(solution_form['x']," ", solution_form['y'])
    print ("first 100 solution pairs: ")
    for i in range (100):
        #print(linear_equation.subs([(a,solution_form['x'].subs(k,i)),(b,solution_form['y'].subs(k,i))]))
        check=linear_equation.subs([(a,solution_form['x'].subs(k,i)),(b,solution_form['y'].subs(k,i))])==g
        if check is True:
            print("( ", solution_form['x'].subs(k, i)," , ", solution_form['y'].subs(k, i), " )")



if __name__=="__main__":
    sp.init_printing
    """x,y=37,47
    euclidean_algorithm(x,y)
    sls_a,g=smallest_linear_solution(x,y)
    all_solutions(x,y,sls_a,g)
    """
    j=0
    k=0
    m=0
    m_numbers={}
    m_prime_factorizations={}
    m_prime_numbers={}
    while k<1:
         print("what")
         if j not in m_numbers.keys():
             m_numbers[j]=((4*j)+1)
         i=j
         m_prime_factors=[]
         while i != 0:
             if m_numbers[j]%m_numbers[i]==0:
                 if i!=j:
                     m_prime_factors.append(m_numbers[i])
             i-=1
         if not m_prime_factors:
             print("m prime number:")
             print (m_numbers[j])
             m_prime_numbers[m]=m_numbers[j]
             m+=1
         elif len(m_prime_factors)==4:
             print("found it!")
             print(m_prime_factors)
             print(m_numbers[j])
             k+=1;
         else:
             print ("m factorable number: ")
             print (m_numbers[j])
             print (m_prime_factors)
             m_prime_factorizations[m_numbers[j]]=m_prime_factors

         j+=1;
print (m_prime_numbers)
