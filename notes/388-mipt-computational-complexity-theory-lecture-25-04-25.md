---
id: 388-mipt-computational-complexity-theory-lecture-25-04-25
aliases:
  - MIPT computational complexity theory lecture 25-04-25
tags: []
---

# MIPT computational complexity theory lecture 25-04-25

$$
DPath \defeq \set{\group{G, s, t} \mid \textit{G - ориентированный граф, в котором есть путь из s в t}}
$$
Direct Path

# Lemma 1

$$
DPath \in N\mcL
$$

## Proof:

Идея: недетерминированный BFS.
В памяти две вершины - $P_1, P_2$ и счетчик кол-ва вершин в пути $k$.

# Lemma 2

$$
DPath \in \complete{N\mcL}
$$
