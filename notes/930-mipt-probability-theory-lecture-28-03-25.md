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

# Замыкание

$$
\mathring{\xi} \defeq \xi - E_\xi
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

1. $cov(\xi, \eta) = E_{\xi\eta} - E_\xi E_\eta$
2. $cov(\xi, \xi) = D_\xi$
3. $\eta = a\xi + b \implies cov(\xi,\eta) = a D_\xi$

# Независимость

$\set{\xi_j}$ - независимые случайные величины, если
$\bbB$ - алгебра
$\set{B_j} \subseteq \bbB$

$$
P\group{ \bigcup_{j=1}^{n}\set{\xi_j \in B_j}} = \prod_{j=1}^{n}{P\group{\xi_j \in B_j}}
$$

# Lemma. Эквивалентные определения.

1. $B_j \in \bbB$ - алгебра
2. $B_j \in \mcB$ - Борелевская сигма-алгебра
3. $B_j \in (-\infty, b_j)$
4. $B_j \in [a_j, b_j)$

$$
F_{\xi_1, \dots, \xi_n} \group{x_1, \dots, x_n} = \prod_{j=1}^{n}{F_{\xi_j}(x_j)}
$$

$$
\AlignLeft{
2 \implies 1 \\
1 \implies 4 \\
2 \implies 3 \\
1 \implies 2 \\
3 \implies 4 \\
4 \implies 1 \\
}
$$

![28-03-25_13-09-45_978_IMG_20250328_125809.jpg](assets/imgs/28-03-25_13-09-45_978_IMG_20250328_125809.jpg)
![28-03-25_13-09-45_106_IMG_20250328_130703.jpg](assets/imgs/28-03-25_13-09-45_106_IMG_20250328_130703.jpg)
![28-03-25_13-09-45_407_IMG_20250328_130848.jpg](assets/imgs/28-03-25_13-09-45_407_IMG_20250328_130848.jpg)

# Lemma. Свойство-Эквивалентное определение.

Сигма-алгебры, порожденные НСВ, являются независимыми.

![28-03-25_13-20-10_735_IMG_20250328_131348.jpg](assets/imgs/28-03-25_13-20-10_735_IMG_20250328_131348.jpg)
![28-03-25_13-21-42_739_IMG_20250328_132125.jpg](assets/imgs/28-03-25_13-21-42_739_IMG_20250328_132125.jpg)

# Claim

$$
\xi, \eta - НСВ \implies E_{\xi\eta} = E_\xi E_\eta
$$

![28-03-25_13-20-10_106_IMG_20250328_131858_1.jpg](assets/imgs/28-03-25_13-20-10_106_IMG_20250328_131858_1.jpg)
![28-03-25_13-24-33_875_IMG_20250328_132410.jpg](assets/imgs/28-03-25_13-24-33_875_IMG_20250328_132410.jpg)

# Claim
$$
\xi, \eta - НСВ \implies \Cases{
E_{\xi\eta} = E_\xi E_\eta \\
cov(\xi, \eta) = 0 \\
D_{\xi\eta} = D_\xi + D_\eta \\
\rho(\xi, \eta) = 0
}
$$

# Коэффицент кореляции
$$
\rho\group{\xi, \eta} \defeq \frac{cov(\xi, \eta)}{\sqrt{D_\xi D_\eta}}
$$

## Свойства
1. $\rho \le 1$
2. $\eta = a \xi + b \implies \rho = sign(a)$
3. $\xi,\eta - НСВ \implies \rho = 0$

# Нормальный случайный вектор
$$
N(\vec{m}, R)
$$
$\vec{m} = E{\vec{\xi}}$
$R_{ij} = \set{cov(\xi_i, \xi_j)}$
