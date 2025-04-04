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

(Интегральное Свойство - ИС)

$$
\forall A \in F_0 \hthen E(\xi I_A) = E(\eta I_A)
$$

# Свойства:

1. $\xi - F_0-\textit{измеримо},\quad \sigma(\xi) \subseteq F_0 \implies E(\xi \mid F_0) \stackrel{п.н.}{=} \xi$
2. $E(const \mid F_0) = const$
3. $E(\xi \mid \set{\emptyset, \Omega}) = E\xi$
4. $E\xi = E(E(\xi \mid F_0))$
5. $E(\alpha \xi + \beta \eta \mid F_0) = \alpha E(\xi \mid F_0) + \beta E(\eta \mid F_0)$

# Theorem

## If:

1. $F_0 = \sigma_\min\group{\set{D_n}_{n \in \NN}}$
2. $\bigcup{D_n} = \Omega$

## Then:

$$
E(\xi \mid F_0) = \sum_{n \in \NN, P(D_n) \neq 0}{\frac{E(\xi I_{D_n})}{P(D_n)} I_{D_n}}
$$

# Теорема Радона-Никодима

$\set{\Omega, F, P}$ - [[613-вероятностное-пространство|вероятностное пространство]]
$P$ - $\sigma$-конечная мера

# Свойство линейности.

$$
E(\alpha \xi + \beta \eta \mid F_0) = \alpha E(\xi \mid F_0) + \beta E(\eta \mid F_0)
$$

# Lemma. Свойство 6.

$$
\xi \stackrel{п.н.}{\ge} 0 \implies
E(\xi \mid F_0) \stackrel{п.н.}{\ge} 0
$$

# Lemma. Свойство 6-1.

$$
\xi \stackrel{п.н.}{\ge} \eta \implies
E(\xi \mid F_0) \stackrel{п.н.}{\ge} E(\eta \mid F_0)
$$

# Lemma. Свойство 6-2.

$$
a \le \xi \le b,\quad a,b - F_0-\textit{измеримые} \implies
(п.н.)\ a \le E(\xi \mid F_0) \le b
$$

# ?

$$
\Gather{
E(\xi - E(\xi \mid F_0) \mid F_0) = 0 \\
E(\xi - E(\xi \mid F_0)) = 0 \\
}
$$

# Lemma. Свойство 7.

$$
\abs{E(\xi \mid F_0)} \le E(\abs{\xi} \mid F_0)
$$

# Lemma. Свойство 8.

$$
\sigma(\xi) \perp F_0 \implies E(\xi \mid F_0) \stackrel{п.н.}{=} E\xi
$$

# Lemma. Свойство 9. Телескопическое свойство.

$F_0 \subseteq F_1 \subseteq F \implies$

$$
E(E(\xi \mid F_0) \mid F_1) = E(E(\xi \mid F_1) \mid F_0) = E(\xi \mid F_0)
$$

# Lemma. Свойство 10.

$0 \le \xi_n \uparrow \xi,\quad E\xi < \infty \implies$

$$
E(\xi_n \mid F_0) \uparrow E(\xi \mid F_0)
$$
# Lemma. Свойство 11.

$\xi - F_0-\textit{измеримо}$
$E\abs{\eta} < \infty$
$E\abs{\xi\eta} < \infty$
$$
E(\xi\eta \mid F_0) = \xi E(\eta \mid F_0)
$$
