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

$S = \frac{c}{4\pi} \vecprod{E}{B}$

$$
\gradv_i{T^{i0}} = \divv \frac{S}{c}
$$

$\Align{
\partial_\mu T^{\mu 0} = 0 \implies \\
\pdv{t}{T^{00}} + \gradv_i{T^{i0}}
}$
