---
id: 287-mipt-computational-complexity-theory-lecture-28-03-25
aliases:
  - MIPT computational complexity theory lecture 28-03-25
tags: []
---

# MIPT computational complexity theory lecture 28-03-25

$$
L_{BPP} \defeq \set{\group{M, x, 1^n} \mid P(M(x, time=n) = 1) \ge \frac{2}{3}}
$$
# Claim
$$
L_{BPP} \in \text{BPP-hard}
$$

# Theorem. Gacs-Sipser-Lautemann.
$$
BPP \subseteq \Sigma_2^P \cap \Pi_2^P
$$
$$
\AlignLeft{
L \in BPP \\
M(x,r) \textit{ работает за } q(\abs{x}) - полином \\
S_x \defeq \set{r \mid M(x,r) = 1} \\
m \defeq q(\abs{x}) \\
x \in L \implies \abs{S_x} - big,\quad
\abs{S_x} > \group{1 - \frac{1}{m}} 2^m \\
x \not\in L \implies \abs{S_x} - small,\quad 
\abs{S_x} < \frac{1}{m} 2^m \\
S_x + z \defeq \set{r + z \mid r \in S_x} \\
+ - \textit{побитовый xor}\\
x \in L \implies \exists \set{z_j}_{j=1}^{m} \subseteq \set{0,1}^m :
\bigcup_{j=1}^{m}{S_x + z_j} = \set{0,1}^m \\
x \not\in L \implies \abs{\bigcup_{j=1}^{m}{S_x + z_j}} < \abs{\set{0,1}^m} \implies 
\exists y \in \set{0,1}^m : y \not\in \bigcup_{j=1}^{m}\group{S_x + z_j} \\
P(\exists y \in \set{0,1}^m : y \not\in \bigcup_{j=1}^{m}\group{S_x + z_j}) \le 
2^m P(y \in \bigcup_{j=1}^{m}\group{S_x + z_j})
}
$$
