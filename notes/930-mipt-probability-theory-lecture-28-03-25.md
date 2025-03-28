---
id: 930-mipt-probability-theory-lecture-28-03-25
aliases:
  - MIPT probability theory lecture 28-03-25
tags: []
---

# MIPT probability theory lecture 28-03-25

k-ый момент случайной величины

$$
E\group{(\xi - a)^k}
$$

$a = 0$ - начальный момент
$a = E\xi$ - центральный момент

$$
E_{\xi\eta} = \int{\xi(\omega) \cdot \eta(\omega) P(\d \omega)}
$$

$$
\vecprod{\xi}{\eta} \defeq E_{\xi\eta}
$$

[[803-Гильбертово-пространство-hilbert-space|гильбертово пространство]]

Гельдера

$$
E_{\abs{\xi\eta}} \le \group{E_{\abs{\xi}^p}}^\frac{1}{p} \group{E_{\abs{\eta}^q}}^\frac{1}{q}
$$

КБШ

$$
\group{E_{\abs{\xi + \eta}^p}}^\frac{1}{p} \le
\group{E_{\abs{\xi}^p}}^\frac{1}{p} + \group{E_{\abs{\eta}^p}}^\frac{1}{p}
$$

Ляпунова

$$
\group{E_{\abs{\xi + \eta}^p}}^\frac{1}{p} \ge
\group{E_{\abs{\xi}^q}}^\frac{1}{q},\quad
p > q > 0
$$

Йенсена

$$
$$

# Норма

$$
\norm{\xi} \defeq \sqrt{\vecprod{\xi}{\xi}}
$$

$$
\norm{\xi - a}^2 = E(\xi - a)^2 = E_{\xi^2} + a^2 - 2a E_\xi
$$

# Дисперсия

$D_\xi = \sigma^2 \defeq \norm{\xi - E\xi}$

## Свойства

1. $D_\xi = E_{\xi^2} - (E_\xi)^2$
2. $D_{a\xi + b} = a^2 E\group{\group{\mathring{\xi}}^2}$
3. $D_\xi = 0 \same \xi \equiv const$
4. $D_{\xi + \eta} = 
E\group{\mathring{\xi} + \mathring{\eta}}^2 = 
D_\xi + D_\eta + 2 E_{\mathring{\xi}\mathring{\eta}} = 
D_\xi + D_\eta + cov\group{\xi, \eta}$

# Ковариация

$$
cov(\xi, \eta) \defeq E_{\mathring{\xi}\mathring{\eta}}
$$

## Свойства
