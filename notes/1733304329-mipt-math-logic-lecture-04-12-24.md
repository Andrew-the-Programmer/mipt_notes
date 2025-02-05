---
id: 1733304329-mipt-math-logic-lecture-04-12-24
aliases:
  - MIPT math logic lecture 04-12-24
tags: []
---

# MIPT math logic lecture 04-12-24
$sT_R = \set{(u,v) \mid u \xrightarrow[R]{} v}$

# Th 1
$\exists U : sT_U \not\in \mcR$
$U$ - [[1730292465-универсальная-машина-Тьюринга-МТ|универсальная МТ]]

***Полугруппа***
$(G, \cdot)$
$a(bc) = (ab)c$
$\Sigma = \set{a_i} \subseteq G$
$R = \set{u_i = v_i \mid u_i,v_i \in \Sigma^*}$ 
$\xleftrightarrow[R]{*}$ - [[1730027331-отношение-эквивалентности|отношение эквивалентности]]
$\mathrm{Valid}$
$\mathrm{Eq} = \set{(\Sigma, R, u, v) \mid u \xrightarrow[R]{} v}$
# Th 2
$$
\mathrm{Eq} \le_m \mathrm{Valid}
$$ 
$$
\alignleft{
f: \mathrm{Eq} \to \mathrm{Valid} \\
}
$$
Сигнатура:
$E$ - бинарный предикат 
$a_1, \dots, a_n$ - унарные ф-ии

$\Re f = \forall x E(x, x)$
$Symm = \forall x \forall y (E(x, y) \to E(y, x))$
$Trans = \forall x \forall y \forall z (E(x, y) \land E(y, z) \to E(x, z))$
$A_i = \forall x \exists y (E(x, y) \to E(a_i(x), a_j(y)))$ 
$R(u,v) = \forall x E(u_1 \cdot \dots \cdot u_s (x), v_1 \cdot \dots \cdot v_r (x))$ 

# Th 3
$\mathrm{Ar}$ не [[1731501440-перечислимость|перечислим]].
