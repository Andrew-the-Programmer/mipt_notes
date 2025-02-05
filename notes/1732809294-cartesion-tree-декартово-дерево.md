---
id: 1732809294-cartesion-tree-декартово-дерево
aliases:
  - декартово дерево
  - cartesion tree
tags: []
---

# Cartesion Tree | Декартово дерево

# Definition
![[1732803980.png]]
![[1732803987.png]]

BST с ограничением:
$$
T.y \ge T.parent.y
$$

# Theorem
$d(x)$ - глубина
![[1732803992.png]]
![[1732804087.png]]
![[1732804606.png]]

# Merge
![[1732806141.png]]
$$
\mathrm{Keys}(T_1) < \mathrm{Keys}(T_2)
$$
```python
# <T> = O(log n)
# T_bad = O(n + m)
def Merge(T1: Node, T2: Node) -> Node:
    if T1 is None:
        return T2
    if T2 is None:
        return T1
    if T1.y < T2.y:
        T1.SetRight(Merge(T1.right, T2))
        return T1
    else:
        T2.SetLeft(Merge(T1, T2.left))
        return T2
```

# Split
![[1732806151.png]]
```python
# <T> = O(log n)
# T_bad = O(n)
def Split(T: Node, x0: Xtype) -> (Node, Node):
    if T is None:
        return None, None
    x = T.x
    if x < x0:
        A, B = Split(T.right, x0)
        T.SetRight(A)
        B.parent = None
        return T, B
    else:
        A, B = Split(T.left, x0)
        T.SetLeft(B)
        A.parent = None
        return A, T
```
# Insert
```python
def Insert(T: Node, (x, y): tuple(Xtype, Ytype)) -> Node:
    new_node = Node(x, y)
    A, B = Split(T, x)
    A = Merge(A, new_node)
    return Merge(A, B)
```
# Erase
```python
def Erase(T: Node, N: Node) -> Node:
    x = N.x
    A, B = Split(T, x)
    C, D = Split(B, UpperBound(x))
    return Merge(A, D)
```
# Build
$$
\mathrm{Build} : \set{(x_i, y_i)} \to CT
$$
## 1 (Insert)
```python
# T_bad = O(n^2)
for node in {(x_i, y_i)}:
    T = Insert(T, node)

```
## 2 (Merge)
```python
# T_bad = O(n log(n))
def Build(nodes: list[Node]) -> Node:
    nodes = sorted(nodes, key=lambda node: return node.x)
    while len(nodes) > 1:
        n = len(nodes)
        last = nodes[-1]
        nodes = [
            Merge(nodes[2*i], nodes[2*i+1])
            for i in range(0, n // 2)
        ]
        if n % 2 == 1:
            nodes.append(last)
    return nodes[0]
```
## 3
```python
# T_bad = O(n)
def Build(nodes: list[Node]) -> Node:
    nodes = sorted(nodes, key=lambda node: return node.x)
    root = None
    last = None
    for new in nodes:
        node = last
        while node is not None and node.y > new.y:
            node = node.parent
        if node is None:
            last = root = new
        else: # node.y <= new.y
            new.SetLeft(node.right)
            node.SetRight(new)
            last = new
```
