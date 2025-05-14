---
id: 970-mipt-field-theory-lecture-14-05-25
aliases:
  - MIPT field theory lecture 14-05-25
tags: []
---

# MIPT field theory lecture 14-05-25

Последняя лекция

# Спрошлой лекции

Запаздывающий потенциал

$$
\Gather{
\vec{A}(x,t) = \frac{e}{c} \frac{\vec{v}(t_{ret})}{\abs{x - x_e(t_{ret})}} \\
t_{ret} = t - \frac{\abs{x - x_e(t)}}{c} \\
x_e(t) = \Matrix{
0 \\ 0 \\ z_0 \cos \omega t
} = z_0 \Re \Matrix{
0 \\ 0 \\ e^{i \omega t}
}
}
$$

Диаграмма Минковского

Решаем систему методом последовательных приближений

1. Если $x_e \ll x$
   $\Align{
t_{ret} \approx t - \frac{\abs{x}}{c} + \frac{\vec{n} \cdot \vec{x_e}(t)}{c} \\
\vec{n} = \frac{\vec{x}}{\abs{x}} \\
\frac{\frac{\vec{n} \cdot \vec{x_e}(t)}{c}}{t - \frac{\abs{x}}{c}} \sim \frac{v_e}{c} \\
\textit{Релятивисткое приближение}: \frac{v_e}{c} \to 0
}$

<br>

0. Нулевое (ведущее) приближение $t_{ret} = t - \frac{\abs{x}}{c}$
1. Первое приближение $t_{ret} = t - \frac{\abs{x}}{c} + \frac{\vec{n} \cdot \vec{x_e}(t - \frac{\abs{x}}{c})}{c}$

$$
A(x,t) = \frac{e}{c} \frac{v_e(t - \abs{x} / c)}{\abs{x - x_e(t - \abs{x} / c)}}
$$

Мультипольное разложение

$$
A(x,t) = \frac{e}{c} \frac{v_e(t - \abs{x} / c)}{\abs{x}}
$$

$\Align{
d(t) \defeq e x_e
}$

$$
\Gather{
\varphi = \frac{1}{c} \frac{\veccross{\dot{d}}{n}}{\abs{x}} + \frac{\veccross{d}{n}}{\abs{x}^2} \\
B = \frac{\ddot{d} \times n}{c^2 \abs{x}} + \frac{\dot{d} \times n}{c \abs{x}^2} \\
E =
\frac{3 \veccross{d}{n} \vec{n} - \vec{d}}{\abs{x}^3} +
\frac{3 \veccross{\dot{d}}{n} \vec{n} - \dot{\vec{d}}}{c \abs{x}^2} +
\frac{\veccross{\ddot{d}}{n} \vec{n} - \ddot{\vec{d}}}{c^2 \abs{x}}
}
$$

Для B:

3 случая
