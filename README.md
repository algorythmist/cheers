# Cheers

---

## Problem statement


In this party, every one has to clink glasses with everyone else. 
Only three glasses can be clinked simultaneously.
What is the minimum number of clinks for a company of n guests.

### Recursive Solution

Assume n guests can achieve this in f(n) clinks. When a new guest arrives, 
they have to clink glasses with everyone else. 
This can be done if the other guests pair up and cheers the new guest two at a time.
Therefore

$$
f(n+1) = \lceil n/2\rceil + f(n)
$$

It is possible to write this as a system of difference equations for even numbers and odd numbers:

$$
o(n+1) = n/2 + e(n)
$$

$$
e(n) = n/2 + o(n-1)
$$

and combining them obtain a second order  

$$
f(n+1) = n +f(n-1)
$$

Using the initial conditions $$f(3) = 1$$, $$f(4) = 3$$, this can be solved explicitly:

$$
f(n) = (2n^2-1+(-1)^n)/8 - 1
$$
