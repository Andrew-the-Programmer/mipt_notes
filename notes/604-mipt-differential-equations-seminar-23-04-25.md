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
\boxed{\pdv{\mu}{x} \rvert_{\mu=0} = \frac{(1 - t) - \ln\abs{1 - t}}{(1 - t)^2}} \\
}$

# 17.45

![23-04-25_16-25-57_323.png](assets/imgs/23-04-25_16-25-57_323.png)
![23-04-25_16-25-40_189.png](assets/imgs/23-04-25_16-25-40_189.png)

$\Align{
\Cases{
\dot{x} = xz \tg z \\
\dot{y} = y - x \\
\dot{z} = -z
} \\
\frac{\d x}{xz \tg z} = \frac{\d y}{y - x} = \frac{\d z}{-z} \\
\circled{1} x,z \\
\frac{\d x}{x} = -\d z \tg z \\
\boxed{u_1 = \frac{x}{\cos z}} \\
\circled{2} y,z \\
\frac{\d (zy)}{xz} = \frac{\d z}{z} \\
x = \cos(z) c_1 \\
\boxed{u_2 = zy - x \tg z} \\
u = F(u_1, u_2) \in C^1 \\
\Cases{
u_1 \\
u_2 \\
x = yz
} \\
u = \cos z - \sin z = \frac{u_2}{u_1} \\
\boxed{u = (zy - x \tg z) \frac{\cos z}{x}}
}$

# 17.79

![23-04-25_16-25-57_323.png](assets/imgs/23-04-25_16-25-57_323.png)
![23-04-25_16-35-39_078.png](assets/imgs/23-04-25_16-35-39_078.png)

$\Align{
\Cases{
\dot{x} = 2xy \\
\dot{y} = 1 - y^2 - 2xz \\
\dot{z} = -\frac{y}{x}
} \\
\frac{\d x}{2xy} = \frac{\d y}{1 - y^2 - 2xz} = \frac{\d z}{-\frac{y}{x}} \\
\circled{1}\ x,z \\
\boxed{u_1 = \frac{1}{2x} - z} \\
\textit{тяжело...}\\
\boxed{u_2 = y^2 x - \frac{x}{2} + x^2 z} \\
\Cases{
u_1 \\
u_2\\
y^2 + xz = 1 \\
} \\
u_2 = \frac{x}{2} \\
u = \frac{1}{2} - y^2 = \frac{1}{2} - 1 + xz = -1 + x u_1 - 4 z u_2 \\
}$
