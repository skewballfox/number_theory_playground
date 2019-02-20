Joshua Ferguson
# HW 4: 7.1, 7.2, 7.6
Exercises 7.1, 7.2, 7.6

7.1. Suppose that gcd(a, b) = 1, and suppose further that a divides the product c. Show that a must divide c.

let
$a,b,c \in Z$
 , the gcd(a,b)=1 and a*b=c,

since the gcd of a and b is 1, Then by the linear equation theorem

 there exist an equation ax+by=1

multiply both sides by c:

axc+byc=c,

a divides axc because a is a factor of axc, and it is also given that a divides bcy because a divides bc,

since c is a sum of axc and byc, and both axc and byc are divisible by a, then as the sum of both numbers it is also divisible by a.

therefore a | c,

  QED

7.2. Suppose that gcd(a, b) = 1, and suppose further that a divides c and that b divides c. Show that the product ab must divide c.

let $a,b,c \in Z$,
since the gcd of a and b is 1, and a|c and b|c then,

if both a and b are 1, then c is 1 and we are done.

if either a or b is greater than 1 then c is greater than 1,

therefore by the fundamental theorem of arithmetic c is a product of exactly 1 factorization of primes.

given a|c and b|c, then a and b exist as a factor of c,

if a or b are prime, then they are part of the prime factorization of c,

if they are not prime, then they exist as a factor of primes.

given that the gcd of a and b is 1 then they have no common prime factors greater than 1. since both a and b are factors of c, and a and b are both either prime or the product of primes, then the factorization of c must include a and b (or their factorization) without overlapping factors.

therefore a*b=c,

QED

7.6 Welcome to M-World, where the only numbers that exist are positive integers that leave a remainder of 1 when divided by 4. In other words, the only M-numbers that exist are
{1,5,9,13,17,21,...}.

(Another description is that these are the numbers of the form At + 1 for t = 0,1, 2, )
In the M-World, we cannot add numbers, but we can multiply them, since if a and b both leave a remainder of 1 when divided by 4 then so does their product. (Do you see why this is true?) We say that m M-divides n if n = mk for some M-number k. And we that say that n is an M-prime if its only M-divisors are 1 and itself. (Of course, we don't consider 1 itself to be an M-prime.)

(a) Find the first six M-primes.

how about I print the first 40?

{0: 1, 1: 5, 2: 9, 3: 13, 4: 17, 5: 21, 6: 29, 7: 33, 8: 37, 9: 41, 10: 49, 11: 53, 12: 57, 13: 61, 14: 69, 15: 73, 16: 77, 17: 89, 18: 93, 19: 97, 20: 101, 21: 109, 22: 113, 23: 121, 24: 129, 25: 133, 26: 137, 27: 141, 28: 149, 29: 157, 30: 161, 31: 173, 32: 177, 33: 181, 34: 193, 35: 197, 36: 201, 37: 209, 38: 213, 39: 217}

(b) Find an M-number n that has two different factorizations as a product of M-primes.

the first number that satisfies this parameter is
225
5*45=9*25=225
