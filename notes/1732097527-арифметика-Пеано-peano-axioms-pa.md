---
id: 1732097527-арифметика-Пеано-peano-axioms-pa
aliases:
  - арифметика Пеано
  - Peano axioms
  - PA
tags: []
---

# арифметика Пеано-Peano axioms-PA
$$
\left(=, \cdot, +, 0, 1\right)
$$
$$
x \to x + 1
$$
$-$ биекция везде, кроме 0

***Аксиома индукции***
$$
(A(0) \land \forall n (A(n) \to A(n+1))) \to \forall n A(n)
$$
# Теорема Компактности
1. $$
\Gamma \not\vdash \bot \same
\forall \Gamma^{'} \subseteq \Gamma: \abs{\Gamma^{'}} < \infty \hthen
\Gamma^{'} \not\vdash \bot
$$
$\Gamma$ непротиворечива
$\same$
$\forall \Gamma^{'} \subseteq \Gamma: \abs{\Gamma^{'}} < \infty \hthen \Gamma^{'}$
непротиворечива
2. 
$\Gamma$ совместна
$\same$
$\forall \Gamma^{'} \subseteq \Gamma: \abs{\Gamma^{'}} < \infty \hthen \Gamma^{'}$
совместна
