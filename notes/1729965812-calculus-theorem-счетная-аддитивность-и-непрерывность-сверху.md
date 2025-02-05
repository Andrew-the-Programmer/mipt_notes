---
id: 1729965812-calculus-theorem-счетная-аддитивность-и-непрерывность-сверху
aliases:
  - calculus theorem-счетная аддитивность и непрерывность сверху
  - теорема о счетной аддитивности и непрерывности сверху
tags: []
---

# Theorem - счетная аддитивность и непрерывность сверху
`Пусть:`
1. $M$ - [[1728833822-sigma-алгебра|sigma-алгебра]]
2. $\mu$ - [[1728917539-конечно-аддитивная-мера|конечно-аддитивная мера]] на $M$
3. $\mu$ - [[1728918993-конечная-мера|конечная мера]]

`Тогда:`
Утв. эквивалентны:
1. $\mu$ - [[1728917820-счетно-аддитивная-мера|счетно-аддитивная мера]]
2. $\mu$ [[1729108514-непрерывная-мера|непрерывна сверху]]
3. $\mu$ [[1729108514-непрерывная-мера|непрерывна сверху]] в нуле

## Proof
### $1 \implies 2$
>[[1729418369-теорема-эквивалентность-счетной-аддитивности-и-непрерывности-снизу|теорема об эквивалентности счетной аддитивности и непрерывности снизу]]

`Пусть:`
$$
\left\{ \begin{array}{l}
\set{A_i}_{i\in \NN} \subseteq M \\
A_{i+1} \subseteq A_{i} \\
A = \bigcap_{i \in \NN}^{}{A_i}
\end{array} \right.
$$
$$
\begin{gather}
B_i \ldefeq A_1 \setminus A_i, \quad B \ldefeq A_1 \setminus A \\
B \eq \bigcup_{i \in \NN}^{}{B_i} \in M \\
B_i \subseteq B_{i+1} \\
\mu(B) = \lim_{i \to \infty}{\mu(B_i)} =
\lim_{i \to \infty}{\left(\mu(A_1) - \mu(A_i)\right)} \implies \\
\exists \lim_{i \to \infty}{\mu(A_i)} = \mu(A_1) - \mu(B) = \mu(A) \quad \blacksquare
\end{gather}
$$

### $2 \implies 3$
очевидно.

### $3 \implies 1$

`Пусть:`
$$
\left\{ \begin{array}{l}
\set{A_i}_{i\in \NN} \subseteq M \\
A = \bigsqcup_{i \in \NN}^{}{A_i}
\end{array} \right.
$$
$$
\begin{gather}
B_n \ldefeq \bigsqcup_{i=1}^{n}{A_i} \\
B_{n} \subseteq B_{n+1} \\
C_n \ldefeq A \setminus B_n \\
C_{n+1} \subseteq C_n \\
\bigcap_{n \in \NN}^{}{C_n} = A \setminus \bigcap_{n \in \NN}^{}{B_n} =
A \setminus A = \noneset \\
\exists \lim_{n\to \infty}{C_n} = 0 \\
A = C_n \sqcup B_n \\
\mu(A) = \mu(C_n) + \mu(B_n) = \lim_{n \to \infty}{\mu(C_n)} + \lim_{n \to \infty}{\mu(B_n)} = \\
= \lim_{n \to \infty}{\bigsqcup_{i=1}^{n}{A_i}} =
\lim_{n \to \infty}{\sum_{i=1}^{n}{\mu(A_i)}} = \sum_{i \in \NN}^{}{A_i}
\quad\blacksquare
\end{gather}
$$

### End of the proof $\blacksquare$
