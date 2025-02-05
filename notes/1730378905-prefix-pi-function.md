---
id: 1730378905-prefix-pi-function
aliases:
  - prefix-function
  - pi-function
tags: []
---

# prefix-pi function
# Definition
$$
\pi(S, i) = \Cases{
0 & i = 0 \\
\max{\left\{k \le i \mid S[0, k] = S[i + 1 - k, i + 1]\right\}}
& i > 0
}
$$

# Algorithms

## 1. $O(S^3)$
```python
def PrefixFunction(S):
    p = [0,...,0]
    for i from 1 to |S| - 1: # O(S)
        for k from i downto 1: # O(S)
            if S[0...k-1] == S[i-k+1...i]: # O(S)
                p[i] = k
                break
    return p
```

## 2. $O(S)$
![[1730379539.png]]

$\pi(i) \le \pi(i - 1) + 1$

```python
def PrefixFunction(S):
    p = [0,...,0]
    for i from 1 to |S| - 1:
        k = p[i - 1]
        while S[i] != S[k] and k > 0:
            k = p[k - 1]
        if S[i] == S[k]:
            p[i] = k + 1
    return p
```
