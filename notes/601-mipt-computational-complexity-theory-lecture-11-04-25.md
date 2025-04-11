---
id: 601-mipt-computational-complexity-theory-lecture-11-04-25
aliases:
  - MIPT computational complexity theory lecture 11-04-25
tags: []
---

# MIPT computational complexity theory lecture 11-04-25

Опоздал опять...

# Сложность по памяти

$s: \Gamma^* \to \NN$

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

$M \in DSpace(s)$
$s$ [[496-конструируемая-по-времени-сложность|конструируемая по времени]]

## Then:

$\exists N \in DSpace(s)$
