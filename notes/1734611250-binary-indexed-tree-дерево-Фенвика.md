---
id: 1734611250-binary-indexed-tree-дерево-Фенвика
aliases:
  - Binary Indexed Tree
  - дерево Фенвика
  - Fenwick Tree
tags: []
---

# Binary Indexed Tree | дерево Фенвика

$b_1 = n, \quad a_i = f(b_i),\quad b_i = a_{i-1} - 1, \quad a_n = 0$
$\sum_{i=0}^{n}{A_i} = \sum_{i=a_1}^{b_1}{A_i} + \dots + \sum_{i=a_n}^{b_n}{A_i}$
$$
f(i) = i\ \&\ (i+1)
$$
зануляет первые подряд идущие 1
Дерево Фенвика позволяет эффективно находить результат произвольной ассоциативной, обратимой и коммутативной операции.
$$
F[k] = \sum_{i = f(k)}^k{A_i}
$$
```python
class BinaryIndexedTree:
    F: list[ValueType] = []

    # ?01...1 -> ?00...0
    def f(i: int) -> int:
        return i & (i + 1) # bitwise AND

    # sum(A[:r+1])
    # O(log n)
    def Query(r: int) -> ValueType:
        s = 0
        for i = r, i >= 0, i = f(i) - 1:
            s += F[i]
        return s
    
    # sum(A[l:r+1])
    # O(log n)
    def Query(l: int, r: int) -> Any:
        return Query(r) - Query(l - 1)

    # O(n)
    def Build(A: list[ValueType]) -> None:
        n: int = len(A)
        P: list[ValueType] = [0] # prefix sums
        for i in range(n):
            P.append(P[i] + A[i])
        for i in range(n):
            F[i] = P[i+1] - P[f(i)]

    # ?01...1 -> ?11...1
    def g(i: int) -> int:
        return i | (i + 1) # bitwise OR

    # A[k] += d
    def Update(k: int, d: ValueType) -> None:
        # S = {i | f(i) <= k <= i}
        # |S| = O(log n)
        for i = k, i < n, i = g(i):
            # коммутативная операция
            # O(log n)
            F[i] += d
            # не коммутативная операция
            # O(log^2(n))
            F[i] = Query(f(i), k) + d + Query(k+1, i)

    # A[:r+1] += d
    # O(n log(n))
    def UpdateRange(l: int, d: ValueType) -> None:
        B: list[ValueType] = [A[0]] + [A[i] - A[i-1] for i in range(1, len(A))]
        B[r] += d # A[:r+1] += d
        C: list[ValueType] = [i * B[i] for i in range(len(B))]
        T1 = BinaryIndexedTree(B)
        T2 = BinaryIndexedTree(C)
        P: list[ValueType] = []
        for i in range(len(A)):
            P.append((i+1) * T1.Query(i) - T2.Query(i))
        for i in range(n):
            F[i] = P[i+1] - P[f(i)]
        

    # A[l:r+1] += d
    def UpdateRange(l: int, r: int, d: ValueType) -> None:
        UpdateRange(l, d)
        UpdateRange(r+1, -d)
```
Коммутативность операции используется в Update.
$$
A_{f(i)} + \dots + A_{k} + d + \dots + A_{i} \neq A_{f(i)} + \dots + A_{i} + d
$$
$$
\sum_{i=0}^{r}{A_i} = \sum_{i=0}^{r}\sum_{j=0}^{i}{B_j} =
\sum_{i=0}^{r}{(r + 1 - i) B_i} =
(r+1) \sum_{i=0}^{r}{B_i} - \sum_{i=0}^{r}{i \cdot B_i}
$$
