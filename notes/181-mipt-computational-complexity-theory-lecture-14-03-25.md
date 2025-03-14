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
TQBF \defeq \set{Q_1 y_1 \dots Q_n y_n\ \varphi(y_1, \dots, y_n) = 1,\quad n \in \NN}
$$

$TQBF \in PH \implies PH\ \textit{схлопывается}$

# Альтернирующие МТ

Альтернативное определение арифм. иерархии ($\Sigma_n^P$).
Это не очень нужно в курсе.

# BGS-theorem

$$
\exists A, \exists B : \Cases{
\P^A = \NP^A \\
\P^B \neq \NP^B
}
$$

## Proof
$$
\AlignLeft{
A \defeq \set{\group{M, x, 1^n} \mid M - ДМТ\ расспознает\ x\ за\ 2^n} \\
A \in EXP \\
A \in \complete{EXP} \\
L \in EXP, M\ \textit{принимает}\ L\ за\ 2^{p(\abs{x})} \implies \\
x \to \group{M, x, 1^{p(\abs{x})}} \\
EXP \subseteq P^A \subseteq NP^A \subseteq EXP^A \subseteq EXP \\
\implies P^A = NP^A \\
\hline
\Gamma \defeq \set{0,1}
D \subseteq \Gamma^* \\
len(D) \defeq \set{1^n \mid \exists x \in \Gamma^n \cap D} \\
len(D) \in \NP^D \\
\textit{Show that: } \exists B \in \Gamma^* : 
len(B) \not\in P^B \\
💀\dots \blacksquare \\
}
$$
# Theorem 2
$$
P_L(\P^L \neq \NP^L) = 1
$$
Вероятность того, что $\P^L = \NP^L$ относительно случайного $L$, равна 0.

# Пример
$$
P_L(A^L \neq B^L) = 1 \centernot\implies A \neq B
$$
$$
PSpace = IP
$$

# Theorem Mahaney.
Разреженный язык.
$$
A \in \set{0,1}^* : \exists p(n) - \textit{polynomial} : \abs{A \cap \set{0,1}^n} \le p(n)
$$
