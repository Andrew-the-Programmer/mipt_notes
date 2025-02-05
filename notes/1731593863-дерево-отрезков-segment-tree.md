---
id: 1731593863-дерево-отрезков-segment-tree
aliases:
  - дерево отрезков
  - segment tree
tags: []
---

# Дерево отрезков | Segment Tree
# Description
![[1731596142.png]]
![[1731596154.png]]

# Materialization
Heap
\$ - бинарная ассоциативная операция
```python
def FindLeaf(i):
    return i + n - 1
```

# Build
![[1731596165.png]]
$$
O(n)
$$
# Query (запрос)
## Версия 1 (требует коммутативности операции)
![[1731596193.png]]
## Версия 2 (не требует коммутативности операции)
![[1731596229.png]]
```python
def Query(l, r):
    left_ans, right_ans = None
    l = FindLeaf(l)
    r = FindLeaf(r)
    while l < r:
        if l != Left(Parent(l)):
            left_ans = left_ans $ ST[l]
        l = Parent(l + 1)
        if r != Right(Parent(r)):
            right_ans = right_ans $ ST[r]
        r = Parent(r - 1)
    if l = r:
        left_ans $= ST[l]
    return left_ans $ right_ans
```
$$
O(\log n)
$$
## Рекурсивная версия
```python
def Query(l, r, i, a, b):
    if [a,b] not intersect [l,r]:
        return
    if [a,b] subseteq [l,r]:
        return Node(i).value
    lr = Query(l, r, Left(i), a, (a+b) / 2)
    rr = Query(l, r, Right(i), (a+b) / 2, b)
    return lr $ rr
```
![[1731598396.png]]
$$
O(\log n)
$$
# Update element
```python
def Update(i, x):
    i = FindLeaf(i)
    ST[i] = x
    while i != Parent(i): # i is not root
        i = Parent(i)
        ST[i] = ST[Left(i)] $ ST[Right(i)]
```
$$
O(\log n)
$$
# Изменить отрезок | Update range
операция & дистрибутивна по запросу
$$
(a\ \$\ b)\ \&\ c = (a\ \&\ c)\ \$\ (b\ \&\ c)
$$
```python
&(a $ b) = &(a) $ &(b)
```
```python
def Push(i):
    p = node[i].promise
    Left(i).promise *=  p
    Right(i).promise *=  p
    Node(i).value = p(Node(i).value)
    Node(i).promise = None
```
```python
def Query(l, r, i, a, b):
    if [a,b] not intersect [l,r]:
        return
    if [a,b] subseteq [l,r]:
        return Node(i).promise(Node(i).value)
    Push(i) # +
    lr = Query(l, r, Left(i), a, (a+b) / 2)
    rr = Query(l, r, Right(i), (a+b) / 2, b)
    return lr $ rr
```
```python
def Update(l, r, i, a, b, &):
    if [a,b] not intersect [l,r]:
        return
    if [a,b] subseteq [l,r]:
        Node(i).promise *= &
    Push(i)
    Update(l, r, i, Left(i), a, (a+b) / 2, &)
    Update(l, r, i, Right(i), (a+b) / 2, b, &)
    lr = Query(a, (a+b)/2, Left(i), a, (a+b)/2)
    rr = Query((a+b)/2, b, Right(i), (a+b)/2, b)
    Node(i).value = lr $ rr
```
+1 строчка в рекурсивной версии Query
![[1732200612.png]]
![[1732200712.png]]
![[1732200722.png]]

## Examples
\$ = "min"
& = "+n", $n \in \NN$
& = "\*n", $n \in \NN_+$

\$ = "+"
& = "\*n", $n \in \NN$

# Задачи
## Кол-во 0 на $[l, r]$
```python
ST[FindLeaf(i)] = 1 if A[i] = 0 else 0
$ = "+"
```
## Кол-во k на $[l, r]$
```python
ST[FindLeaf(i)] = dict(A[i] = 1)
$ = (x: dict, y: dict):
    res = copy(x)
    for k,v in y.items():
        res[k] = x.get(k, 0) + v
    return res

def Query(l, r, k):
    ...
```

Memory : $O(n \log n)$
