---
id: 601-mipt-computational-complexity-theory-lecture-11-04-25
aliases:
  - MIPT computational complexity theory lecture 11-04-25
tags: []
---

# MIPT computational complexity theory lecture 11-04-25

Опоздал опять...

# Сложность по памяти

$s: \NN \to \NN$

$$
\Gather{
DSpace(s) \\
NSpace(s)
}
$$

> Я бы написал определения, но они интуитивно понятны.

# Theorem.

Для любой МТ с конечной памятью, существует эквивалентная МТ, которая использует не больше памяти и всегда останавливается.

## Let:

МТ $M$ работает за $s$ по памяти.
$s$ [[496-конструируемая-по-времени-сложность|конструируемая по времени]]

## Then:

$\exists N \sim M,\quad N \in DSpace(s)$

# Claim

$$
[D|N]Time(f) \subseteq [D|N]Space(f)
$$

$f = \Omega(\log n)$ и [[496-конструируемая-по-времени-сложность|конструируемая по времени]]

$$
[D|N]Space(f) \subseteq [D|N]Time(2^{O(f)})
$$

# PSpace

$$
\Gather{
PSpace \defeq \bigcup_{k\in\NN}{DSpace(n^k)} \\
NPSpace
}
$$

# Claim

$$
P \subseteq PSpace \subseteq Exp
$$

# Theorem. Сэвича (Savitch)

$s$ конструируемая по памяти.
$s = \Omega(\log n)$

$$
NSpace(s) \subseteq DSpace(s^2)
$$

## Proof:

$\Align{
Path_G(a,b,k) \stackrel{def}{\same} \textit{в G есть путь из a в b длины} \le 2^k \\
Path_G(a,b,k) \same \exists u : Path_G(a,u,k-1) \land Path_G(u,b,k-1) \\
L \in NSpace(s),\quad L \sim N \\
x \in L \same Path_{G_N}(start,finish,\log K) \\
n \defeq \abs{x} \\
K \defeq \abs{Q} \cdot O(n) \cdot \abs{\Gamma}^{s(n)} \cdot s(n) - \textit{кол-во всевозможных конфигураций} \\
\log(K) = O(s(n)) + O(\abs{N}) + O(\log n) = O(s(n)) + O(\abs{N}) \\
\textit{Нужно вычислить предикат по памяти за } O(s^2) \\
\alpha(m) = O(\log K) + \alpha(m-1) = O((\log K)^2) \\
}$

# Claim

$$
PSpace = NPSpace
$$

# .
$$
L_{Space} \defeq \set{\group{M, x, 1^n} \mid M\ \textit{принимает}\ x\ \textit{за память}\ n}
$$
$$
L_{Space} \in PSpace
$$

