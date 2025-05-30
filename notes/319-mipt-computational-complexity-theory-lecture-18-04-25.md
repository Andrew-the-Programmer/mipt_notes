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

# Обновленная картина мира.

![18-04-25_11-37-59_701_IMG_20250418_113718.jpg](assets/imgs/18-04-25_11-37-59_701_IMG_20250418_113718.jpg)

# Def. $\mcL$

$$
\Gather{
\mcL \defeq DSpace(O(\log)) \\
N\mcL \defeq NSpace(O(\log)) \\
}
$$

# Theorem. Об иерархии по памяти.

## If:

$f,g \ge \log$
$f = o(g)$

## Then:

$$
DSpace(f) \subsetneq DSpace(g)
$$

## Proof:

$\Align{
L \defeq \set{\group{M, x} \mid 
\textit{M принимает x за} \le O(g(n))\ \textit{памяти и} \le 2^{O(g(n))}\ шагов} \\
Claim:\ L \in DSpace(g) \\
Claim:\ L \not\in DSpace(f) \\
}$

# .

$$
N\mcL \subseteq P
$$

# Def. Логарифмическая сводимость: $\le_{\log}^m$

$$
L_1 \le_{\log}^m L_2 \implies L_1 \le_p^m L_2
$$

$$
L_1 \le_{\log}^m L_2 \implies \group{L_2 \in [N]\mcL \implies L_1 \in [N]\mcL}
$$

Транзитивность:

$$
L_1 \le_{\log}^m L_2 \land L_2 \le_{\log}^m L_3 \implies L_1 \le_{\log}^m L_3
$$
