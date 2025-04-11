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

# Theorem. Выполняется ИС

$$
\Align{
E(\xi \mid \eta=y) =
\int_{-\infty}^{\infty}{x f_{\xi \mid \eta}(x \mid y) \d x} = g(y) \\
E(E(\xi \mid \eta) I(\eta \in B)) = \\
\int\int{g(y) f_\eta(y) I_B(y) \d y} = \\
\int{\groupr{\int{x \frac{f_{\xi\eta}(x,y)}{f_\xi(y)} \d x}} I_B(y) f_\eta(y) \d y} =  \\
\int{\groupr{\int{x f_{\xi\eta}(x,y) \d x}} I_B(y) \d y} = \\
\int\int{x I_B(y) f_{\xi\eta}(x,y) \d x \d y} = \\
E(\xi I(\eta \in B))
}
$$

# .

$\set{x_n}_{n \in \NN}$
$\set{F_n}_{n \in \NN}$
$F_1 \subseteq F_2 \subseteq \dots$ 

1. $x_n \in F_n\text{-измеримо}$ 
2. $E\abs{x_n} < \infty$
3. $E(x_{n+1} \mid F_n) \stackrel{п.н.}{=} x_n$

# Claim

$(3) \same E(x_m \mid F_n) \stackrel{п.н.}{=} x_n,\quad \forall m > n$

## Proof:
$\Align{
E(x_m \mid F_n) = E(E(x_m \mid F_{m-1}))
}$
