---
id: 987-mipt-probability-theory-lecture-04-04-25
aliases:
  - MIPT probability theory lecture 04-04-25
tags: []
---

# MIPT probability theory lecture 04-04-25

# Def. Условное мат. ожидание

$\set{\Omega, F, P}$ - [[613-вероятностное-пространство|вероятностное пространство]]
$F_0 \subseteq F$
$\set{\Omega, F_0, P}$

$$
\eta \defeq E(\xi \mid F_0)
$$

$$
\forall A \in F_0 \hthen E(\xi I_A) = E(\eta I_A)
$$

# Свойства:

1. $\xi - F_0-\textit{измеримо},\quad \sigma(\xi) \subseteq F_0 \implies E(\xi \mid F_0) \stackrel{п.н.}{=} \xi$
2. $E(const \mid F_0) = const$
3. $E(\xi \mid \set{\emptyset, \Omega}) = E\xi$
4. $E\xi = E(E(\xi \mid F_0))$

# Theorem

1. $F_0 = \sigma_\min\group{\set{D_n}_{n \in \NN}}
\bigcup{D_n} = \Omega
$$
$$
E(\xi \mid F_0) = \sum_{n \in \NN, P(D_n) \neq 0}{\frac{E(\xi I_{D_n})}{P(D_n)} I_{D_n}}
$$
