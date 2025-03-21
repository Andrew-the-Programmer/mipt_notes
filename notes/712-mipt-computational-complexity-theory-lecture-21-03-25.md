---
id: 712-mipt-computational-complexity-theory-lecture-21-03-25
aliases:
  - MIPT computational complexity theory lecture 21-03-25
tags: []
---

# MIPT computational complexity theory lecture 21-03-25

# Вероятностная модель вычислений

# ПВМТ (Полиномиальная Вероятностная Машина Тьюринга)

$M(x,r)$ - МТ
$p$ - полином.
$r \in U\group{\set{0,1}^{p(\abs{x})}}$ - ветка вычислений
$U$ - равномерное распределение

Результат работы - случайная величина.

# PP

$$
\Gather{
L \in PP \\
\stackrel{def}{\same} \\
\exists\ \text{ПВМТ}\ M(x,r) : \\
\forall x \in L \hthen
P(M(x,r) = 1) > \frac{1}{2} \\
\forall x \not\in L \hthen
P(M(x,r) = 0) > \frac{1}{2} \\
}
$$

# BPP

$$
\Gather{
L \in BPP \\
\stackrel{def}{\same} \\
\exists\ \text{ПВМТ}\ M(x,r) : \\
\forall x \in L \hthen
P(M(x,r) = 1) \ge \frac{2}{3} \\
\forall x \not\in L \hthen
P(M(x,r) = 0) \ge \frac{2}{3} \\
}
$$

# RP

$$
\Gather{
L \in RP \\
\stackrel{def}{\same} \\
\exists\ \text{ПВМТ}\ M(x,r) : \\
\forall x \in L \hthen
P(M(x,r) = 1) \ge \frac{1}{2} \\
\forall x \not\in L \hthen
P(M(x,r) = 0) = 1 \\
}
$$

# coRP

$$
\Gather{
L \in \co{RP} \\
\stackrel{def}{\same} \\
\exists\ \text{ПВМТ}\ M(x,r) : \\
\forall x \in L \hthen
P(M(x,r) = 1) = 1 \\
\forall x \not\in L \hthen
P(M(x,r) = 0) \ge \frac{1}{2} \\
}
$$

# NP

$$
\Gather{
L \in \NP \\
\stackrel{def}{\same} \\
\exists\ \text{ПВМТ}\ M(x,r) : \\
\forall x \in L \hthen
P(M(x,r) = 1) > 0 \\
\forall x \not\in L \hthen
P(M(x,r) = 0) = 1 \\
}
$$

# coNP

$$
\Gather{
L \in \co\NP \\
\stackrel{def}{\same} \\
\exists\ \text{ПВМТ}\ M(x,r) : \\
\forall x \in L \hthen
P(M(x,r) = 1) = 1 \\
\forall x \not\in L \hthen
P(M(x,r) = 0) > 0 \\
}
$$

# Иерархия

![hi.png](assets/imgs/21-03-25_11-48-37_603_21-03-25_11-48-37_068.png)

# Theorem

$$
PH \subseteq P^{PP}
$$

## Proof

hard...

# Theorem

$$
NP \subseteq PP
$$

## Proof

Было док-во, но я проспал...

# Оценка Чернова

$X_1, \dots, X_n$ - независимые бернулевские случайные величины.
$X = \sum{X_i}$
$\mu = \bbE(X)$
$\delta \in (0,1)$

$$
\bbP(\abs{X - \mu} \ge \delta \mu) \le 2 e^{-\frac{\delta^2 \mu}{3}}
$$

# Theorem

$f,g: \NN \to (0,1)$.
$f,g$ вычислимы.

$$
\Gather{
L \in BPP_w \\
\stackrel{def}{\same} \\
\exists\ \text{ПВМТ}\ M(x,r) : \\
\forall x \in L \hthen
P(M(x,r) = 1) \ge f(n) + g(n) \\
\forall x \not\in L \hthen
P(M(x,r) = 0) \le f(n) - g(n) \\
(n \defeq \abs{x}) \\
}
$$
