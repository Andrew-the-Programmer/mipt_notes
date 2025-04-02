---
id: 471-mipt-differential-equations-seminar-02-04-25
aliases:
  - MIPT differential equations seminar 02-04-25
tags: []
---

# MIPT differential equations seminar 02-04-25

![1.png](assets/imgs/02-04-25_16-00-01_138_02-04-25_16-00-01_194.png)
![2.png](assets/imgs/26-03-25_15-46-21_828_26-03-25_15-46-21_352.png)

# Доделали Р13.39

# 894

![894.png](assets/imgs/02-04-25_16-07-54_429_02-04-25_16-07-54_382.png)
$
\AlignCenter{
\Cases{
\dot{x} = a_1 x + b_1 y + c_1(t) \\
\dot{y} = a_2 x + b_2 y + c_2(t)
}
}
$
Я не осознал...

# 920

![920.png](assets/imgs/02-04-25_16-08-14_304_02-04-25_16-08-14_582.png)
$
\AlignCenter{
(x_0, y_0) = (1,1), (-4, -4) \\
\textit{Матрица Якоби:}\\
J = \Pmatrix{
\pdv{x}{f} & \pdv{y}{f} \\
\pdv{x}{g} & \pdv{y}{g}
} = \Pmatrix{
-e^x & e^y \\
(3x + y^2)^{-\frac{1}{2}} \frac{3}{2} & (3x + y^2)^{-\frac{1}{2}} y
} \\
J\rvert_{x_0,y_0} = ? \\
A = J\rvert_{1,1} = \Pmatrix{
-e & e \\
\frac{3}{4} & \frac{1}{2}
} \\
\lambda^2 + \lambda (e - \frac{1}{2}) - \frac{5}{4} = 0 \\
\textit{Неустойчивое седло.}\\
J_2 = J\rvert_{-4,-4} \\
}
$

# Р13.57

![1357.png](assets/imgs/02-04-25_16-27-54_774_02-04-25_16-27-54_147.png)
![13572.png](assets/imgs/02-04-25_16-28-39_614_02-04-25_16-28-39_925.png)

$
\AlignCenter{
\Cases{
y \defeq \dot{x} \\
\dot{y} = \ddot{x} = -2 \dot{x} - x + 2x^2 - 1
} \\
\Cases{
\dot{x} = y \\
\dot{y} = -2 y - x + 2x^2 - 1
} \\
(x_0, y_0) = (1, 0), (-1/2, 0) \\
(x_0, y_0) = (1, 0) \\
\textit{Матрица Якоби:}\\
J(x,y) = \Pmatrix{
\pdv{x}{f} & \pdv{y}{f} \\
\pdv{x}{g} & \pdv{y}{g}
} = \Pmatrix{
0 & 1 \\
4x - 1 & -2
} \\
A = J(x_0, y_0) = \Pmatrix{
0 & 1 \\
3 & -2
}\\
\lambda_{1,2} = 1,-3 \\
h_1 = \Pmatrix{
1 \\ 1
},\quad
h_2 = \Pmatrix{
-1 \\ 3
} \\
\textit{Неустойчивое седло.}\\
(x_0, y_0) = (-1/2, 0) \\
\lambda_{1,2} = -1 \pm i \sqrt{2} \\
\textit{Тип: устойчивый фокус} \\
\textit{Направление: по часовой} \\
}
$

# 13.48

![.png](assets/imgs/02-04-25_17-24-32_321_02-04-25_17-24-32_501.png)
![13-48.png](assets/imgs/02-04-25_16-45-46_100_02-04-25_16-45-46_814.png)

$
\AlignCenter{
(x_0, y_0) = (\pm 1, 1) \\
\textit{Матрица Якоби:}\\
J(x,y) = \Pmatrix{
\pdv{x}{f} & \pdv{y}{f} \\
\pdv{x}{g} & \pdv{y}{g}
} = \Pmatrix{
1 & -2y \\
0 & \frac{-2y}{1 + (1-y^2)^2}
} \\
1.\ (x_0, y_0) = (1, 1) \\
A = J(x_0, y_0) = \Pmatrix{
1 & -2 \\
0 & -2
}\\
\lambda_{1,2} = 1,-2 \\
h_1 = \Pmatrix{
1 \\ 0
},\quad
h_2 = \Pmatrix{
2 \\ 3
} \\
\textit{Тип: неустойчивое седло.}\\
2.\ (x_0, y_0) = (-1, 1) \\
A = J(x_0, y_0) = \Pmatrix{
1 & 2 \\
0 & 2
}\\
\lambda_{1,2} = 1,2 \\
h_1 = \Pmatrix{
1 \\ 0
},\quad
h_2 = \Pmatrix{
2 \\ 1
} \\
\textit{Тип: неустойчивый узел.} \\
}
$
![234.png](assets/imgs/02-04-25_17-00-29_963_02-04-25_17-00-24_966.png)
