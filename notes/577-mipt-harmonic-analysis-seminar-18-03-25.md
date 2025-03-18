---
id: 577-mipt-harmonic-analysis-seminar-18-03-25
aliases:
  - MIPT harmonic analysis seminar 18-03-25
tags: []
---

# MIPT harmonic analysis seminar 18-03-25

# Свойства свертки ф-ий

# Апроксимационная единица на алгебре X

$$
\exists \set{\varphi_n}_{n\in\NN}:
\forall f \in X \hthen \norm{\varphi_n f - f} \to 0, \quad n \to \infty
$$

# Полная система

$X$ - [[416-банахово-пространство|банахово пространство]]
$\set{e_n} \subseteq X$

$$
\Gather{
\ol{\lin\set{e_n}} = X (замыкание) \\
\forall x \in X \forall \varepsilon > 0 \hthen
\exists \set{n_k}_{k=1}^{N}, \set{\alpha_k}_{k=1}^{N} \in \RR : \\
\norm{\sum_{k=1}^{N}{\alpha_k e_{n_k}} - x} < \varepsilon \\
}
$$

## Пример 1

$\set{x^n}_{n\in\NN} \subseteq L_2[-1,1]$ - базис?
Да.

## Пример 2
$\set{P_n \defeq \dv[n]{x}{} (1+x^2)^n}_{n\in\NN} \subseteq L_2[-1,1]$ - базис?
