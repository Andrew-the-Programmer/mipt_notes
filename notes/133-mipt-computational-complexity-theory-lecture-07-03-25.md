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

# Def. (типа арифметическая иерархия №2)

$$
\AlignCenter{
\Sigma_0^P \defeq P \\
\Sigma_{n+1}^p \defeq \set{L \mid \exists\ \text{ПДМТО}\ {N}^{(\cdot)} : 
\exists B \in \Sigma_{n}^{P} : L = Accept(N^B)
} \\
\Pi_n^P \defeq \co \Sigma_n^P \\
PH \defeq \bigcup{\Sigma_n^P}
}
$$

# Свойства

$$
\Gather{
\Sigma_1^P = NP \\
\Sigma_n^P \cup \Pi_n^P \subseteq \Sigma_{n+1}^P \cap \Pi_{n+1}^P \\
}
$$

# Theorem. (типа т. Поста №2)
$$
\Sigma_n^P = \set{L \mid \group{
x \in L \same 
\exists y_1 \forall y_2 \dots \forall\exists y_n : P(x, y_1, \dots, y_n)
}}
$$
$P$ - полиномиальный предикат

# .
Пусть
1. $m,n > 0,\quad m \le n$
2. $\Sigma_m^P = \Pi_n^P$
Тогда
$$
\Sigma_m^P = \Sigma_{m+1}^P
$$

# Гипотезы.
1. $P \neq NP$
2. $NP \neq \co NP$
3. $NP \neq \co NP$
