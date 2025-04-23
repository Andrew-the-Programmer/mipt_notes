---
id: 604-mipt-differential-equations-seminar-23-04-25
aliases:
  - MIPT differential equations seminar 23-04-25
tags: []
---

# MIPT differential equations seminar 23-04-25

# Ф 1064

![23-04-25_15-47-25_439.png](assets/imgs/23-04-25_15-47-25_439.png)

$\Align{
\circled{1} \\
\textit{Вырожденное ДУ}: \mu \equiv 0 \\
\boxed{y = e^x} \\
\circled{2} \\
\pdv{\mu}{y} \defeq u(x,\mu) \\
\textit{Ур-ие в вариациях}: \\
\Cases{
u_x = u + x + ysr + 2 \mu y u \\
u \rvert_{x=0} = 0
} \\
\mu \equiv 0 \implies\\
u_x = u + x + y^2 = u + x + e^{2x} \\
\implies \\
u = - x - 1 + e^{2x} \\
\textit{Ассимптотические ряды} \\
y(x,\mu) = y(x,0) + \mu \pdv{\mu}{y}(x,0) + \frac{\mu^2}{2} \pdv[2]{\mu}{y}(x,0) + o(\mu^2) \\
y(x,\mu) = \sum_{i\in\NN_0}{\mu^i y_i(x)} \\
\Cases{
{y}_{0}^{'} + \mu {y}_{1}^{'} = y_0 + \mu y_1 + \mu(x + y_0^2) + o(\mu) \\
y_0(0) + \mu y_1(0) = 1 \\
} \\
\Cases{
{y}_{0}^{'} = y_0 \\
y_0(0) = 1
},\quad
\Cases{
{y}_{1}^{'} = y_1 + x + {y}_{0}^{2} \\
y_1(0) = 0
} \\
}$

![1.jpg](assets/imgs/23-04-25_16-13-27_606_IMG_20250423_155710.jpg)
![2.jpg](assets/imgs/23-04-25_16-13-27_113_IMG_20250423_155714.jpg)
![3.jpg](assets/imgs/23-04-25_16-13-27_888_IMG_20250423_155718.jpg)

# Ф 1068

![23-04-25_16-02-43_759.png](assets/imgs/23-04-25_16-02-43_759.png)
![23-04-25_16-02-26_429.png](assets/imgs/23-04-25_16-02-26_429.png)

$\Align{
y = y_0 + \mu y_1 \\
\Cases{
{y}_{0}^{'} = y_0^2 \\
y_0(0) = 1
} \\
\boxed{y_0 = \frac{1}{1 - x}} \\
\Cases{
{y}_{0}^{'} + \mu y_1^{'} = y_0^2 + 2 \mu y_0 y_1 + \mu x y_0^3 + o(\mu) \\
y_0(0) + \mu y_1(0) = 1 + \mu \\
} \\
\mu = 0 \\
\Cases{
{y}_{1}^{'} = 2 y_0 y_1 + x y_0^3 \\
y_1(0) = 1
} \\
\boxed{y_1 = \frac{(1 - x) - \ln\abs{1 - x}}{(1 - x)^2}} \\
}$
