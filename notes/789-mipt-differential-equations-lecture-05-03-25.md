---
id: 789-mipt-differential-equations-lecture-05-03-25
aliases:
  - MIPT differential equations lecture 05-03-25
tags: []
---

# MIPT differential equations lecture 05-03-25
$$
\sum_{k=0}^{n}{a_k(x) {y}^{(n-k)}(x)} = f(x)
$$
$$
\Gather{
y_{k+1} = {y}^{(k)}, \quad k = 0,\dots,n \\
\vec{y} = \Pmatrix{
y_1 \\
\dots \\
y_n
} \\
\dv{x}{\vec{y}} = A \vec{y} + \vec{F} \\
A = \Pmatrix{
& E_n & \\
-\frac{a_n}{a_0} & \dots & -\frac{a_1}{a_0}
}, \quad F = \Pmatrix{
0 \\
\dots \\
0 \\
\frac{f(x)}{a_0(x)}
}
}
$$


# Lemma 1.
