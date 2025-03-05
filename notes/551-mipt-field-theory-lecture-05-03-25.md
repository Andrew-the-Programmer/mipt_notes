---
id: 551-mipt-field-theory-lecture-05-03-25
aliases:
  - MIPT field theory lecture 05-03-25
tags: []
---

# MIPT field theory lecture 05-03-25

Инвариант ные тензоры в пространстве Минковского.
Абволютно антисимметричный тензор $e_{\mu\nu\rho\sigma}$
4-объем $V_4$
Символ кронекера $\delta^\mu_\nu$

# Абсолютно антисимметричный тензор

$$
e_{\mu\nu\rho\sigma} = \Cases{
-1 & 0123 + сдвиги \\
0 & одинаковые \\
1 & 1023 + сдвиги
}
$$

# 4-объем

$$
V_4 = e_{\mu\nu\rho\sigma} a^\mu b^\nu c^\rho d^\sigma
$$

# Символ кронекера

$$
\delta^\mu_\nu = \Cases{
1, & \mu = \nu \\
0, & \mu \neq \nu
}
$$

# Дифференциал

$$
\d f = \pdv{x^\mu}{f} \d{x^\mu}
$$

$$
\partial_\mu \defeq \pdv{x^\mu}{} = \Pmatrix{
\frac{1}{c} \pdv{t}{} \\
\gradv
}
$$

# 4-дивергенция

Скаляр

$$
\partial_\mu A^\mu (x)
$$

Обобщение т. Гаусса.

$$
\Gather{
\int{\partial_\mu A^\mu \d V_4} = \int{A^\mu \d S_\mu} \\
\d S_\mu = e_{\mu\nu\rho\sigma} (r_u^{'})^\nu (r_v^{'})^\rho (r_t^{'})^\sigma \d u \d v \d t \\
}
$$

$u,v,t$ - обобщенные координаты на 3-мерной поверхности

Т. Стокса

$$
\d{{S}_{i}^{'}} = ({r}_{u}^{'} \times {r}_{v}^{'})_i \d u \d v =
e_{ijk} ({r}_{u}^{'})_j ({r}_{u}^{'})_k \d u \d v =
\frac{1}{2} e_{ijk} \left[({r}_{u}^{'})_j ({r}_{u}^{'})_k - ({r}_{u}^{'})_k ({r}_{u}^{'})_j\right] =
\frac{1}{2} e_{ijk} \d{S_{jk}}
$$

$$
\int{\rot{A} \d S} =
\frac{1}{2} \int{e_{ilm}\ \partial_l A_m\ e_{ijk}\ \d{S_{jk}}} =
\frac{1}{2} \int{\left(\partial_j A_k - \partial_k A_j\right) \d S_{jk}}
$$

$$
\oint{A \d l} = \frac{1}{2} \int{\left(\partial_j A_k - \partial_k A_j\right) \d S_{jk}}
$$

$$
\oint{A_\mu \d x^\mu} = \int{\left(\partial_\mu A_\nu - \partial_\nu A_\mu\right) \d S^{\mu\nu}}
$$

# Движение свободной релятивисткой частицы

# Мировая линия

$-$ траектория в пространстве Минковского $x^\mu(t)$.

# Скорость

$$
\vec{{v}_{i}}(t) = \dv{t}{\vec{{x}_{i}}} = \pDv{t}{x^i}
$$

Проблемы:

- нелинейный закон сложения скоростей.
-

# Мнговенно сопутствующая инерциальная система отсчета

Начало координат в положении частицы + имеет скорость частицы.

# Собственное время

$$
\AlignLeft{
x_1^\mu = \Pmatrix{
c t_1 \\
x(t_1)
}, \quad
x_2^\mu = \Pmatrix{
c (t_1 + \d t) \\
x(t_1 + \d t)
} = \Pmatrix{
c (t_1 + \d t) \\
x(t_1) + v(t_1) \d t
} \\
\d S_{12}^2 = (c \d t)^2 - v(t_1)^2 \d t^2 =
(c\ \d t)^2 \left(1 - \frac{v^2(t_1)}{c^2}\right) \\
\textit{В МССО:}\quad t = \tau \textit{(собственное время)}, \quad v = 0 \\
(c\ \d \tau^2) = (c\ \d t)^2 \left(1 - \frac{v^2(t_1)}{c^2}\right) \\
}
$$

Собственное время:

$$
\D \tau = \tau_2 - \tau_1 = \int_{t_1}^{t_2}{\d t \sqrt{1 - \frac{v^2}{c^2}}}
$$

Собственное время - инвариант.

# Принцип максимума собственного времени
$$
v = \frac{x_2 - x_1}{t_2 - t_1}
$$
