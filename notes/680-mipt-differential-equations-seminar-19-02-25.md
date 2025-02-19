---
id: 680-mipt-differential-equations-seminar-19-02-25
aliases:
  - MIPT differential equations seminar 19-02-25
tags: []
---

# MIPT differential equations seminar 19-02-25
$$
\sum_{k = 1}^{n}{a_k y^{(n-k)}} = f
$$
***Вронскиан***
$$
W_{u_1, \dots, u_n} = \det \Pmatrix{
u_1 & \dots & u_n \\
\dots & \ddots & \vdots \\
u_1^{(n-1)} & \dots & u_n^{(n-1)}
}
$$
$\set{u_k}$ лин. не зависимы, если
 $$
\exists \set{c_k = const}: \sum{c_k^2} \neq 0 \land \sum_{k = 1}^{n}{c_k u_k} = 0
$$
1. $\set{u_k} - ЛЗ \implies W_{u_1, \dots, u_n} = 0$ 
2. $W_{u_1, \dots, u_n}(x_0) \neq 0 \implies \set{u_k} - ЛНЗ$ 
3. $W_{u_1, \dots, u_n}(x_0) = 0 \not\implies \set{u_k} - ЛЗ$
