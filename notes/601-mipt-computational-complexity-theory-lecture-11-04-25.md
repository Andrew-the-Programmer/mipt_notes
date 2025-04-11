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
Path_G(a,b,k) \same \textit{в G есть путь из a в b длины} \le 2^k \\
Path_G(a,b,k) \same \exists u : Path_G(a,u,k-1) \land Path_G(u,b,k-1) \\

}$

# Claim
$$
PSpace = NPSpace
$$
