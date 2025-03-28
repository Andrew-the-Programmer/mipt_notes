---
id: 299-mipt-probability-theory-seminar-28-03-25
aliases:
  - MIPT probability theory seminar 28-03-25
tags: []
---

# MIPT probability theory seminar 28-03-25

516

[[589-неравенство-Маркова-Чебышева|неравенство Маркова-Чебышёва]]

# Модель случайного графа Эрдеша-Реньи (Erdos-Renye).

$n \in \NN$
$G_n \defeq G(n, p(n)) = (V_n, E_n)$
$\abs{V_n} = n$

В $V_n$ есть ребро $(u,v)$ с вероятностью $p$. 

$p(n): \NN \to [0,1]$

$T_n$ - кол-во треугольников в $G_n$.

# Claim
$p(n) = o(\frac{1}{n}) \implies P(T_n = 0) \to 1,\quad n \to \infty$ 
$p(n) = \Omega(\frac{1}{n}) \implies P(T_n = 0) \to 0,\quad n \to \infty$ 
$p(n) = O(\frac{1}{n}) \implies T_n \sim Poiss\group{\frac{c^3}{3!}}$ 

# Неравенство
$$
\forall \varepsilon > 0 \hthen
P\set{\abs{\xi - E\xi} \ge \varepsilon} \le \frac{D_\xi}{\varepsilon^2}
$$

# Пример
$X_1, \dots, X_n$ - НОРСВ
$\xi \defeq \ol{X} = \frac{1}{n} \sum{X_i}$ - среднее значение
$E_{X_i} = m,\quad D_{X_i} = \sigma^2$

$$
D\group{\sum{X_i}} = \sum{D_{X_i}} - 2 \sum_{i\neq j}{cov(X_i, X_j)}
$$ 
$$
E_{\xi} = m
$$
$$
D_\xi = \frac{\sigma^2}{n}
$$

# 72

