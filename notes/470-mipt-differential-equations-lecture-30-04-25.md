---
id: 470-mipt-differential-equations-lecture-30-04-25
aliases:
  - MIPT differential equations lecture 30-04-25
tags: []
---

# MIPT differential equations lecture 30-04-25

![1.jpg](assets/imgs/30-04-25_11-31-35_645_IMG_20250430_104921.jpg)
![2.jpg](assets/imgs/30-04-25_11-31-35_801_IMG_20250430_105439.jpg)
![3.jpg](assets/imgs/30-04-25_11-31-35_271_IMG_20250430_110131.jpg)

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
V = V(x,y,u) = F(V_1, V_2) \in C^1 \\
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
\textit{Хар. сист. в форме Коши}: \\
\Cases{
\dot{x} = \sin y \\
\dot{y} = e^y \\
\dot(u) = 2x u^2 \sin y
}\\
\frac{\d x}{\sin y} = \frac{\d y}{e^y} = \frac{\d u}{2x u^2 \sin y} \\
e^x \d x = \sin y \d y \\
V_1 = e^x + \cos y \\
V_2 = x^2 + \frac{1}{u} \\
V(x,y,u) = F(V_1, V_2) \in C^1 \\
}$

# Пример 3

$$
y u_x - x u_y = 0
$$

1. Способ 1

$\Align{
u_1 = x^2 + y^2 \\
u = F(x^2 + y^2) \in C^1
}$

2. Квазилинейный способ

$\Align{
y V_x - x V_y + 0 \cdot V_u = 0 \\
u_1 = x^2 + y^2 \\
u_2 = u \\
V = F(u_1, u_2) \in C^1 \\
}$

Тот же результат, но больше действий и мы не можем быть уверены, что не потеряли решений.

# Пример 4 - Ур-ие Хопфа

$$
u_t + u u_x = 0
$$

решить самим

# Зависимость решения ЗК от параметров и начальных условий

$$
\dv{x}{\vec{y}} = f(x,\vec{y})
$$

# Theorem

# Lemma. Об интегральном представлении

ЗК $\same$

$$
\vec{y}(x) = \vec{{y}_{0}} + \int_{x_0}^{x}{f(\xi, \vec{y}(\xi)) \d \xi}
$$

# Lemma. Гронуолла (о дифф. неравенстве)

## If:

$\varphi(x) \ge 0$
$\exists A,B \ge 0: \varphi(x) \le A + B \abs{\int_{x_0}^{x}{\varphi(\xi) \d \xi}}$

## Then:

$\varphi(x) \le A e^{B \abs{x - x_0}}$

# ЗК с параметром

$$
\Cases{
\dv{x}{\vec{y}} = \vec{f}(x, \vec{y}, \vec{\mu}) \\
\vec{y}(x_0) = \vec{{y}_{0}}(\vec{\mu})
}
$$

Ур-ие эволюции ошибки
