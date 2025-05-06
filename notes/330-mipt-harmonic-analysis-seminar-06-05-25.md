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

# Definition

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

# Claim

## If:

$f \in {D}^{'}$
$g \in C^{\infty}$

## Then:

$$
\groupt{gf, \varphi} \defeq \groupt{f, g \varphi}
$$
