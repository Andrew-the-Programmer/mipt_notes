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
