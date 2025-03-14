---
id: 181-mipt-computational-complexity-theory-lecture-14-03-25
aliases:
  - MIPT computational complexity theory lecture 14-03-25
tags: []
---

# MIPT computational complexity theory lecture 14-03-25
$$
\AlignCenter{
\Sigma_n\ \text{SAT} \defeq \set{
\varphi \mid \exists y_1 \forall y_2 \dots \exists\forall y_n :
\varphi(y_1, \dots, y_n) = 1
} \\
\Pi_n\ \text{SAT} \defeq \set{
\varphi \mid \forall y_1 \exists y_2 \dots \forall\exists y_n :
\varphi(y_1, \dots, y_n) = 1
} \\
}
$$
$$
\AlignCenter{
\Sigma_n\ \text{SAT} \in \complete{\Sigma_n^P} \\
\Pi_n\ \text{SAT} \in \complete{\Pi_n^P}
}
$$

$$
L_n \defeq \set{Q_1 y_1 \dots Q_n y_n \varphi(y_1, \dots, )}
$$
