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
\int_a^b{(h \varphi + {h}^{'} f)} = 0 \\
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
J[y] - экстремум \\
\implies (условие\ Эйлера) \\
F_y = \Dv{x}{F_{{y}^{'}}}
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

# Класс допустимых функций
-- некоторый класса функций

# Допустимая экстремаль
-- экстремаль из класса допустимых функций.

# Основная задача Вариационного Исчисления (ВИ) - задача с закрепленными концами
$$
\AlignLeft{
J[y] = \int_a^b{F(x,y,{y}^{'}) \d x} \\
F \in C^2 \\
y \in M_1^{AB} \defeq \set{y \in C^1 \mid y(a) = A, y(b) = B} - \text{допустимый класс функций} \\
h \in M_1^{00} \\
\implies \\
\text{Найти допустимые экстремали}
}
$$

# Theorem 3.
$$
\AlignLeft{
y - \text{допустимый экстремум}\ M_1^{A?} \\
\implies (граничное\ условие) \\
F_{{y}^{'}} \rvert_{x = b} = 0
}
$$
## Proof
$$
\AlignLeft{
\delta J_y[h] = 0 \\
\delta J_y[h] = \int_a^b{(F_y h + F_{{y}^{'}} {h}^{'}) \d x} = 
\int_a^b{(\Dv{x}{F_{{y}^{'}}} h + F_{{y}^{'}} {h}^{'}) \d x} = 
F_{{y}^{'}} h \rvert_a^b = F_{{y}^{'}}(b) h(b) - F_{{y}^{'}}(a) h(a) = 0 \\
h(a) = 0\\
F_{{y}^{'}}(b) = 0 \\
\blacksquare
}
$$
# Векторные функции
$y: \RR \to \RR[n]$
$$
\vec{y}(x) = \Pmatrix{
y_1(x) \\
\dots \\
y_n(x)
}
$$

# Условие Эйлера для векторных ф-ий 
$$
\AlignLeft{
\vec{y} - экстремум\ J[\vec{y}] \\
\implies \\
\Cases{
F_{y_i} = \Dv{x}{F_{y_i^{'}}} & i \in [1,n] \\
}
}
$$

# Закрепленные концы - k
$$
\AlignLeft{
M_k^{AB} = \set{y \in C^k([a,b]) \mid\ y^{(i)}(a) = A_i,\ y^{(i)}(b) = B_i, \quad i \in [0, k-1]}
}
$$

# Вариация - k
$$
\delta J_{\vec{y}}[h] = \int_a^b{\left(\sum_{i\in [0,k]}{F_{y^{(i)}} h^{(i)}}\right) \d x}
$$

# Theorem 4.
$$
\AlignLeft{
y \in M_k^{AB} - \text{экстремум} \\
\implies (условие\ Эйлера-Пуассона) \\
}
$$
$$
\Gather{
\sum{(-1)^k \Dv[k]{x}{\pdv{y^{(k)}}{F}}} = 0
}
$$
