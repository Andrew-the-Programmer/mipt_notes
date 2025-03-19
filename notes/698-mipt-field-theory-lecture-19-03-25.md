---
id: 698-mipt-field-theory-lecture-19-03-25
aliases:
  - MIPT field theory lecture 19-03-25
tags: []
---

# MIPT field theory lecture 19-03-25

# Тема лекции - Динамика свободной релятивисткой частицы.

# Действия для свободной релятивисткой частицы.

1. Инсинные траектории - прямые
2. Принцип максимума собственного времени.
3. S - действие - лоренцевый скаляр
   $$
   \D \tau = \int_{t_1}^{t_2}{\d t \sqrt{1 - \frac{v^2}{c^2}}}
   $$
4. S минимально на истинной траектории.

$\implies$

$$
\AlignLeft{
S = -\alpha \int{\d s} = -\alpha c \D \tau \\
\frac{v}{c} \to 0 \\
S \to \int_{t_1}^{t_2}{\d t \frac{m v^2}{2}} \\
S \approx \int{\group{-\alpha c + \frac{\alpha v^2}{2 c}}\d t} \\
\alpha = mc \\
}
$$

$$
\Gather{
S = -m c^2 \int_{t_1}^{t_2}{\d t \sqrt{1 - \frac{v^2}{2}}} \\
L = -mc^2 \sqrt{1 - \frac{v^2}{c^2}} \\
}
$$

# Импульс

$$
p \defeq \vdv{v}{L} = m \vec{v}(t) \gamma(t)
$$

# Уравнение движения в ковариантной форме

$$
x^\mu(s) = x^\mu(0) + u^\mu s
$$

# 4-импульс

$$
P^\mu \defeq mc u^\mu = \Pmatrix{
\frac{E}{c} \\ \vec{p}
}
$$

# ЗС 4-импульса

$$
\dv{x}{P^\mu} = 0
$$

# Длина 4-импульса

$$
P^2 = P^\mu P_\mu = \group{\frac{E}{c}}^2 - p^2
$$

В системе покоя.

$$
{{P}^{'}}^\mu = \Pmatrix{
\frac{mc^2}{c} \\ \vec{0}
}
$$

# Дисперсионное соотношение

$P^2 = { {P}^{'} }^2 \implies$

$$
\group{\frac{E}{c}}^2 - p^2 = (mc)^2
$$

# Импульсное пространство минковского
$\group{\frac{E}{c}, p_x, p_y, p_z}$ 

$\group{\frac{E}{c}}^2 - p^2 = (mc)^2$ - гиперболоид -
***массовая поверхность***
***mass shell***

Конус: $m = 0$.
$E = \abs{p} c$

# Инвариантная масса системы частиц
Суммарный 4-импульс
$$
P_\Sigma^\mu = \sum{P_i^\mu}
$$
***Система центра инерции*** -
ИСО, в которой $P_\Sigma^\mu = 0$
# Система центра инерции
