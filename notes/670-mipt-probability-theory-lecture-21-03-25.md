---
id: 670-mipt-probability-theory-lecture-21-03-25
aliases:
  - MIPT probability theory lecture 21-03-25
tags: []
---

# MIPT probability theory lecture 21-03-25
# Векторная функция вероятности
# Функция распределения случайного вектора
# Свойства
# Lemma
$B_n \defeq \bigcup_{k=1}^{n}{\set{\omega \mid a_k \le \xi_k(\omega) < b_k}}$
$$
\Gather{
\forall D \in F \hthen \\
P(B_n D) = 
\sum_{\set{k_1, \dots, k_n} \in \set{0,1}^n}{
(-1)^{\sum{k_j}}
P\group{\bigcap_{j=1}^{n}\set{\omega \mid \xi_j(\omega) < x_j^{k_j}} \cap D}
}
}
$$
$x_j^0 \defeq b_j$
$x_j^1 \defeq a_j$ 

## Proof (by induction)
