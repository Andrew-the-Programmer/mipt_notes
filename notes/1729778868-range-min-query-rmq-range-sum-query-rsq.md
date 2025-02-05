---
id: 1729778868-range-min-query-rmq-range-sum-query-rsq
aliases:
  - Range Min Query-RMQ Range Sum Query-RSQ
tags: []
---

# Range Min Query-RMQ Range Sum Query-RSQ
Массив A.
$$
RMQ(l,r) \ldefeq Min(A[l:r+1])
$$
$$
RSQ(l,r) \ldefeq Sum(A[l:r+1])
$$

## Static / Dynamic

## Свойства операций
+
1. ассоциативность
2. коммутативность
3. обративмость

Min
1. ассоциативность
2. коммутативность
3. идемпотентность

## Static RSQ
Массив префиксных сумм.
$p[k] = \sum_{i=0}^{k}{A_i} = \cases{A_0 & k = 0\\p[k-1] + A_k & k > 0}$ 
$p - O(n)$
$RSQ(l,r) = p[r] - p[l-1]$ 
$RSQ - O(1)$

## Static RMQ
$T_1$ - Build
$T_2$ - Query

### 1. [[1729779553-sqrt-декомпозиция|sqrt-декомпозиция]]
$$
\aligncenter{
T_1 = O(n)\\
T_2 = O(\sqrt n)
}
$$
### 2.
$$
\aligncenter{
T_1 = O(n^2)\\
T_2 = O(1)
}
$$
```python
B[i][k] = Min(A[i:i+k])
RMQ(l,r) = B[l][r-l+1]
```
$B - O(n^2)$
$RMQ - O(1)$ 

### 3. Sparse Table
$$
\aligncenter{
T_1 = O(n \log n)\\
T_2 = O(1)
}
$$
```python
ST[i][k] = Min(A[i:i+2^k])
k = floor(log2(r-l+1))
RMQ(l,r) = Min(ST[l][k], ST[r + 1 - 2^k][k])
```
$ST - O(n \log{n})$
$RMQ - O(1)$ 

```python
ST[i][0] = A[i]
ST[i][k+1] = Min(ST[i][k], ST[i + 2^k][k])
```
```python
for i in range(0, n):
    ST[i][0] = A[i]
for k in range(0, log2(n)):
    for i in range(0, n):
        ST[i][k+1] = Min(ST[i][k], ST[i + 2^k][k])
```

### 4. Sqrt-декомпозиция $\times$ Spase Table
1. Построим массив B.
2. Построить spase table ST по массиву B.

$RMQ(l,r) =$

Предпроцессинг: $T_1 = O(n + \frac{n}{b} \log{\frac{n}{b}})$
Запрос: $T_2 = O(1 + b)$ 

$b = \log{n} \implies$
$$
\aligncenter{
T_1 = O(n)\\
T_2 = O(\log{n})
}
$$

### 5. Sqrt-декомпозиция $\times$ Spase Table $(v2)$
1. Построим массив B из $Min(B_i)$.
2. ST на B и ST на $B_i$

$T_1 = O(n + \frac{n}{b} \log{\frac{n}{b}} + n \log{b})$
$T_2 = O(1)$
$b = \log{n} \implies$
$$
\aligncenter{
T_1 = O(n \log\log n)\\
T_2 = O(1)
}
$$
