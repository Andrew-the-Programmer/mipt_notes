---
id: 896-mipt-field-theory-lecture-12-03-25
aliases:
  - MIPT field theory lecture 12-03-25
tags: []
---

# MIPT field theory lecture 12-03-25

4-вектор
4-ускорение

# Принцып наименьшего действия

# Симметрии законов преобразования

# Def. Действие

$$
\Gather{
S - \textit{функционал от траектории}\ x(t) \\
S: x(t) \to \RR
}
$$

$$
S = \int_{t_1}^{t^2}{L(x,\dot{x},t) \d t}
$$

# Принцып Гамильтона (наименьшего действия)

На действительной траектории $S$ локально минимальна.

# Теорема Нётера

$S$ инвариантно относительно некоторого преобразования
$\implies$
имеется некоторый интеграл движения

$L$ - лагранжиан.

# Уравнения Лагранжа

$$
\AlignLeft{
x(t) = x_0(t) + \delta x(t) - \textit{вариация} \\
\delta x(t_1) = \delta x(t_2) = 0 \\
\delta S = \int_{t_1}^{t_2}{\group{\pdv{x}{L} \delta x + \pdv{\dot{x}}{L} \delta \dot{x}} \d t} =
\pdv{\dot{x}}{L} \delta x \rvert_{t_1}^{t_2} +
\int_{t_1}^{t_2}{\group{\pdv{x}{L} - \Dv{t}{\pdv{\dot{x}}{L}}} \delta x \d t} = \\
= \int_{t_1}^{t_2}{\group{\pdv{x}{L} - \Dv{t}{\pdv{\dot{x}}{L}}} \delta x \d t} \\
\pdv{\dot{x}}{L} \delta x \rvert_{t_1}^{t_2} = 0 \\
}
$$
# Преобразование траектории и однородность пространства.
