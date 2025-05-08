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
