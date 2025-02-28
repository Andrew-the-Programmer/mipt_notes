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
1) одна вершина для каждого литерала
2) литералы в одном дизъюнкте соединены ребром
3) Есть ребро между $x\ и\ \ol{x}\quad \forall x$

$k = 2m$
