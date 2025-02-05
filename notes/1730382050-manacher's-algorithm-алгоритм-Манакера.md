---
id: 1730382050-manacher's-algorithm-алгоритм-Манакера
aliases:
  - Manacher's algorithm
  - алгоритм Манакера
tags: []
---

# Manacher's algorithm-алгоритм Манакера
```python
def manaker(s: str) -> List[int]:
    n = len(s)
    p = [0] * n
    right = 0
    left = 0
    for i in range(n):
        if i < right:
            p[i] = min(p[2 * left - i], right - i + 1)
        else:
            p[i] = 1
        while i - p[i] >= 0 and i + p[i] < n and s[i - p[i]] == s[i + p[i]]:
            p[i] += 1
        if i + p[i] - 1 > right:
            right = i + p[i] - 1
            left = i
    return p

def count_palindromes(s: str) -> int:
    n = len(s)
    p_even, p_odd = manaker(s)
    return sum(p_even) + sum(p_odd) + n
```
