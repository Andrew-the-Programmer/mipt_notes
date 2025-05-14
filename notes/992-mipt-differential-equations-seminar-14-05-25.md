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
} \\
\boxed{u = \frac{1 - u_1}{1 + u_2} = \frac{1 - \frac{y}{x} + y^2}{1 + \frac{1}{z} - \frac{x}{y}}}
}$

# 11.55

![14-05-25_15-53-13_776.png](assets/imgs/14-05-25_15-53-13_776.png)
![14-05-25_15-52-56_429.png](assets/imgs/14-05-25_15-52-56_429.png)

$$
\Cases{
\dot{x} = x + 2z \\
\dot{y} = 2x - y + 2z \\
\dot{z} = x - y + z
}
$$

$\Align{
\textit{Линеаризованная система}: \dot{r} = A r \\
A = \Matrix{
1 & 0 & 2 \\
2 & -1 & 2 \\
1 & -1 & 1
} \\
\textit{Ищем собственные значения}:
\det (A - \lambda E) = (1 - \lambda) (\lambda^2 - 1) \\
\lambda_{1,2} = 1, \lambda_{3} = -1 \\
h_1 \same \lambda_{1,2} = 1 \\
(A - \lambda_1 E) h_1 = 0 \\
h_1 = \Matrix{
1 \\ 1 \\ 0
} \\
A h_2 = h_1 \\
h_2 = \Matrix{
0 \\ 0 \\ \frac{1}{2}
} \\
h_3 \same \lambda_3 = -1 \\
h_3 = \Matrix{
-1 \\ 1 \\ 1
} \\
r = C_1 e^t h_1 + C_2 e^t \groupr{t h_1 + h_2} + C_3 e^{-t} h_3 \\
\boxed{
\Matrix{
x \\ y \\ z
} = C_1 e^t \Matrix{
1 \\ 1 \\ 0
} + C_2 e^t \groupr{
t \cdot \Matrix{
1 \\ 1 \\ 0
} + \Matrix{
0 \\ 0 \\ \frac{1}{2}
}} + C_3 e^{-t} \Matrix{
-1 \\ 1 \\ 1
}}
}$

# 13.49

![14-05-25_16-07-02_268.png](assets/imgs/14-05-25_16-07-02_268.png)
![14-05-25_16-06-45_512.png](assets/imgs/14-05-25_16-06-45_512.png)

$$
\Cases{
\dot{x} = 2 - 2 \sqrt{1 + x + y} \\
\dot{y} = \exp{\frac{5}{4} x + 2y + y^2} - 1
}
$$

$\Align{
\textit{ПР}: \dot{r} = 0 \\
(x*0, y_0) = \group{0, 0} \\
\textit{Линеаризованная система}: \dot{r} \approx A r \\
A = \Matrix{
P_x & P_y \\
Q_x & Q_y
} \rvert*{(x_0,y_0)} = \Matrix{
-1 & -1 \\
\frac{5}{4} & 2
} \\
\textit{Ищем собственные значения}: \\
\det (A - \lambda E) = (\lambda - \frac{3}{2}) (\lambda + \frac{1}{2}) \\
\lambda_1 = \frac{3}{2},\quad \lambda_2 = -\frac{1}{2} \\
h_1 = \Matrix{
2 \\ -5
} \\
h_2 = \Matrix{
2 \\ -1
} \\
\textit{Неустойчивое седло}. \\
}$
![14-05-25_16-34-19_391_IMG_20250514_162432.jpg](assets/imgs/14-05-25_16-34-19_391_IMG_20250514_162432.jpg)
$\Align{
(x_0, y_0) = \group{\frac{3}{4}, -\frac{3}{4}} \\
\textit{Линеаризованная система}: \dot{r} \approx A r \\
A = \Matrix{
-1 & -1 \\
\frac{5}{4} & \frac{1}{2}
} \\
\textit{Ищем собственные значения}: \\
\det (A - \lambda E) = \lambda^2 + \frac{1}{2} \lambda + \frac{3}{4} \\
\lambda_1 = -\frac{1}{4} \pm \frac{i}{4} \sqrt{11} \\
\textit{Устойчивый фокус}. \\
}$
![14-05-25_16-36-11_650_IMG_20250514_163450.jpg](assets/imgs/14-05-25_16-36-11_650_IMG_20250514_163450.jpg)

# 20.1.8

![14-05-25_16-40-11_272.png](assets/imgs/14-05-25_16-40-11_272.png)
![14-05-25_16-39-51_036.png](assets/imgs/14-05-25_16-39-51_036.png)

$$
J(y) = \int_1^2{\groupr{x^3 ({y}^{'})^2 - 8(x^2 - x) y {y}^{'} + 4 y^2 + 8 x^2 {y}^{'}} \d x}
$$

$\Align{
\textit{Ур-ие Э-Л}: \\
\dv{x}{} \pdv{{y}^{'}}{F} - \pdv{y}{F} = 0 \\
x^2 {y}^{''} + 3 x {y}^{'} - 8 y + 8 = 0 \\
\textit{- ур-ие Эйлера} \\
y_{од} = C_1 x^2 + C_2 \frac{1}{x^4} \\
y_{частное} \equiv 1 \\
y = C_1 x^2 + C_2 \frac{1}{x^4} + 1 \\
\Cases{
\pdv{{y}^{'}}{F} \rvert_{x=1} = 0 \\
y(2) = -7
} \implies \Cases{
C_1 = -2 \\
C_2 = 0
} \\
y = -2 x^2 + 1
}$

Не дорешали...
