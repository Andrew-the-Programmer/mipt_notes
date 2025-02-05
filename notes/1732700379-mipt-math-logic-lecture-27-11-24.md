---
id: 1732700379-mipt-math-logic-lecture-27-11-24
aliases:
  - MIPT math logic lecture 27-11-24
tags: []
---

# MIPT math logic lecture 27-11-24
# Examples
1. $\set{\Phi \mid \Phi-\text{тавтология}}$ - [[1730897304-разрешимый-рекурсивный-язык|разрешимое мн-во]].
2. $\set{\Phi \mid \Phi-\text{тавтология в алгебре Тарского}}$ - [[1730897304-разрешимый-рекурсивный-язык|разрешимое мн-во]].
$(\RR, =, <, \cdot, +, 0, 1)$

# Th 1
`Let:`
$\Gamma$ - [[1731501440-перечислимость|перечислимое]] мн-во формул.
`Then:`
$$
\mathrm{Th}_\Gamma \defeq \set{\Phi \mid \Gamma \vdash \Phi}
$$
$\mathrm{Th}_\Gamma$ - [[1731501440-перечислимость|перечислимое]] мн-во.

# Cor
$\mathrm{Valid} \defeq \set{\Phi \mid \Phi \text{общезначна}}$ - [[1731501440-перечислимость|перечислимое мн-во]].

# Th 3
$\mathrm{Valid}$ - [[1730897304-разрешимый-рекурсивный-язык|неразрешимо]].

# Th 4
$\mathrm{TAr} = \set{\Phi \mid \Phi-\text{тавтология в арифметике}}$
$(\NN, =, \cdot, +, 0, 1)$
$\mathrm{TAr}$ - [[1731501440-перечислимость|неперечислимо]].

#

$(\Sigma, R)$
$R = \set{l_i \to r_i \mid l_i, r_i \in \Sigma^*}$
$$
\Gather{
u \xrightarrow[R]{1} v \same
\exists (l \to r) \in R : l \subseteq u \land r \subseteq v
}
$$
	
$\mathrm{sT} \defeq \set{(\Sigma, R, u, v) \mid u \xrightarrow[R]{} v}$

# Th 5
$$
\mathrm{Halt} \le_m sT
$$

