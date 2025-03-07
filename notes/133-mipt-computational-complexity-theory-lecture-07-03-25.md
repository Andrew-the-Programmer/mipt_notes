---
id: 133-mipt-computational-complexity-theory-lecture-07-03-25
aliases:
  - MIPT computational complexity theory lecture 07-03-25
tags: []
---

# MIPT computational complexity theory lecture 07-03-25
$B \in \Sigma^*$
$$
P^B,\ \text{NP}^B
$$
ПДМТО - полиномиальные ДМТ с оракулом

# Def. (Типа арифметическая иерархия №2)

$$
\AlignCenter{
\Sigma_0^P \defeq P \\
\Sigma_{n+1}^p \defeq \set{L \mid \exists\ \text{ПДМТО}\ {N}^{(\cdot)} : 
\exists B \in \Sigma_{n}^{P} : L = Accept(N^B)
} \\
\Pi_n^P \defeq \co \Sigma_n^P
}
$$

# Свойства

$$
\Gather{
\Sigma_1^P = NP \\
}
$$

# Theorem. (Поста №2, возможно)
$$
\Sigma_n^P = \set{L \mid (
x \in L \same 
\exists y_1 \forall y_2 \dots \forall\exists y_n : P(x, y_1, \dots, y_n)
}
$$
$P$ - полиномиальный предикат
