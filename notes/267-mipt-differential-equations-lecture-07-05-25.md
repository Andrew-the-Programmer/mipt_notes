---
id: 267-mipt-differential-equations-lecture-07-05-25
aliases:
  - MIPT differential equations lecture 07-05-25
tags: []
---

# MIPT differential equations lecture 07-05-25

# Зависимость решения от параметров и начальных данных

Теоремка с прошлой лекции

Задача Коши

$$
\Cases{
\dv{x}{} \vec{y} = \vec{f}(x,\vec{y},\vec{\mu}) \\
y(x_0) = y_0(\mu)
}
$$

# Theorem

## If:

1. $f(x,y,\mu) \in C$
2. $\exists \pdv{y_j}{f_i} \in C$
3. $y_0(\mu) \in C$
4. $\exists \mu_0 : (x_0, y_0(\mu_0)) - \textit{НТ}$

## Then:

$\Align{
\exists \delta > 0, \exists \alpha > 0:\\
\forall x \in U_\delta(x_0), \forall \mu \in U_\alpha(\mu_0) \hthen
}$

$$
y(x, \mu) \in C_\mu
$$
