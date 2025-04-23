---
id: 117-mipt-differential-equations-lecture-23-04-25
aliases:
  - MIPT differential equations lecture 23-04-25
tags: []
---

# MIPT differential equations lecture 23-04-25

# Photos

![1.jpg](assets/imgs/23-04-25_12-26-40_125_IMG_20250423_105807.jpg)
![2.jpg](assets/imgs/23-04-25_12-26-40_626_IMG_20250423_105810.jpg)
![3.jpg](assets/imgs/23-04-25_12-26-40_482_IMG_20250423_105813.jpg)
![4.jpg](assets/imgs/23-04-25_12-26-40_772_IMG_20250423_110054.jpg)
![5.jpg](assets/imgs/23-04-25_12-26-40_747_IMG_20250423_111644.jpg)
![6.jpg](assets/imgs/23-04-25_12-26-40_875_IMG_20250423_111647.jpg)
![7.jpg](assets/imgs/23-04-25_12-26-40_150_IMG_20250423_112536.jpg)
![9.jpg](assets/imgs/23-04-25_12-26-40_641_IMG_20250423_112540.jpg)
![10.jpg](assets/imgs/23-04-25_12-26-40_600_IMG_20250423_114508.jpg)
![11.jpg](assets/imgs/23-04-25_12-26-40_179_IMG_20250423_114511.jpg)
![12.jpg](assets/imgs/23-04-25_12-26-40_991_IMG_20250423_114515.jpg)
![13.jpg](assets/imgs/23-04-25_12-26-40_468_IMG_20250423_115355.jpg)
![14.jpg](assets/imgs/23-04-25_12-26-40_261_IMG_20250423_120653.jpg)
![15.jpg](assets/imgs/23-04-25_12-26-40_467_IMG_20250423_120657.jpg)
![17.jpg](assets/imgs/23-04-25_12-26-40_799_IMG_20250423_121021.jpg)
![19.jpg](assets/imgs/23-04-25_12-26-40_760_IMG_20250423_121028.jpg)

# ЛДУ в ЧП 1 порядка

(линейные дифференциальные уравнения в частных производных 1-ого порядка)

$$
\sum_{k=0}^{n}{f_k(\vec{x}) \pdv{x_k}{u}} = 0
\tag{1}
$$

$f_k \in C^1$
$\sum f_k^2 \neq 0$
$u \in C^1$
$\veccross{f}{\grad u} = 0$

# Характеристическая система

$$
\dot{x} = f(x)
\tag{2}
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
\frac{\d x_1}{f_1(x)} = \dots = \frac{\d x_{n}}{f_{n}(x)}
\tag{3}
$$

В общем случае:

$$
\eqref{2} \nsim \eqref{3}
$$

# Claim

$$
\Gather{
f_k \neq 0 \\
\implies\\
\eqref{2} \sim \eqref{3}
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

# Характеристическая точка

1. $x \in D$
2. $g: D \to R$
3. $\Cases{
g \in C^1\\
\grad g \neq 0
} - \textit{гладкая}$
4. $S \defeq \set{x \in D \mid g(x) = 0}$

$b \in S$ называется **_характеристической_**, если

$$
\veccross{f}{\grad g} \rvert_{x=b} = 0
$$

# Задача Коши

$$
\Cases{
\sum_{k=1}^{n}{f_k \pdv{x_k}{u}} = 0 \\
u(x) \rvert_S = v(x)
}
$$

# Theorem

## If:

$b$ - не характеристическая точка

## Then:

В некоторой окр. т $b$ $\exists!$ решение ЗК

# Пример. C 17.46

# Def. Квазилинейные ДУ в ЧП 1 порядка

$$
\Cases{
\sum_{k=1}^{n}{f_k(x_1, \dots, x_n, u) \pdv{x_k}{u}} = f(x_1, \dots, x_n, u) \\
f_k \neq 0 \\
f_k, f, u \in C^1
}
$$

# Нахождение решений

Решение в виде: $V(x_1,\dots,x_n, u) = 0$
$\Align{
\dv{x_k}{V} = \pdv{x_k}{V} + \pdv{u}{V} \pdv{x_k}{u} = 0 \\
\pdv{x_k}{u} = - \frac{\pdv{x_k}{V}}{\pdv{u}{V}} \\
\sum_{k=1}^{n}{f_k \pdv{x_k}{V}} + f \pdv{u}{V} = 0 -
\textit{ЛДУ в ЧП 1 порядка ранга n} \\
\textit{Общее решение}: \\
V = F(V_1())
}$
