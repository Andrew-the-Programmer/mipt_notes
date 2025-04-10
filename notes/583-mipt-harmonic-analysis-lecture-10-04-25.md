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
