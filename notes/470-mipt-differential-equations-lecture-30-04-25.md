---
id: 470-mipt-differential-equations-lecture-30-04-25
aliases:
  - MIPT differential equations lecture 30-04-25
tags: []
---

# MIPT differential equations lecture 30-04-25

# Пример 1

$$
\group{1 + \sqrt{u - x - y}} \pdv{x}{u} + \pdv{y}{u} = 2
$$

$\Align{
V = V(x,y,u) = 0 \\
\textit{ЛДУ в ЧП}: \\
\group{1 + \sqrt{u - x - y}} \pdv{x}{V} + \pdv{y}{V} + 2 \pdv{u}{V} = 0 \\
\textit{Характеристическая система в форме Коши}: \\
\Cases{
\dot{x} = 1 + \sqrt{u - x - y} \\
\dot{y} = 1 \\
\dot(u) = 2
} \\
\frac{\d x}{1 + \sqrt{u - x - y}} = \d y = \frac{\d u}{2} \\
V_1 = 2y - u \\
\d y = \frac{\d u - \d y - \d x}{2 - 1 - \group{1 + \sqrt{u - x - y}}} =
-\frac{\d (u - y - x)}{\sqrt{u - x - y}} \\
V_2 = y + 2 \sqrt{u - x - y} \\
V = V(x,y,u) = F(V_1, V_2) = 0 \\
\textit{Специальное решение (нельзя получить из ур-ия)}: \\
u = x + y \\
}$

# Пример 2

$$
\sin y \cdot u_x + e^y \cdot u_y = 2x u^2 \sin y
$$

$\Align{
V = V(x,y,u) = 0 \\
\textit{ЛДУ в ЧП}: \\
\sin y \cdot \pdv{x}{V} + e^y \cdot \pdv{y}{V} + 2x u^2 \sin y \pdv{u}{V} = 0 \\
\textit{Характеристическая система в форме Коши}: \\
\Cases{
\dot{x} = \sin y \\
\dot{y} = e^y \\
\dot(u) = 2x u^2 \sin y
}\\
\frac{\d x}{\sin y} = \frac{\d y}{e^y} = \frac{\d u}{2x u^2 \sin y} \\

}$
