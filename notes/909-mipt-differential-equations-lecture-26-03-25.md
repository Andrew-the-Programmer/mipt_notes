---
id: 909-mipt-differential-equations-lecture-26-03-25
aliases:
  - MIPT differential equations lecture 26-03-25
tags: []
---

# MIPT differential equations lecture 26-03-25

# АСДУ

автономная система ду

$$
\dv{t}{\vec{x}} = \vec{f}(x)
$$

# Lemma 1

АСОДУ можно свести к неавтономной в окр. точки неравновесия.

# Устойчивое решение

мало меняется при изменении начальных условий.

# Устойчивость по Ляпунову

Решение $\vec{x}(t)$ АСОДУ $\dv{t}{x} = f(x)$ называется **_устойчивым по Ляпунову_**, если:

1. $\forall x^\star \in U_\delta(x_0)$ - решение ЗК $\Cases{
\dv{t}{x} = f(x) \\
x(t_0) = x^\star
}$ существует $\forall t > t_0$

2. $$
   \forall \varepsilon > 0 \exists \delta_\varepsilon > 0 :
   \abs{x^* - x_0} < \delta_\varepsilon \implies
   \abs{\vec{x}(t, x^\star) - \vec{x}(t_0, x_0)} < \varepsilon
   $$

# Ассимптотическая устойчивость

1. Устойчивость по Ляпунову
2. $$
   \forall \varepsilon \exists \delta^\star \le \delta_\varepsilon :
   \forall 
   $$
