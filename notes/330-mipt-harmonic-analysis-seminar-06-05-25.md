---
id: 330-mipt-harmonic-analysis-seminar-06-05-25
aliases:
  - MIPT harmonic analysis seminar 06-05-25
tags: []
---

# MIPT harmonic analysis seminar 06-05-25

# Пр-во пробных функций $D(\RR)$.

$$
D(\RR) \defeq \set{f \in C^\infty(\RR) \mid \supp f - \textit{компакт}}
$$

# Claim

$\set{\varphi_n} \in D$

## If:

1. $\varphi_n^{(k)} \rightrightarrows \varphi^{(k)}$
2. $\exists R : \supp \varphi_n \subset [-R, R]$

## Then:

$$
\varphi_n \to \varphi \in D
$$

# Definition. Пр-во обобщенных функций.

$$
{D}^{'}(\RR)
$$

$$
f \in {D}^{'} \same \forall \varphi_n \to \varphi \in D \hthen
f(\varphi_n) \to f(\varphi)
$$

# Claim

$$
L_1^{loc} \to {D}^{'}
$$

$$
\groupt{f,\varphi} = \int_{\RR}{f \varphi \d x}
$$

# Сингулярные функционалы

$\delta \in {D}^{'}$

$$
\delta(\varphi) \defeq \varphi(0)
$$

Сингулярный функцианал не представляется ф-ией из $L_1^{loc}$

# Definition

$$
P\groupr{\frac{1}{x}}
$$

$\Align{
f(x) = \frac{1}{x} \\
v.p. \int_\RR{f \varphi \d x} = \int_\RR{\frac{\varphi(x) - \varphi(0)}{x} \d x}
}$

# Def - Claim

## If:

$f \in {D}^{'}$
$g \in C^{\infty}$

## Then:

$$
\groupt{gf, \varphi} \defeq \groupt{f, g \varphi}
$$

# Утв. о невозможности Шварца

# Взятие производной в пр-ве обощенных ф-ий

$f \in C^{\infty} \subset {D}^{'}$
$\Align{
\groupt{{f}^{'}, \varphi} = 
\int_{\RR}{{f}^{'} \varphi \d x} = 
f \varphi \rvert_{-\infty}^{+\infty} - \int_{\RR}{f {\varphi}^{'} \d x} = 
-\groupt{f, {\varphi}^{'}}
}$

$$
\groupt{{f}^{'}, \varphi} \defeq -\groupt{f, {\varphi}^{'}}
$$

Обобщенная производная
$\Align{
f(x) = \abs{x} \\
\groupt{{f}^{'}, \varphi} = \int_{\RR}{\sign x \d x}
}$

$$
\abs{x}^{'} \defeq \sign x
$$

$$
\theta(x) \defeq \Cases{
0,& x \le 0 \\
1,& x > 0
}
$$

$$
{\theta}^{'} = \delta
$$

$$
{f}^{'}_{обобщ} = {f}^{'}_{класс} + \sum{\alpha_i \delta(x - x_i)}
$$

$x_i$ - точки разрыва

$$
{\delta}^{(k)} = (-1)^k {\varphi}^{(k)}(0)
$$

# Пример

$\Align{
f(x) = \delta(x) \group{e^{\sin x} + 3x \cos^2(x)} \\
\groupt{f, \varphi} = 
\groupt{\delta, \group{e^{\sin x} + 3x \cos^2(x)} \varphi} = 
\varphi(0) = \groupt{\delta, \varphi}
}$

# Дельта-образная последовательность

## If:



$\set{\varphi_n}$

1.  $\varphi_n \in C$
2.  $\int_\RR{\varphi_n \d x} = 1$
3.  $\varphi_n(x) \to \Cases{
0,& x \neq 0 \\
+\infty,& x = 0
}$

$$
\varphi_n \to \delta
$$
