---
id: 680-mipt-differential-equations-seminar-19-02-25
aliases:
  - MIPT differential equations seminar 19-02-25
tags: []
---

# MIPT differential equations seminar 19-02-25

# Photos

![[1739971757.png]]
![[1739971770.png]]
![[1739971778.png]]

# .

$a_k(x) \neq 0$

$$
\sum_{k = 0}^{n}{a_k y^{(n-k)}} = f
$$

**_Вронскиан_**

$$
W_{u_1, \dots, u_n} = \det \Pmatrix{
u_1 & \dots & u_n \\
\vdots & \ddots & \vdots \\
u_1^{(n-1)} & \dots & u_n^{(n-1)}
}
$$

$\set{u_k}$ лин. не зависимы, если

$$
\exists \set{c_k = const}: \sum{c_k^2} \neq 0 \land \sum_{k = 1}^{n}{c_k u_k} = 0
$$

1. $\set{u_k} - ЛЗ \implies W_{u_1, \dots, u_n} \equiv 0$
2. $W_{u_1, \dots, u_n}(x_0) \neq 0 \implies \set{u_k} - ЛНЗ$
3. $W_{u_1, \dots, u_n} \equiv 0 \centernot\implies \set{u_k} - ЛЗ$
   $x^3, \abs{x}^3$

## **_Формула Остроградского-Лаувилла_**

$a_k(x) \neq 0$

$$
\sum_{k = 0}^{n}{a_k y^{(n-k)}} = f
$$

$$
W_{y_1, \dots, y_n}(x) = W_{y_1, \dots, y_n}(x_0)
\exp{-\int_{x_0}^x{\frac{a_1(t)}{a_0(t)}} \d t}
$$

# Задачи

![[1739971170.png]]

# 667

![[1739970280.png]]
![[1739972192.png]]

$$
\AlignLeft{
y_1 = x \\
y_2 = x^5 \\
y_3 = \abs{x^5} \\
x^2 y^{(2)} - 5x y^{(1)} + 5y = 0 \\
(-1, 1)
}
$$

$$
\AlignLeft{
c_1 x + c_2 x^5 + c_3 \abs{x^5} = 0 \\
}
$$

# 668

![[1739970263.png]]
![[1739972367.png]]

# 677

![[1739972304.png]]
![[1739972290.png]]

У доски.
![[1739975667.png]]

![[1739972122.png]]

# 22.47

![[1739971524.png]]
?

# 22.58

![[1739971806.png]]

$$
\AlignLeft{
\sum_{k=0}^{n}{a_k(x) y^{(n-k)}} = f(x) \\
n = 2 \\
y = y_f + y_0 \\
}
$$

![[1739972470.png]]

# 22.59

![[1739972340.png]]
![[1739972662.png]]

# T2

![[1739972715.png]]

$$
\AlignLeft{
W_{y_1,y_2}(x) = W_{y_1,y_2}(x_0) + \exp{-\int_{x_0}^{x}{\frac{a_1(t)}{a_0(t)} \d t}} = W_{y_1,y_2}(x_0) \frac{x_0}{x} \\
W(x) \to \infty, \quad x \to 0 \\
}
$$

![[1739973322.png]]

# Какая-то дичь под конец

![[1739973490.png]]
![[1739973495.png]]
