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
f(n+1) = ceil(n/2) + f(n)
$$