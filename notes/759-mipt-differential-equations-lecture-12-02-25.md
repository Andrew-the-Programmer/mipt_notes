---
id: 759-mipt-differential-equations-lecture-12-02-25
aliases:
  - MIPT differential equations lecture 12-02-25
tags: []
---
# MIPT differential equations lecture 12-02-25

![[1739346552.png]]

# Def. Функционал

![[1739346602.png]]

## Примеры

![[1739346720.png]]

# Непрерывность

$J \in C(f_0)$

$$
\forall \varepsilon > 0 \exists \delta > 0 \forall f \in M \hthen
\abs{J(f) - J(f_0)} < \varepsilon
$$

$$
\norm{J(f) - J(f_0)}_{C} \defeq \sup_{x \in X}{\abs{f - f_0}(x)}
$$

$$
\norm{J(f) - J(f_0)}_{{C}^{'}} = \sup_{x \in X}{\abs{f - f_0}(x)} + \sup_{x \in X}{\abs{{f}^{'} - f_0^{'}}(x)}
$$

![[1739347540.png]]

$$
\norm{J(f) - J(f_0)}_{C^k} \defeq \sum_{i=1}^{k}{\sup_{x \in X}{\abs{f^{(i)} - f_0^{(i)}}(x)}}
$$
$$
M_k = \set{f \in M \mid f \in C^k(X)}
$$

# Дифференцируемость
$$
f = A \D x + o(\D x)
$$

## Линейный функционал
$L[y]$

- $L$ непрерывен
-  $$
\Gather{
\forall \alpha, \beta \in \CC, \forall f_1, f_2 \in M_k \hthen \\
L[\alpha f_1 + \beta f_2] = \alpha L[f_1] + \beta L[f_2]
}
$$

# Вариация функционала
$y \in M$
$y + h \in M$
$$
\D J = J[f + h] - J[f] = L[y,h] + o(\norm{h}_{C^k})
$$
