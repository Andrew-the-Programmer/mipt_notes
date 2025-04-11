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
E(g(\xi) \mid F_0) \stackrel{п.н.}{\ge} g(E(\xi \mid F_0))
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

$E \xi^2 < \infty$

$$
\argmin_{\eta \in F_0\text{-измеримо}}{E(\xi - \eta)^2} = E(\xi \mid F_0)
$$

# Условное мат. ожидание отн. СВ
$$
E(\xi\mid\eta) \defeq E(\xi \mid \sigma(\eta))
$$

# .
$$
f_{\xi \mid \eta}(x \mid y) = \frac{f_{\xi\eta}(x,y)}{f_\eta(y)}
$$
$$
\Align{
E(\xi \mid \eta=y) = 
\int_{-\infty}^{\infty}{x f_{\xi \mid \eta}(x \mid y) \d x} = g(y) \\


}
$$
