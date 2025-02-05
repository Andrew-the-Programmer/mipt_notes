---
id: 1729967169-calculus-envelope-theorem
aliases:
  - calculus-envelope theorem
  - теорема о конверте
tags: []
---

# calculus-envelope theorem
## Lemma 1
`Пусть:`
1. $X$ - [[1729420318-абстрактное-множество|абстрактное множество]]
2. $P$ - [[1728840113-полукольцо|полукольцо]] на X
3. $\mu$ - [[1728917820-счетно-аддитивная-мера|счетно-аддитивная мера]] на $P$
4. $\mu^*$ - [[1729432519-верхняя-мера|верхняя мера]] $\mu$

`Тогда:`
$$
\gather{
\forall A \subseteq X : 
\left[\Array{l}{
\mu^*(A) < +\infty \\
\mu^* - \sigma\text{-конечная мера}
}\right. \hthen 
\exists B \in \mcM(P): \quad\\\\
A \subseteq B, \quad \mu^*(B \setminus A) = 0
}
$$
([[1729419707-sigma-конечная-мера|sigma-конечная мера]])
При этом:
$$
\alignleft{
B = \bigcap_{i\in\NN}{\bigcup_{j\in\NN}{P_{i,j}}}, \quad
P_{i,j} \in P \\
A \subseteq \bigcup_{j\in\NN}{P_{i,j}} \\
\sum_{j\in\NN}{\mu(P_{i,j})} \le \mu^*(A) + \varepsilon_i, \quad
\varepsilon_i \to 0, i \to \infty
}
$$
### Proof
$$
\alignleft{
\forall i \in \NN \hthen \exists \set{P_{i,j}} :
A \subseteq \bigcup_{j\in\NN}{P_{i,j}}, \\
\mu^*(A) + \frac{1}{2^i} \ge \sum_{j\in\NN}{\mu(P_{i,j})} \\
B_n \ldefeq \bigcap_{i=1}^{n}{\bigcup_{j\in\NN}{P_{i,j}}} \in \mcM_{\mu^*} \\
B \ldefeq \bigcap_{i\in\NN}{\bigcup_{j\in\NN}{P_{i,j}}} \in \mcM_{\mu^*} \\
A \subseteq B \subseteq B_n \\
\mu^*(A) \le \mu^*(B) \le \mu^*(B_n) \\
\mu^*(B_n) \le \mu^*\left(\bigcup_{j\in\NN}{P_{n,j}}\right) \le 
\sum_{j\in\NN}{\mu(P_{n,j})} \le \mu^*(A) + \frac{1}{2^n} \\
\inf_{n}{\mu^*(B_n)} = \mu^*(B) \le \mu^*(A) \\
\mu^*(A) \le \mu^*(B) \le \mu^*(A) \\
\blacksquare
}
$$ 
## Theorem
`Пусть:`
1. $X$ - [[1729420318-абстрактное-множество|абстрактное множество]]
2. $P$ - [[1728840113-полукольцо|полукольцо]] на X
3. $\mu$ - [[1728917820-счетно-аддитивная-мера|счетно-аддитивная мера]] на $P$
4. $\mu^*$ - [[1729432519-верхняя-мера|верхняя мера]] $\mu$

`Тогда:`
$$
\gather{
\forall B \subseteq \mcM_{\mu^*} :
\left[\Array{l}{
\mu^*(B) < +\infty \\
\mu^* - \sigma\text{-конечная мера}
}\right. \hthen 
\exists A, C \in \mcM(P) : \\\\
A \subseteq B \subseteq C, \quad \mu^*(C \setminus A) = 0
}
$$

### Proof
#### C.
Применим к B предыдущую лемму, получим C.
$$
B \subseteq C, \quad \mu^*(B) = \mu^*(C)
$$
#### A.
$$
D \ldefeq C \setminus B \\
$$
$$
\alignleft{
\mcM(P) \subseteq \mcM_{\mu^*} \implies C \in \mcM_{\mu^*} \implies
D \in \mcM_{\mu^*} 
}
$$
$$
D \in \mcM_{\mu^*}, \quad \mu^*(D) = 0 < +\infty
$$
Применим к $D$ предыдущую лемму, получим $D^*$.
$$
D \subseteq D^*, \quad \mu^*(D^*) = 0, \quad D^* \in \mcM(P)
$$
Пусть $A \ldefeq C \setminus D^*$
$$
\alignleft{
C,D^* \in \mcM(P) \implies A \in \mcM(P)
}
$$
$$
\gather{
\mu^*(A) = \mu^*(C) \implies \mu^*(C \setminus A) = 0
}
$$
#### End of the proof $\blacksquare$
