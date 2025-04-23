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
\sum_{k=0}^{n}{f_k(\vec{x}) \pdv{x_k}{u}} = 0 \hspace{1cm} (1)
$$

$f_k \in C^1$
$\sum f_k^2 \neq 0$
$u \in C^1$
$\veccross{f}{\grad u} = 0$

Характеристическая система

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

1. метод выделения, интегрирование
$\Align{
1) \\

}$
