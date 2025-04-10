---
id: 583-mipt-harmonic-analysis-lecture-10-04-25
aliases:
  - MIPT harmonic analysis lecture 10-04-25
tags: []
---

# MIPT harmonic analysis lecture 10-04-25

Лекция онлайн, Александр Иванович заболел (╥﹏╥)

# Теорема с прошлой лекции

# Theorem. О дифференцировании несобственного интеграла по параметру.

## If:

1. $f : [a,b) \times [c,d] \to \RR$
2. $f \in C$
3. $f \in C_y^1$ ($\forall x,y \hthen \exists f_y(x,y),\quad f_y \in C$)
4. $\int_a^{\to b}{f_y(x,y) \d x}$ сх-ся равномерно
5. $\int_a^{\to b}{f(x,y) \d x}$ сх-ся для всех $y \in [c,d]$

## Then:

$$
\pdv{y}{}\groupr{\int_a^{\to b}{f(x,y) \d x}} = \int_a^{\to b}{\pdv{y}{f}(x,y) \d x}
$$

![10-04-25_19-19-47_342.png](assets/imgs/10-04-25_19-19-47_342.png)

# Напоминание

![10-04-25_19-30-19_522.png](assets/imgs/10-04-25_19-30-19_522.png)

# Апроксимационная единица

$\set{\omega_t}$

1.  $\omega_t \in C_0^{\infty}$
2.  $\int{\omega_t \d x} = 1$
3.  $\forall \delta > 0
\int_{\RR^n \setminus B_\delta(0)}{\omega_t \d x} \to 0,\quad t \to 0
$

# Corollary 1.

$$
f \in L_1^{loc} \implies f \star \omega_t \in C_0^{\infty}
$$

![10-04-25_19-47-07_659.png](assets/imgs/10-04-25_19-47-07_659.png)
![10-04-25_19-47-27_754.png](assets/imgs/10-04-25_19-47-27_754.png)

# Corollary 2.

$$
C_0^{\infty}\ \textit{полно в}\ L_p^{loc}
$$

![10-04-25_19-47-48_796.png](assets/imgs/10-04-25_19-47-48_796.png)

# Theorem. Признак Дирихле
