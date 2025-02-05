---
id: 1729975203-calculus-theorem-теорема-о-единственности-продолжения-меры-по-Каратеодори
aliases:
  - calculus theorem теорема о единственности продолжения меры по Каратеодори
  - теорема о единственности продолжения меры по Каратеодори
  - теореме о единственности продолжения меры по Каратеодори
tags: []
---

# Теорема - единственность продолжения меры по Каратеодори
`Пусть:`
1. X - [[1729420318-абстрактное-множество|абстрактное множество]]
2. $P$ - [[1728840113-полукольцо|полукольцо]] на $X$
3. $\mu$ - [[1728917820-счетно-аддитивная-мера|счетно-аддитивная мера]] на $P$
4. $\mu^*$ - [[1729432519-верхняя-мера|верхняя мера]] $\mu$
5. $M_{\mu^*}$ - [[1729605960-измеримые-по-Каратеодори-множества|измеримые по Каратеодори множества]]
6. $M_\nu$ - [[1728833822-sigma-алгебра|sigma-алгебра]] на $X$ : $P \subseteq M_\nu$
8. $\nu$ - продолжение $\mu$ на $\mcM_\nu$ 
7. $\nu$ - [[1728917820-счетно-аддитивная-мера|счетно-аддитивная мера]] на $M_\nu$
`Тогда:`
$$
\Gather{
\forall A \in M_{\mu^*} \cap M_\nu : 
\left[\Array{l}{
\mu^*(A) < +\infty \\
\mu^* - \sigma\text{-конечная мера}
}\right. \hthen
\nu(A) = \mu^*(A)
}
$$
([[1729419707-sigma-конечная-мера|sigma-конечная мера]])
### Proof
#### 1. $\nu(A) \le \mu^*(A)$
`Пусть:` $A \subseteq \bigcup_{i\in\NN}^{}{P_i},\quad P_i \in P$
$$
\begin{gather}
\nu(A) \le \sum_{i\in\NN}^{}{\nu(P_i)} = \sum_{i\in\NN}^{}{\mu(P_i)} \mid inf\\
\nu(A) \le \mu^*(A)
\end{gather}
$$
#### 2.
`Пусть:` $p \in P,\quad \mu(p) < +\infty,\quad A \in M_{\mu^*} \cap M_\nu$
$p \cap A \in M_{\mu^*} \cap M_\nu$
$p \setminus A \in M_{\mu^*} \cap M_\nu$
$\nu(p \cap A) \le \mu^*(p \cap A)$
`Предположим:` $\nu(p \cap A) < \mu^*(p \cap A)$
$$
\mu(p) = \mu^*(p) = \mu^*(p \cap A) + \mu^*(p \setminus A) >
\nu(p \cap A) + \nu(p \setminus A) =
\nu(p) = \mu(p)
$$
$$
\aligncenter{
\nu(p \cap A) = \mu^*(p \cap A)\\
\nu(p \setminus A) = \mu^*(p \setminus A)
}
$$
$$
\alignleft{
\mu^*(A) < +\infty \implies \exists \set{A_i} \subseteq P :
A \subseteq \bigcup_{i\in\NN}^{}{A_i}\\
\bigcup_{i\in\NN}^{}{A_i} = \bigsqcup_{i\in\NN}^{}{Q_i},\quad Q_i \in P \\
\mu^*(A) \le \sum_{i\in\NN}^{}{A \cup Q_i} =
\sum_{i\in\NN}^{}{\nu(A \cup Q_i)} =
\nu(A) \\
\mu^*(A) \le \nu(A)
}
$$
