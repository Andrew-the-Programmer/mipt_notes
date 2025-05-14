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

2. Нулевое (ведущее) приближение $t_{ret} = t - \frac{\abs{x}}{c}$
3. Первое приближение $t_{ret} = t - \frac{\abs{x}}{c} + \frac{\vec{n} \cdot \vec{x_e}(t - \frac{\abs{x}}{c})}{c}$
