---
id: 643-mipt-differential-equations-lecture-19-02-25
aliases:
  - MIPT differential equations lecture 19-02-25
tags: []
---

# MIPT differential equations lecture 19-02-25

# Lemma
$$
\AlignLeft{
\varphi, f \in C([a,b]) \\
\forall h \in C^1([a,b]): h(a) = h(b) = 0 \hthen
\int_a^b{(h \varphi + {h}^{'})} = 0 \\
\implies \\
1)\ f \in C^1([a,b]) \\
2)\ \varphi = \dv{x}{f}
}
$$
## Proof
![[1739952284.png]]
![[1739952293.png]]

## Note
![[1739952301.png]]

# Theorem 1.
$$
\AlignLeft{
F(x,y,p) \in C^2 \\
J[y] = \int_a^b{F \d x} \\
J[y_m] - max \\
\implies (условие\ Эйлера) \\
F_y \rvert_{y_m} = \Dv{x}{F_{{y}^{'}}} \rvert_{y_m}
}
$$
## Proof
![[1739952310.png]]

# Theorem 2.
$$
\AlignLeft{
F \in C^2 \\
F_y = \Dv{x}{F_{{y}^{'}}} \\
\pdv[2]{({y}^{'})}{F} \neq 0 \\
\implies \\
y \in C^2
}
$$
## Proof
![[1739952988.png]]
![[1739952993.png]]
![[1739952999.png]]

# Экстремаль
-- решение ур-ия Эйлера

# Допустимая функция

# Допустимая экстремаль
-- экстремаль из класса допустимых функций.

# Основная задача Вариационного Исчисления (ВИ) - задача с закрепленными концами
$$
\AlignLeft{
J[y] = \int_a^b{F(x,y,{y}^{'}) \d x} \\
F \in C^2 \\
M_1^{AB} \defeq \set{y \in C^1 \mid y(a) = A, y(b) = B} - \text{допустимый класс функций} \\
\implies \\
\text{Найти допустимые экстремали}
}
$$
