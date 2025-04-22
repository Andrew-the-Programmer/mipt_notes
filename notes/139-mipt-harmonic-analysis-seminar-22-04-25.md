---
id: 139-mipt-harmonic-analysis-seminar-22-04-25
aliases:
  - MIPT harmonic analysis seminar 22-04-25
tags: []
---

# MIPT harmonic analysis seminar 22-04-25

# Интеграл Фурье интеграла Пуассона

$$
F\groupr{e^{-\frac{x^2}{2}}}(y) = \frac{1}{\sqrt{2\pi}} e^{-\frac{y^2}{2}}
$$

# Пример 2

$$
f(x) = \Cases{
e^{-ax},& x\ge0\\
0,& x<0\\
}
$$

$$
F\groupr{f}(y) = \frac{1}{2\pi} \frac{1}{i y + a}
$$

$$
F\groupr{e^{-a \abs{x}}} = F\groupr{f(x) + f(-x)} =
\frac{1}{\pi} \frac{a}{a^2 + y^2}
$$

# Claim

$$
F\groupr{f(-x)}(y) = F\groupr{f(x)}(-y)
$$

# 3

$f, xf, \dots, x^k f \in L_1(\RR)$

$\Align{
F[xf] = i {F}^{'}[f]
}$

$$
F[x^k F] = i^k {F}^{(k)}[f]
$$

$x \to i \dv{x}{}$

# Claim

$$
f, {f}^{'} \in L_1 \implies f(x) \to 0, x \to \pm\infty
$$

# 4

$f, {f}^{'}, \dots, {f}^{(k)} \in L_1(\RR)$

$$
F\groupr{{f}^{'}} = i y F[f]
$$

$\dv{x}{} \to i y$

# Claim

$$
f \in C^\infty(\RR) \implies \forall k \hthen y^k f(y) \to 0,\quad y \to \infty
$$

$$
x^k f \in L_1(\RR) \forall k \implies f \in C^\infty(\RR)
$$

# Пространство Шварца

$$
S \defeq \set{f \in C^\infty(\RR) \mid
\forall m,p \in \NN \hthen x^m {f}^{(p)}(x) \to 0,\ x \to \pm\infty}
$$

# Claim

$$
F: S \to S - \textit{изоморфизм}
$$

$$
F^2[f(x)] = f(-x)
$$

# .

$$
\Gather{
\abs{f(x)} < e^{-\delta x}\quad (\delta > 0) \\
\implies\\
F\groupr{f}(y : \Im y < \delta) - \textit{аналитична (сходится к своему ряду Тейлора)}
}
$$

# .

$f$ - с компактным носителем ($supp(f) \defeq \sigma\set{x : f(x) = 0}$ - компакт)
$\implies$
$F\groupr{f}$ - аналитична в $\CC$

# .

# Преобразование Фурье в $L_2(\RR)$

$F: L_2(\RR) \to L_2(\RR)$

$$
F\groupr{f}(y) \defeq v.p.
\frac{1}{\sqrt{2\pi}} \int_{-\infty}^{+\infty}{f(x) e^{-iyx} dx}
$$

Интеграл в смысле главного значения

$$
v.p. \int_{-\infty}^{+\infty}{f(x) dx} \defeq \lim_{R\to\infty} \int_{-R}^{+R}{f(x) \d x}
$$

# Theorem.

## If:

$f \in L_2(\RR)$

## Then:

1. $F\groupr{f}$ всегда суцествует
2. $f \in L_1(\RR) \cap L_2(\RR) \implies F_{L_1}\groupr{f} = F_{L_2}\groupr{f}$
