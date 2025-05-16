---
id: 687-mipt-probability-theory-seminar-16-05-25
aliases:
  - MIPT probability theory seminar 16-05-25
tags: []
---

# MIPT probability theory seminar 16-05-25

Распределение Коши

$$
\Align{
K(0,1) \sim f(x) = \frac{1}{\pi (1 + x^2)} \\
F(x) = \frac{1}{2} + \frac{1}{\pi} \arctan{x}
}
$$

# 2.

$\Align{
\xi_i - \textit{норсв} \in K(0,1) \\
X_n = \frac{1}{n} \max \xi_i \\
}$

Д-ть:

$X_n \xra{d} $

$\Align{
\arctan x \to \frac{\pi}{2} \group{1 - \frac{2}{x}}, \quad x \to \infty \\
F_{X_n} = \prod{P(\xi_i < n x)} = F_\xi^n(nx) \to e^{-\frac{1}{x}} \\
}$

# ЗБЧ (закон больших чисел)

$X_i$ - норсв

$$
\frac{1}{n} \sum_{k=1}^{n}{X_k} \xra{p} E X
$$

# ЦПТ (центральная предельная)

$$
\frac{1}{\sqrt{n}} \sum_{k=1}^{n}{X_k} \xra{d} \mcN(E X, D X)
$$

# Теорема Линдеберга

## If:

$X_i$ - независимы
$D_n = \sqrt{D\group{\sum_{k=1}^{n}{X_k}}}$

Условие Линдеберга:

$$
\frac{1}{D_n^2} \sum_{k=1}^{n}{
E\groupr{\mathring{X_k^2} I\set{\abs{\mathring{X_k^2}} > \varepsilon D_n}}}
$$

## Then:

$\forall \varepsilon$

$$
\frac{1}{D_n} \sum_{k=1}^{n}{\mathring{X_k}} \xra{d} \mcN(0,1)
$$

# Задача

$\Align{
X_k = \Cases{
k,& \frac{1}{2} \\
-k,& \frac{1}{2}
}
}$

ЦПТ

$\Align{
D_n \sim \sqrt{\frac{n^3}{3}} \\
(L)
}$
