---
id: 471-mipt-differential-equations-seminar-02-04-25
aliases:
  - MIPT differential equations seminar 02-04-25
tags: []
---

# MIPT differential equations seminar 02-04-25

![1.png](assets/imgs/02-04-25_16-00-01_138_02-04-25_16-00-01_194.png)

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
\dot{y} = \ddot{x} = -2 \dot{x} - x -2x^2 + 1
}
}
$
