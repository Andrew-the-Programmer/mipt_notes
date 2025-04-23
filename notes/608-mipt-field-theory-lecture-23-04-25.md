---
id: 608-mipt-field-theory-lecture-23-04-25
aliases:
  - MIPT field theory lecture 23-04-25
tags: []
---

# MIPT field theory lecture 23-04-25

![1.jpg](assets/imgs/23-04-25_09-16-29_904_IMG_20250423_091057.jpg)
![2.jpg](assets/imgs/23-04-25_09-16-29_476_IMG_20250423_091103.jpg)

# Энергия и импульс ЭМ поля

# Действие свободного ЭМ поля

$$
S = -\frac{1}{16\pi c} \int{F^{\mu\nu} F_{\mu\nu} \d^4 x}
$$

# Теорема Нётера.

$\delta S$ инвариантна относительно сдвигов $\varepsilon^\mu$.
Для свободного ЭМ поля:

$$
\delta S = -\frac{1}{16\pi c} \int{\d^4 x \groupr{-4 \partial_\mu }}
$$

$\varepsilon^\mu$ произвольно $\implies$

# Тензор энергии-импульса ЭМ поля

$$
\Gather{
T_\nu^\mu \defeq -\frac{1}{4\pi} F^{\mu\lambda} (\partial_\nu A_\nu) +
\frac{1}{16\pi} \delta_\lambda^\mu \group{F^{\rho\sigma} F_{\rho\sigma}} \\
\partial_\mu\group{T_\nu^\mu} = 0 \\
}
$$

$T_\lambda^\mu$ задан неоднозначно:

$B_\nu^{\rho\mu} = B_\nu^{\mu\rho}$
$const \cdot T_\nu^\mu + \partial_\rho B_\nu^{\rho\mu}$ - тоже тензор энергии-импульса.

Калибровочная инвариантность
Симметричность

$$
T^{\mu\lambda} = -\frac{1}{4\pi} F^{\mu\nu} F_{\nu}^{\lambda} + \frac{1}{16\pi} \eta^{\mu\lambda} F^{\rho\sigma} F_{\rho\sigma}
$$

# Физический смысл компонент тензора энергии-импульса ЭМ поля

Плотность ЭМ поля

$$
\varepsilon \defeq T^{00} = \frac{E^2 + B^2}{8\pi}
$$

$T^{\mu 0}$ соответствует сдвигу по временной оси.
$T^{\mu i}$ соответствует сдвигу по пространственным компонентам.

$\Align{
S = \frac{c}{4\pi} \vecprod{E}{B} \\
\gradv_i{T^{i0}} = \divv \frac{S}{c} \\
\partial_\mu T^{\mu 0} = 0 \implies \\
\frac{1}{c} \pdv{t}{T^{00}} + \gradv_i{T^{i0}} = 0 \\
}$

Закон сохраниения энергии ЭМ поля:

$$
\pdv{t}{\varepsilon} + \divv S = 0
$$

Закон сохраниения импульса ЭМ поля:

$\Align{
\partial_\mu T^{\mu i} = 0 \\
\frac{1}{c} \pdv{t}{T^{0i}} + \pdv{x^j}{}{T^{ji}} = 0 \\
}$

$$
T = \Pmatrix{
\varepsilon & \frac{S_1}{c} & \frac{S_2}{c} & \frac{S_3}{c} \\
\frac{S_1}{c} & \sigma_{11} & \sigma_{12} & \sigma_{13} \\
\frac{S_2}{c} & \sigma_{21} & \sigma_{22} & \sigma_{23} \\
\frac{S_3}{c} & \sigma_{31} & \sigma_{32} & \sigma_{33} \\
}
$$

# Законы сохранения тензара энергии-импульса ЭМ поля в присутствии внешних токов и зарядов.

Ур-ия Максвелла:

$$
\partial_\mu F^{\mu\nu} = \frac{4\pi}{c} j^\mu
$$

$\Align{
\partial_\mu T^{\mu\nu} = \frac{1}{c} F^{0\mu} \\
}$

ЗСЭ:

$$
\pdv{t}{\varepsilon} + \divv S = \veccross{j}{E}
$$
