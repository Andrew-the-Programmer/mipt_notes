---
id: 1728831155-limsup-liminf
aliases:
  - limsup liminf
tags: []
---

# limsup liminf

## Definition
Пусть $\set{A_n}_{n \in \NN}$ - [[1728830216-система-множеств|система множеств]].
$$
\limsup_{n \to \infty}{A_n} \ldefeq
\set{x \mid \exists \set{A_{n_m}} \subseteq \set{A_n} : \forall m \in \NN \hthen x \in A_{n_m}} =
\set{x \mid \forall N \in \NN \hthen \exists n \ge N : x \in A_n}
$$
$$
\liminf_{n \to \infty}{A_n} \ldefeq
\set{x \mid \exists N \in \NN : \forall n \ge N \hthen x \in A_n}
$$
## Lemma 1
$$
\limsup_{n \to \infty}{A_n} = \bigcap_{N \in \NN}^{}{ \bigcup_{n \ge N}^{}{A_n}}
$$
$$
\liminf_{n \to \infty}{A_n} = \bigcup_{N \in \NN}^{}{ \bigcap_{n \ge N}^{}{A_n}}
$$
## Lemma 2
$$
\liminf_{n \to \infty}{A_n} \subseteq \limsup_{n \to \infty}{A_n}
$$
