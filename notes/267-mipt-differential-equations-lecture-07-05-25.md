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

## Proof:

$W = \set{(\mu, x,y) \mid \mu \in U_\alpha(\mu_0), x \in U_\delta(x_0), \abs{y - \varphi_0} \le R}$ - трубка
В общем область в которой мы работаем

Колебания
$\Align{
\omega_f(\D \mu) = \max_W{\D f_\mu} = \max_W\group{f(x, y(\mu + \D \mu), \mu + \D \mu) - f(x,y(\mu), \mu)} \\
\omega_{y_0}(\D \mu) = \max_W{\D{{y_0}_\mu}} \\
\omega_{\cdot} \to 0, \quad \D {\mu} \to 0
}$

Ошибка:
$z(x,\mu,\D \mu) \defeq y(x,\mu+\D \mu) - y(x,\mu)$

Фиксируем $\D \mu$.
ЗК для ошибки:
$\Align{
\Cases{
\dv{x}{z} = \D f_\mu(x,y,\mu) = F \\
z(x_0) \defeq y_0(\mu + \D \mu) - y_0(\mu) = z_0(\mu)
}
}$

По ф-ле интегрального представления решения ЗК:
$z(x) = z_0 + \int_{x_0}^{x}{F \d \xi}$

$\Align{
z*0 \le \omega*{y*0}(\D \omega) \\
\int_{x_0}^{x}{F \d \xi} \le \omega_f(\D \mu) \delta
}$

$\abs{z} \to 0,\quad \D \mu \to 0$

$\blacksquare$

# Theorem. Дифференцируемость решения по параметру

## If:

1. $f(x,y,\mu) \in C$
2. $\exists \pdv{y_j}{f_i} \in C$
3. $\exists \pdv{\mu_j}{f_i} \in C$
4. $y_0 \in C^1_\mu$

## Then:

$\Align{
\exists \delta > 0, \exists \alpha > 0:\\
\forall x \in U_\delta(x_0), \forall \mu \in U_\alpha(\mu_0) \hthen
}$

$$
y(x, \mu) \in D_\mu
$$

$u_{ij} \defeq \pdv{\mu_j}{y_i}$ удовлетворяют уравнениям в вариациях

$$
\Cases{
\dv{x}{u_{ik}} = \pdv{\mu_k}{f_i} + \sum_{j}{\pdv{y_j}{f_i} u_{jk}} \\
u_{ik}(x_0) = \pdv{\mu_k}{(y_0)_i}
}
$$

## Proof:

it's joever

Доказать дифференцируемость довольно просто, воспользовавшись результатом из
док-ва прошлой теоремы. Но доказать ур-ие в вариациях тяжело.
