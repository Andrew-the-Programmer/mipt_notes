---
id: 884-mipt-probability-theory-seminar-08-05-25
aliases:
  - MIPT probability theory seminar 08-05-25
tags: []
---

# MIPT probability theory seminar 08-05-25

$$
\AlignCenter{
X_n \xra{p} X \same
\forall \varepsilon \hthen P(\abs{X_n - X} > \varepsilon) \to 0 \\
X_n \xra{п.н.} X \same
\forall \varepsilon \hthen P(\sup_{k \ge n}\abs{X_n - X} > \varepsilon) \to 0 \\
X_n \xra{d} X \same
\forall
}
$$

# 105

$\Align{
\set{X_n} \\
X \\
\sum_{n\in\NN}{P\set{\abs{X_n - X} > \varepsilon}} < \infty \\
}$

Д-ть:
$X_n \xra{п.н.} X$

# 106

$X_n \xra{p} X$
Д-ть:
$\exists \set{n_k}: X_{n_k} \xra{п.н.} X$

# Claim

$\Align{
\set{X_n}, \set{Y_n} \\
X_n, Y_n - \textit{н.с.в.} \\
X_n \xra{d} X,\quad Y_n \xra{d} Y \\
}$

Д-ть:
$X_n + Y_n \xra{d} X + Y$

# 100 (г)

$\Align{
\set{X_n}, \set{Y_n} \\
X_n \xra{d} X,\quad Y_n \xra{d} Y \\
}$

Привести пример:
$X_n + Y_n \xra{d} X + Y$

$\Align{
X_n \sim \mcN(0,1),\quad Y_n = X_n
}$

# Задача

$\Align{
\set{X_n} - \textit{н.с.в.} \\
X_n \xra{p} X
}$

Д-ть:
$X \equiv const$

# ЗБЧ

$$
\frac{1}{n} \sum_{k=1}^{n}{\mathring{X_k}} \xra{p} 0
$$

# Theorem. Колмогорова. Критерий выполнимости ЗБЧ.

$$
\Gather{
E \group{\frac{\group{\ol{\mathring{\xi_n}}}^2}{1 + \group{\ol{\mathring{\xi_n}}}^2}}
\xrightarrow{n\to\infty} 0 \\
\same \\
ЗБЧ
}
$$

$\set{\xi_n} - НСВ \implies$

$$
\sum_{k=1}^n E\group{\frac{\group{\mathring{\xi_k}}^2}{n^2 + \group{\mathring{\xi_k}}^2}}
\to 0
$$

# 109

$\Align{
x_n = \Cases{
2^k,& \frac{1}{2} \\
-2^k,& \frac{1}{2}
} \\
\set{x_n} - \textit{н.с.в.} \\
}$

Д-ть:
$\lnot ЗБЧ$

$\Align{
}$

# 109.2

$\Align{
x_n = \Cases{
\sqrt{n},& \frac{1}{2} \\
-\sqrt{n},& \frac{1}{2}
} \\
\set{x_n} - \textit{н.с.в.} \\
}$

Д-ть:
$\lnot ЗБЧ$

$\Align{
}$

# 110

$\Align{
x_n = \Cases{
n^\alpha,& \frac{1}{2} \\
-n^\alpha,& \frac{1}{2}
} \\
\set{x_n} - \textit{н.с.в.} \\
}$

При каких $\alpha$:
$ЗБЧ$

При $\alpha \in (0,\frac{1}{2})$

# Теорема Маркова. Достаточное условие ЗБЧ.

$$
\frac{1}{n^2} D\group{\sum_{k=1}^n \xi_k} \xrightarrow{n\to\infty} 0 \implies ЗБЧ
$$

# 111

$\Align{
\set{x_n} \\
D x_n = \sigma_n^2 \\
E\groupr{\mathring{x_k} \cdot \mathring{x_l}}
}$

Д-ть:
$ЗБЧ$

$\Align{
\frac{1}{n^2} D\sum_{k = 1}^{n}{\mathring{x_k}} = 
\frac{1}{n^2} \sum_{k = 1}^{n}{\sigma_k^2} + 
\frac{1}{n^2} \sum_{k\neq l}{cov(x_k, x_l)} \le
\frac{1}{n^2} \sum_{k = 1}^{n}{\sigma_k^2} \to 0
}$
