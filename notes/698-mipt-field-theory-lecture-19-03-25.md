---
id: 698-mipt-field-theory-lecture-19-03-25
aliases:
  - MIPT field theory lecture 19-03-25
tags: []
---

# MIPT field theory lecture 19-03-25

![1.jpg](assets/imgs/19-03-25_10-05-18_377_IMG_20250319_090759.jpg)
![2.jpg](assets/imgs/19-03-25_10-05-18_022_IMG_20250319_091010.jpg)

# .

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

![4.jpg](assets/imgs/19-03-25_10-05-18_273_IMG_20250319_091526.jpg)

# Динамика свободной релятивисткой частицы

![6.jpg](assets/imgs/19-03-25_10-05-18_669_IMG_20250319_092014.jpg)

# Импульс

$$
p \defeq \vdv{v}{L} = m \vec{v}(t) \gamma(t)
$$

# Энергия

$$
H \defeq \veccrossv{p}{v} - L = \gamma m c^2
$$

# ЗСИ и ЗСЭ

![9.jpg](assets/imgs/19-03-25_10-05-18_103_IMG_20250319_092938.jpg)

# Ковариантная форма действия

$$
S = -mc^2 \int_{t_1}^{t_2}{\sqrt{1 + \frac{v^2}{c^2}}\d t}
$$

![10.jpg](assets/imgs/19-03-25_10-05-18_633_IMG_20250319_092944.jpg)

# Уравнение движения в ковариантной форме

$$
x^\mu(s) = x^\mu(0) + u^\mu s
$$

![11.jpg](assets/imgs/19-03-25_10-05-18_918_IMG_20250319_093337.jpg)

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

![14.jpg](assets/imgs/19-03-25_10-05-18_070_IMG_20250319_095552.jpg)

# Импульсное пространство минковского

![13.jpg](assets/imgs/19-03-25_10-05-18_808_IMG_20250319_094857.jpg)

$\group{\frac{E}{c}, p_x, p_y, p_z}$

$\group{\frac{E}{c}}^2 - p^2 = (mc)^2$ - гиперболоид -
**_массовая поверхность_**
**_mass shell_**

Конус: $m = 0$.
$E = \abs{p} c$

# Инвариантная масса системы частиц

Суммарный 4-импульс

$$
P_\Sigma^\mu = \sum{P_i^\mu}
$$

# Система центра инерции

**_Система центра инерции_** - ИСО, в которой $\vec{p}_\Sigma^\mu = 0$.

$$
\group{P_\Sigma^{'}}^\mu = \Pmatrix{
M_\Sigma c \\ \vec{0}
}
$$

## Скорость СЦИ

$v_c$

$$
\AlignLeft{
P_\Sigma^\mu = \group{\Lambda\inv(v_c)}_\nu^\mu \group{P_\Sigma^{'}}^\mu =
\Pmatrix{
\gamma M_\Sigma c \\
\gamma M_\Sigma \vec{v_c}
} \\
\vec{v_c} = c^2 \frac{\vec{p}_\Sigma}{E_\Sigma}
}
$$

# Движение частицы под действием силы

**_4-сила_**:

$$
mc w^\mu = \dv{s}{p^\mu} \defeq \frac{1}{c} f^\mu
$$

# Действие для частицы в силовом поле

![18.jpg](assets/imgs/19-03-25_10-46-07_853_IMG_20250319_101732.jpg)

$$
S = \int{\groupr{-mc \sqrt{\dv{s}{x_\mu} \dv{s}{x^\mu}} + \frac{1}{c} f^\mu x_\mu} \d s} \\


$$

$$
\AlignCenter{
L_{free} \defeq -mc \sqrt{\dv{s}{x_\mu} \dv{s}{x^\mu}} \\
L_{int} \defeq \frac{1}{c} f^\mu x_\mu \quad (interaction) \\
L = L_{free} + L_{int}
}
$$

Ур-ие Эйлера-Лагранжа

$$
\Gather{
\Dv{s}{\vdv{u^\mu}{L}} - \vdv{x^\mu}{L} = 0 \\
mc w^\mu - \frac{1}{c} f^\mu = 0
}
$$
$$
u_\mu \perp f^\mu \\
$$

В сопутствуюцей СО:

$$
\AlignLeft{
{u^{'}}^\mu = \Pmatrix{
1 \\ \vec{0}
} \\
f^0 = 0
}
$$

$$
{f^{'}}^\mu = \Pmatrix{
0 \\ \vec{F}
}
$$

В ЛСО:

$$
f^\mu = \Pmatrix{
\frac{\gamma}{c} \veccross{F}{v} \\
\vec{F} + (\gamma - 1) \veccross{F}{v} \frac{\vec{v}}{v^2}
}
$$

![20.jpg](assets/imgs/19-03-25_10-46-07_564_IMG_20250319_102846.jpg)
