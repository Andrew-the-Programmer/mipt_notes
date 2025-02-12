---
id: 797-mipt-differential-equations-seminar-12-02-25
aliases:
  - MIPT differential equations seminar 12-02-25
tags: []
---
# MIPT differential equations seminar 12-02-25

# 20.2.4

У доски решал
![[1739384720.png]]

# 20.3.5

$$
\AlignLeft{
J = \int_0^1{(y^2 + 2 {( y^{(1)} )}^{2} + {(y^{(2)})}^{2}) \d x} \\
\sum_{k=0}^{n}{(-1)^k \Dv[k]{x}{F_{y^{(k)}}}} = 0 \\
2y - 4 y^{(2)} + 2 y^{(4)} = 0 \\
y = e^{\alpha x} \\
(\alpha - 1)^2 (\alpha + 1)^2 = 0 \\
\alpha = \pm 1^2 \\
y = C_1 e^x + C_2 e^{-x} + C_3 x e^x + C_4 x e^{-x}
}
$$

![[1739367212.png]]

# 21.7

$$
J = \int_0^1{2xy + (y^{(1)})^2}
$$

$$
\AlignLeft{
y(0) = 0, \quad y(1) = 3 \\
\int_0^1{xy \d x} = 1 \\
}
$$

$$
\AlignLeft{
L = 2xy + (y^{(1)})^2 + \lambda xy \\
L_y = \Dv{x}{L_{y^{(1)}}} \\
k = \frac{2 + \lambda}{2} \\
y = k \frac{x^3}{6} + C_1 x + C_2 \\
\Cases{
C_2 = 0 \\
\frac{k}{6} + C_1 = 3 \\
\int_0^1{xy \d x} = \frac{k}{30} + \frac{C_1}{3} + \frac{C_2}{2} = 1 \\
} \\
k = 0 \\
C_1 = 3 \\
C_2 = 0 \\
\lambda = -2 \\
\D J = \int_0^1{2xh + 2 y^{'} h^{'} + (h^{'})^2} =
\int_0^1{2 y^{'} h^{'} + (h^{'})^2} \le \int_0^1{2 y^{'} h^{'}} =
-\int_0^1{2h y^{''}} = 0 \\
\implies min
}
$$
