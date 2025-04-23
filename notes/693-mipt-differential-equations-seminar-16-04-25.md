---
id: 693-mipt-differential-equations-seminar-16-04-25
aliases:
  - MIPT differential equations seminar 16-04-25
tags: []
---

# MIPT differential equations seminar 16-04-25

![16-04-25_15-49-51_672.png](assets/imgs/16-04-25_15-49-51_672.png)

# 17.4

![16-04-25_15-51-00_229.png](assets/imgs/16-04-25_15-51-00_229.png)
![16-04-25_15-51-13_894.png](assets/imgs/16-04-25_15-51-13_894.png)

$\Align{
\Cases{
\dot{x} = x^2 + z^2 \\
\dot{y} = 2(xy - xz^3) \\
\dot{z} = 2xz
} \\
(1)\ и\ (2) \\
\frac{\d x}{x^2 + z^2} = \frac{\d y}{2(xy - xz^3)} = \frac{\d z}{2xz} \\
\frac{\d (x+z)}{(x+z)^2} = \frac{\d (x-z)}{(x-z)^2} \\
\frac{1}{x + z} = \frac{1}{x - z} + C \\
u_1 = \frac{z}{x^2 + z^2} \\
(2)\ и\ (3) \\
\frac{\d y}{y - z^3} = \frac{\d z}{z} = \frac{\d (z^3)}{3 z^3} \\
u_2 = \frac{z}{2y + z^3} \\
\textit{Общее решение:} \\
u = F(u_1, u_2) - ПИ \\
F \in C^1 \\
\textit{Решение ЗК:} \\
\Cases{
u_1 = \frac{z}{x^2 + z^2} \\
u_2 = \frac{z}{2y + z^3} \\
x^2 - z^2 = 2
} \\
u = \frac{u_1 u_2^2 - 8}{2 u_2^2}
}$

# T4

![16-04-25_16-25-32_714.png](assets/imgs/16-04-25_16-25-32_714.png)

$\Align{
\Cases{
\dot{x} = 2 \\
\dot{y} = 3
} \\
u = 3x - 2y \\
\textit{Общее решение:}\quad f(3x - 2y) \in C^1 \\
a)\quad u = \alpha (3x - 2y) - (\alpha - 2) 5 \\
б)\quad \textit{Нет решений} \\
в)\quad u = \sin\group{y - \frac{3}{2} x}
}$

# T5

![16-04-25_16-34-34_238.png](assets/imgs/16-04-25_16-34-34_238.png)

$\Align{
}$

# 17.16

![16-04-25_15-51-00_229.png](assets/imgs/16-04-25_15-51-00_229.png)
![16-04-25_16-47-54_629.png](assets/imgs/16-04-25_16-47-54_629.png)

$\Align{
u_1 = x + y + z \\
u_2 = \frac{3y - x - z}{z^2} \\
x = 3y,\quad u = \frac{4y}{z} \implies \\
u = -1 - u_1 u_2
}$
