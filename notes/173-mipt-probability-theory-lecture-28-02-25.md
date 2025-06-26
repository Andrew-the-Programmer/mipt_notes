---
id: 173-mipt-probability-theory-lecture-28-02-25
aliases:
  - MIPT probability theory lecture 28-02-25
tags: []
---

# MIPT probability theory lecture 28-02-25

# Независимость классов мн-в

$$
\Gather{
\set{\set{A_j^n}_{j=1}^{J_n\in\NN}}_{n=1}^{N\in\NN} \\
P\left(\bigcap_{n=1}^{N}{\bigcup_{k=1}^{J_n}{A_k^n}}\right) =
\prod_{n=1}^{N}{P\left(\bigcup_{k=1}^{J_n}{A_k^n}\right)}
}
$$

## Lecture photos

![[1740735021.png]]

# Theorem.

# Lemma. Бореля-Кантелли

## If:

$$
A = \bigcap_{m \in \NN}{\bigcup_{n \ge m}{A_n}}
$$

## Then:

1. $\sum{P(A_n)} < \infty \implies P(A) = 0$
2. $\sum{P(A_n)} = \infty \land \set{A_n} \dash \text{\textit{совместно независимы}} \implies P(B) = 1$
