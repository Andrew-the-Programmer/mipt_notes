---
id: 117-mipt-differential-equations-lecture-23-04-25
aliases:
  - MIPT differential equations lecture 23-04-25
tags: []
---

# MIPT differential equations lecture 23-04-25

# ЛДУ в ЧП 1 порядка

(линейные дифференциальные уравнения в частных производных 1-ого порядка)

$$
\begin{equation}
\sum_{k=0}^{n}{f_k(\vec{x}) \pdv{x_k}{u}} = 0
\end{equation}
$$

$f_k \in C^1$
$\sum f_k^2 \neq 0$
$u \in C^1$
$\veccross{f}{\grad u} = 0$

# Характеристическая система

$$
\dot{x} = f(x) \hspace{1cm} (2)
$$

Фазовые траектории - "характеристики" (1)

$\exists (n-1)$ ф.н. ПИ $\set{u_i}_{i=1}^{n-1}$
Общее решение

$$
u(x) = F(u_1(x), \ldots, u_{n-1}(x))
$$

$F \in C^1$

# Методы нахождения ПИ

# Метод дробей

$$
\frac{\d x_1}{f_1(x)} = \dots = \frac{\d x_{n}}{f_{n}(x)} \hspace{1cm} (3)
$$

В общем случае:

$$
(2) \nsim (3)
$$

# Claim

$$
\Gather{
f_i \neq 0 \\
\implies\\
(2) \sim (3)
}
$$

## Шаги

1. Метод выделения, интегрирование
2.
3. Метод дробей
4. Использование уже найденного ПИ.
   $\Align{
u_1(x_1,\dots,x_n) = c_1 \\
\implies x_n = \psi(x_1, \dots, x_{n-1}, c_1) \\
\dot{{x}_{k}} = f_k(x_1, \dots, x_n) = {f}_{k}^{'}(x_1, \dots, x_{n-1}, c_1) \\
}$
   Понизили порядок

## Пример. C 17.46

$$
(xy - x^2) \pdv{x}{u} + y^2 \pdv{y}{u} + (e^{\frac{y}{x}} + yz) \pdv{z}{u} = 0
$$

$\Align{
\Cases{
\dot{x} = xy - x^2 \\
\dot{y} = y^2 \\
\dot{z} = e^{\frac{y}{x}} + yz
} \\
\frac{\d x}{xy - x^2} = \frac{\d y}{y^2} = \frac{\d z}{e^{\frac{y}{x}} + yz} \\
\circled{1} \\
-y^2 \d x = xy \d y - x^2 \d y \\
\circled{2} \\
\frac{\d x}{xy - x^2} = \frac{\d y}{y^2} \\
\frac{y \d x}{xy^2 - x^2 y} = \frac{x \d y}{x y^2} \\
\d \group{\frac{y}{x}} = \d \ln\abs{y} \\
\boxed{u_1 = \frac{e^{\frac{y}{x}}}{y}} \\
\circled{3} \\
\frac{\d z}{c_1 y + yz} = \frac{\d y}{y^2} \\
\boxed{u_2 = \frac{e^{\frac{y}{x}} + zy}{y^2}} \\
\textit{Общее решение}: \\
u(x,y,z) = F(u_1, u_2) \in C^1 \\
\\
}$
