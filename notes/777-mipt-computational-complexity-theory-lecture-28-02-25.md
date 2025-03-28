---
id: 777-mipt-computational-complexity-theory-lecture-28-02-25
aliases:
  - MIPT computational complexity theory lecture 28-02-25
tags: []
---

# MIPT computational complexity theory lecture 28-02-25

# Hard языки

$$
\Gather{
VertexCover \\
3-Color \\
DHamPath \\
SubsetSum \\
}
$$

# VertexCover

$$
\text{3-CNFSAT} \le VertexCover
$$

$\varphi \to (G,k)$
В $\varphi$ m дизъюнкта, в каждом 3 литерала
В G 3m вершин:

1. одна вершина для каждого литерала
2. литералы в одном дизъюнкте соединены ребром
3. Есть ребро между $x\ и\ \ol{x}\quad \forall x$

$k = 2m$

# Theorem. Ладнера

$$
P \neq NP \implies \exists L : \Cases{
L \in NP \setminus P \\
L \not\in \text{NP-complete} \\
}
$$
## Proof

$H: \NN \to \NN - \textit{не убывает}$
$SAT_H = \set{\left(\varphi, (1^n)^{H(n)}\right) \mid n = \abs{\varphi}, \varphi \in SAT}$
$H \sim const \implies SAT_H \in \text{NP-c}$
$SAT_H \in \text{NP-c} \implies SAT \le SAT_H$
\
$\varphi \to (\psi, m^{H(m)})$
$\abs{\varphi} = n$
$m^{H(m)} \le n^j$ 
$m \le n^{\frac{j}{H(n)}} \le \sqrt{n}$
\
$H(m) \to \infty$
Построим вычислимую за полином $H(m)$:
Пусть $\set{M_i}$ - полиномиальные ДМТ.
Пусть $s_j : \abs{s} < \log{m}$.
```python
S = [s_j for s_j in (0,1)* if len(s_j) < log(m)]

for i = 1 ;; ++i:
    for s_j in S:
        if not s_j in SAT_H: # o(m)
            continue
        res = M(s_j, steps=len(s_j)**log(log(m))
        if res in (-1, 0):
            continue
        # res == 1
        return i
```
Работает за полином.
