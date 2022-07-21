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

Using the initial conditions $f(3) = 1$, $f(4) = 3$, this can be solved explicitly:

$$
f(n) = (2n^2-1+(-1)^n)/8 - 1
$$

### First Few Values

| Guests | Clinks |
| --- | --- |
| 3 | 1 |
| 4 | 3 |
| 5 | 5 |
| 6 | 8 |
| 7 | 11 |
| 8 | 15 |
| 9 | 19 |
| 10 | 24 |
| 11 | 29 |
| 12 | 35 |


### Powers of Ten

An interesting patterns arises for powers of 10

| Guests | Clinks |
| --- | --- |
| 10 | 24 |
| 100 | 2499 |
| 1000 | 249999 |
| 10000 | 24999999 |
| 100000 | 2499999999 |
| 1000000 | 249999999999 |
| 10000000 | 24999999999999 |
| 100000000 | 2499999999999999 |
| 1000000000 | 249999999999999999 |


