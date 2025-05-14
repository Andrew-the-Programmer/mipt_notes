---
id: 992-mipt-differential-equations-seminar-14-05-25
aliases:
  - MIPT differential equations seminar 14-05-25
tags: []
---

# MIPT differential equations seminar 14-05-25

# 17.84

Уравнение в частных производных (ЧП)

![14-05-25_15-37-23_006.png](assets/imgs/14-05-25_15-37-23_006.png)
![14-05-25_15-37-04_262.png](assets/imgs/14-05-25_15-37-04_262.png)

$$
\Gather{
(x - 2 x^2 y) \pdv{x}{u} + y \pdv{y}{u} + 2 x^2 z^2 \pdv{z}{u} = 0 \\
u = y^2 z, \quad x - y = 0
}
$$

$\Align{
\Cases{
\dot{x} = x - 2x^2 y \\
\dot{y} = y \\
\dot{z} = 2x^2 z^2
} \\
\Cases{
x \neq 2 x^2 y \\
y \neq 0 \\
2 x^2 z^2 \neq 0
} \\
\frac{\d x}{x - 2 x^2 y} = \frac{\d y}{y} = \frac{\d z}{2 x^2 z^2} \\
\hline
\frac{\d x}{x (1 - 2 x y)} = \frac{\d (xy)}{2 xy (1 - xy)} =
\group{\frac{1}{2xy} + \frac{1}{2 - 2xy}} \d (xy) \\
2 \ln\abs{y} = \ln\abs{xy} - \ln\abs{1 - xy} + c \\
u_1 = \frac{y}{x} - y^2 \\
\hline
x = \frac{y}{u_1 + y} \\
\dots \\
u_2 = \frac{1}{z} - \frac{x}{y} \\
\hline
u = f(\frac{y}{x} - y^2, \frac{1}{z} - \frac{x}{y}) \in C^1 \\
\Cases{
x - y = 0 \\
u_1 = \frac{y}{x} - y^2 \\
u_2 = \frac{1}{z} - \frac{x}{y}
} \\
\Cases{
u_1 = 1 - y^2 \\
u_2 = \frac{1}{z} - 1
}
}$
