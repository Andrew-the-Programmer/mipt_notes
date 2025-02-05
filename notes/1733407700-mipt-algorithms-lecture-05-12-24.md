---
id: 1733407700-mipt-algorithms-lecture-05-12-24
aliases:
  - MIPT algorithms lecture 05-12-24
tags: []
---

# MIPT algorithms lecture 05-12-24
[[1732809294-cartesion-tree-декартово-дерево|cartesion tree]]
```python
class Node:
    key
    priority
    value
    sum # sum of subtree
    size
```
$RSQ(l,r) = \sum_{key \in \left[l,r\right)}{A[key]}$
```python
def Update(T: Node):
    T.size = T.left.size + T.right.size + 1
    T.sum = T.left.sum + T.right.sum + T.value
```
```python
def Merge(T1: Node, T2: Node):
    if T1 is None:
        return T2
    if T2 is None:
        return T1
    if T1.priority < T2.priority:
        T = Merge(T1.right, T2)
        T1.SetRight(T)
        T1.Update()
        return T1
    else:
        ...
```
```python
def Split(T: Node, x: KeyType):
    if T is None:
        return None
    if T.key < x:
        T1, T2 = Split(T.right, x)
        T.SetRight(T1)
        T.Update()
    else:
        ...
```
```python
def RSQ(T: Node, l: KeyType, r: KeyType) -> ValueType:
    A1, A2 = Split(T, l)
    B1, B2 = Split(A2, r)
    ans = B1.sum
    Merge(A1, Merge(B1, B2))
    return ans
```
# Update
[[1731593863-дерево-отрезков-segment-tree|segment tree]]
```python
def Update(l: KeyType, r: KeyType, action: Callable):
    ...
```
```python
class Node:
    key
    priority
    value
    sum # sum of subtree
    size
    promice: Callable
```
```python
def Sum(T):
    return 0 if T is None else T.promice(T.sum)
```
```python
def ID(x):
    return x

def Push(T: Node):
    p = T.promice
    T.left.promise *=  p
    T.right.promise *=  p
    T.value = p(T.value)
    T.promice = ID
    T.Update
```
```python
def Split(T: Node, x: KeyType):
    if T is None:
        return None
    Push(T)
    ...
```
```python
def Merge(T1: Node, T2: Node):
    if T1 is None:
        return T2
    if T2 is None:
        return T1
    if T1.priority < T2.priority:
        Push(T1)
        ...
    else:
        Push(T2)
        ...
```
```python
def Update(T: Node, l, r, action) -> ValueType:
    A1, A2 = Split(T, l)
    B1, B2 = Split(A2, r)
    T.promice *= p
    Merge(A1, Merge(B1, B2))
    return ans
```
# На массиве
Построим дерево по массиву
Ключи не нужны
Нужен только Node.size
```python
class Node:
    # -: key
    priority
    value
    sum # sum of subtree
    size
    promice: Callable
```
```python
def Get(T, k):
    N = T
    while N is not None:
        if Size(N.left) < k:
            N = N.right
            k -= Size(N.left) + 1
        if Size(N.left) > k:
            N = N.left
        else:
            return N
```
```python
def Split(T: Node, k: int):
    if T is None:
        return None, None
    if Size(T.left) < k: # m
        k -= Size(N.left) + 1 # +
        T1, T2 = Split(T.right, k)
        T.SetRight(T1)
        T.Update()
    else:
        ...
```
## Rotate
$$
\mathrm{Rotate} - O(\log n)
$$
## Reverse
```python
class Node:
    priority
    value
    sum # sum of subtree
    size
    promice: Callable
    reversed: bool # +
```
