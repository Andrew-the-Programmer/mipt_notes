---
id: 319-mipt-computational-complexity-theory-lecture-18-04-25
aliases:
  - MIPT computational complexity theory lecture 18-04-25
tags: []
---

# MIPT computational complexity theory lecture 18-04-25

$$
TQBF \defeq \set{\psi \mid
\psi = Q_1 x_1 \dots Q_n x_n \varphi(x_1,\dots,x_n) = \top}
$$

# Theorem.

$$
TQBF \in \complete{PSpace}
$$

## Proof:

$\Align{
Напоминание:\\
\hline
G_M - \textit{конфигурационный граф} \\
K = 2^{O(s(n))} - \textit{кол-во состояний} \\
Path_G(a,b,k) \stackrel{def}{\same} \textit{в G есть путь из a в b длины} \le 2^k \\
Path_G(a,b,k) \same \exists u : Path_G(a,u,k-1) \land Path_G(u,b,k-1) \\
L \in PSpace(s),\quad L \sim M_L \\
x \in L \same Path_{G_M}(start,finish,\log K) \\
\hline
Идея:\\
Path_G(a,b,k)\\
\same\\
\exists u \forall x,y \group{
\group{(x=a \land y=u) \lor (x=u \land y=b)} \implies
Path_G(x,y,k-1)
}\\
\hline
}$

# Схема

