---
id: 1730381840-count-palindromes
aliases:
  - count palindromes
tags: []
---

# Count palindromes
[[1730381801-palindrome|palindrome]]

# Algorithms
## 1. $O(n^3)$
```python
def count_palindromes(s: str) -> int:
    n = len(s)
    cnt = 0
    for i in range(n):
        for j in range(i, n):
            if s[i:j+1] == s[i:j+1][::-1]:
                cnt += 1
    return cnt
```

## 2. $O(n^2)$
```python
def count_palindromes(s: str) -> int:
    n = len(s)
    cnt = 0
    for i in range(n):
        for j in range(2): # четная и нечетная длина
            l, r = i, i + j
            while l >= 0 and r < n and s[l] == s[r]:
                cnt += 1
                l -= 1
                r += 1

    return cnt
```

## 3. $O(n)$ [[1730382050-manacher's-algorithm-алгоритм-Манакера|Manacher's algorithm]]

