---
id: 306-mipt-probability-theory-lecture-11-04-25
aliases:
  - MIPT probability theory lecture 11-04-25
tags: []
---

# MIPT probability theory lecture 11-04-25

# Свойство 12. Неравенство Йенсена

$g$ выпукла вниз

$$
E(g(\xi) \mid F_0) \ge g(E(\xi \mid F_0))
$$

## Proof:

$\Align{
g(y) \ge g(x) + d(x)(y-x) \\
y = \xi,\quad x = E(\xi \mid F_0) \stackrel{E(\cdot \mid F_0)}{\implies} \\
E(g(\xi) \mid F_0) \ge E(g(E(\xi \mid F_0)) \mid F_0) + 
E\groupr{\d (E(\xi \mid F_0)) \cdot (\xi - E(\xi \mid F_0)) \mid F_0} \\
E(g(\xi) \mid F_0) \ge g(E(\xi \mid F_0)) + 
\d (E(\xi \mid F_0)) E\groupr{\xi - E(\xi \mid F_0) \mid F_0} \\
E\groupr{\xi - E(\xi \mid F_0) \mid F_0} = 0 \\
E(g(\xi) \mid F_0) \ge g(E(\xi \mid F_0)) \\
\blacksquare
}$

# Theorem. О наилучшем квадратичном прогнозе (приближении)
$\E \xi^2 < \infty$
$\eta \in F_0\text{-измеримо}$
