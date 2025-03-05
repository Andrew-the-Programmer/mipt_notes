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
![98676.png](assets/imgs/98676.png)

# Lemma 1.
![98976875.png](assets/imgs/98976875.png)
![9865543.png](assets/imgs/9865543.png)

# Lemma 2.
![9865543.png](assets/imgs/9865543.png)

# Lemma 3. (Правило дифференцирования детерминанта)
![3457454.png](assets/imgs/3457454.png)

# Theorem 1. Формула Лиувилля-Остроградского.
$$
\dv{x}{\vec{y}} = A \vec{y}, \quad A = (a_{ij}(x))
$$
