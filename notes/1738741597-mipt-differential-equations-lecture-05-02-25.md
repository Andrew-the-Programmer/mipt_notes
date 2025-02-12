---
id: 1738741597-mipt-differential-equations-05-02-25
aliases:
  - MIPT differential equations lecture 05-02-25
tags: []
---

# MIPT differential equations lecture 05-02-25
# Theorem
$$
\AlignLeft{
\dv{x}{y} = f(x, y(x)) \\
f \in C(G) \\
G\ открыто, \quad G = D \times I, \quad x \in I, \quad y: I \to G \\
\dv{y_j}{f_i} \in C(G)\ \forall i,j \\
\forall x_0, y_0 \in G \hthen \exists \delta > 0 : 
\forall x \in U_\delta(x_0) \exists! y(x)
}
$$
## Proof
$$
\AlignLeft{
f - липшецева \\
\exists L = const > 0 : \\
\forall (x,y_1), (x, y_2) \in \Omega \hthen
\abs{f(x, y_1) - f(x, y_2)} \le L \abs{y_1 - y_2} \\
y(x) = y_0 + \int_{x_0}^{x}{f(z, y(z)) \d z} \\
A y(x) = y_0 + \int_{x_0}^{x}{f(z, y(z)) \d z} \\
A y(x) = y(x) \\
\exists A - сжимающий \\
\varphi_0(x) \defeq y_0 \\
\varphi_k(x) = A \varphi_{k-1}(x) \\
\abs{\varphi_k(x) - y_0} = \abs{\int_{x_0}^{x}{f(z, y(z)) \d z}} \le 
\int_{x_0}^{x}{\abs{f} \d z} \le M \int_{x_0}^{x}{\d z} = M(x - x_0) < R \\
}
$$
## Photos
![[1738743930.png]]
![[1738743938.png]]
![[1738743946.png]]
![[1738743958.png]]
![[1738743966.png]]
![[1738743977.png]]

# Theorem 2 - продолжение решения до границы компакта
$$
\AlignLeft{
\dv{x}{y} = f(x, y) \\
f \in C(B) \\
\dv{y_j}{f_i} \in C(B) \\
\text{Тогда решение на B можно продолжить до }\boundary B \\
}
$$
## Proof
$$
\AlignLeft{
\exists a \in I : (a, y(a)) \in \boundary B \\
\exists b \in I, b > a: (a, y(a)) \in \boundary B \\
\set{(x_k, y_k)} \\
(x_0, y_0) \\
(x_{k+1}, y_{k+1}) = (x_k + \delta_k, y(x_{k+1})) \\
x_k \uparrow\uparrow A \\
y_k \to B = y(A) \\
want\ (A, B) \in \boundary B \\
assume\ (A, B) \not\in \boundary B \\
\forall k > K \hthen \rho(P_k, \boundary B) > \Delta \\
\delta_k = \min{\frac{1}{L+1}, \frac{R_k}{\sqrt{M^2 + 1}}} \to 0 \\
R_k \to 0 \implies \rho(P_k, \boundary B) \to 0 \\
contradiction\\
}
$$
# Непродолжимость решения
$\not\exists \lim_{x \to a} y(x)$
$\exists \lim_{x \to a} y(x) = \pm \infty$
