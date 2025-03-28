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
