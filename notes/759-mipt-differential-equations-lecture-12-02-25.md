---
id: 759-mipt-differential-equations-lecture-12-02-25
aliases:
  - MIPT differential equations lecture 12-02-25
  - лемма Дюбуа-Реймона
  - основная теорема вариационного исчисления
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
- Линейность $$
  \Gather{
  \forall \alpha, \beta \in \CC, \forall f_1, f_2 \in M_k \hthen \\
  L[\alpha f_1 + \beta f_2] = \alpha L[f_1] + \beta L[f_2]
  }
  $$

# Вариация функционала

## Опр. по Фреше

$y \in M$
$y + h \in M$
$h$ - допустимое приращение

$$
\D J[h] \defeq J[f + h] - J[f] = L[y,h] + o(\norm{h}_{C^k})
$$

## Опр. Гато

Первая вариация

$$
\delta J_y[h] = \Dv{t}{J[y + th]} \rvert_{t=0}
$$

## Lemma

$\exists\ \D J[h] \implies \exists\ \delta J[h] \land \D J = \delta J$

$$
\AlignLeft{

}
$$

# Экстремум

$y_0 \in M_k$

$$
\forall y \in M_k : \norm{y - y_0}_{C^k} \le \delta \hthen
J[y] < J[y_0] (>)
$$

# Lemma (вариация в экстремуме)

$y_0 \in M_1$ - экстремум $\implies$
$$
\delta J_{y_0}[h] = 0
$$

# Lemma
$y \in M_1$
$J[y] = \int_{X}{F(x,y,{y}^{(1)}) \d \mu}$
$F \in C^2$
 $$
\exists \delta J_y[h] = \int_X{\left(F_y h + F_{{y}^{(1)}} {h}^{(1)}\right)\d x}
$$
![[1739350684.png]]
![[1739350691.png]]

# Theorem. Основная теорема вариационного исчисления.
$$
\AlignLeft{
\mu(X) > 0 \\
\Phi \in C(X) \\
\forall h \in C^1(X) \hthen
\int_X{\Phi(x) h(x) \d x} = 0 \implies \Phi \equiv 0 
}
$$

# Лемма. Дюбуа-Реймона.
$$
\AlignLeft{
X = [a,b] \\
\exists h \in C^1(X): \quad
h(a) = h(b) = 0, \quad
\int_X{\Phi(x) h^{'}(x) \d x} = 0 \\
\implies \\
\Phi \equiv const
}
$$
