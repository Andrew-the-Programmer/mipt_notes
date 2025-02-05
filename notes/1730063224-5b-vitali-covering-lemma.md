---
id: 1730063224-5b-vitali-covering-lemma
aliases:
  - 5B covering lemma
  - Vitali covering lemma
tags: []
---

# 5B | Vitali - covering lemma
https://en.wikipedia.org/wiki/Vitali_covering_lemma
[[1730067645-лемма-Цорна-zorn's-lemma|Zorn's lemma]]

$B = B(x,r)$ - [[1730025394-шар|ball]],  $c \ge 0$
$cB \ldefeq B(x,c \cdot r)$

# Theorem
`Let:`
1. $X$ - [[1730065170-separable-metric-space|separable metric space]]
2. $F$ - set of [[1730025394-шар|balls]] in $X$
3. $R \ldefeq \sup_{B \in F}\left\{rad(B)\right\} \in \RR$
`Then:`
$\exists G \subseteq F : \abs G \le \abs \NN$
$$
\bigcup_{B \in F}{B} \subseteq \bigcup_{C \in G}{5C} \\
$$
$$
\aligncenter{
\forall B \in F \hthen \exists C \in G : \quad
B \cap C \neq \noneset \land B \subseteq 5C \\
\forall C_1, C_2 \in G \hthen C_1 \cap C_2 = \noneset
}
$$
## Proof
Let: 
$$
\aligncenter{
F_n \ldefeq \set{B \in F : \frac{R}{2^{n+1}} < rad(B) \le \frac{R}{2^n}} \\
}
$$
$H_0 \ldefeq F_0$
$G_0$ - maximal disjoint subcollection of $H_0$
$$
\aligncenter{
H_{n+1} \ldefeq \set{B \in F_{n+1} \mid
B \cap C = \emptyset \quad \forall C \in \bigsqcup_{i=0}^{n}{G_i}} \\
}
$$
$G_{n+1}$ - maximal disjoint subcollection of $H_{n+1}$

$\abs{G_{n}} < +\infty$
$$
G \ldefeq \bigsqcup_{n\in\NN}{G_n}
$$
$$
\alignleft{
\forall B \in F_n \hthen \\
\exists C \in \bigsqcup_{i=0}^{n}{G_n}: \quad B \cap C \neq \noneset \implies \\
B \subseteq 5C
}
$$
$\blacksquare$
