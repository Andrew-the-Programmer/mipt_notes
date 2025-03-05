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
