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

# Мартингал или хз

$\set{x_n}_{n \in \NN}$
$\set{F_n}_{n \in \NN}$ - **_фильтрация_**
$F_1 \subseteq F_2 \subseteq \dots$

1. $x_n \in F_n\text{-измеримо}$
2. $E\abs{x_n} < \infty$
3. $E(x_{n+1} \mid F_n) \stackrel{п.н.}{=} x_n$

# Claim

$(3) \same E(x_m \mid F_n) \stackrel{п.н.}{=} x_n,\quad \forall m > n$

## Proof:

$\Align{
E(x_m \mid F_n) = E(E(x_m \mid F_{m-1}) \mid F_n) \stackrel{п.н.}{=} 
E(x_{m-1} \mid F_n) \stackrel{п.н.}{=} \dots \stackrel{п.н.}{=} x_n
}$

# Claim

$$
E(x_m - x_n \mid F_n) = 0
$$

# Естественная фильтрация

$$
F_n = \sigma(x_1, \dots, x_n) \defeq \sigma(\sigma(x_1) \cup \dots \cup \sigma(x_n))
$$

# Пример мартингала

$$
\Gather{
x_n = \sum_{j=1}^{n}{\xi_j} \\
E \xi_j = 0 \\
\set{F_n} - \textit{естественная фильтрация}
}
$$

# Суб-мартингал

$$
E(x_{n+1} \mid F_n) \stackrel{п.н.}{\ge} x_n
$$

# Супер-мартингал

$$
E(x_{n+1} \mid F_n) \stackrel{п.н.}{\le} x_n
$$

# Мартингал Дуба

$\groupt{\Omega, F, P}$
$z$
$E \abs{z} < \infty$
$F_n \in F$

$$
x_n \defeq E(z \mid F_n)
$$

## Proof:

1. $\Align{
E\abs{x_n} = \abs{E(E(z \mid F_n))} \le 
E\abs{E(z \mid F_n)} \le
E(E\abs{z} \mid F_n) < \infty
}$

3. $\Align{
E(x_{n+1} \mid F_n) = E(E(z \mid F_{n+1}) \mid F_n) = E(z \mid F_n) = x_n
}$


# [[589-неравенство-Маркова-Чебышева|неравенство Маркова-Чебышева]]

# Формула свертки
$\xi_1,\xi_2$
 $\eta = \xi_1 + \xi_2$

 $$

$$

## Proof:
$\Align{
F_\eta(u) = P(\xi_1 + \xi_2 < u) = P(\xi_1 + \xi_2 < u) =
\int\int_{x+y < u}{f_{\xi_1\xi_2}(x,y) \d x \d y}
}$
