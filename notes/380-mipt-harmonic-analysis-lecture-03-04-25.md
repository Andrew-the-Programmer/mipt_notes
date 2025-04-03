---
id: 380-mipt-harmonic-analysis-lecture-03-04-25
aliases:
  - MIPT harmonic analysis lecture 03-04-25
tags: []
---

# MIPT harmonic analysis lecture 03-04-25

# Интеграл зависимый от параметра

Бывают собственные и несобственные.

$f : X \times Y \to \ol{\RR}$
$\forall y \hthen f \in L_1(X)$

$$
J(y) \defeq \int_X{f(x,y) \d \mu(x)}
$$

# Вопросы?

1. Когда можно интегрировать по параметру?
2. Дифференцировать?
3. Переходить к пределу?

# Ответы!

1. Практически т. Фубини

# Theorem 1.

Пусть:

1. $Y \defeq (Y, d)$ - [[1728837879-метрическое-пространство|метрическое пространство]]
2. $y_0$ - предельная точка в Y (сущ. посл-ть к y)
3. $X_0 \subset X$ :

4. $\mu(X \setminus X_0) = 0$
5. $\forall x \in X_0 \hthen \exists \lim_{y\to y_0}{f(x,y)} \defeq f_0(x)$
6. $
\exists g \in L_1(X) : \forall \delta > 0 \hthen \abs{f(x,y)} \le g(x)\quad
\forall x \in X_0 \forall y \in B_\delta(y_0)
$
   Тогда:
   $f_0 \in L_1(X)$
   $$
      \exists \lim_{y\to y_0}{\int_X{f(x,y) \d \mu(x)}} = \int_X{\lim_{y\to y_0} f(x,y) \d \mu(x)}
   $$

# Theorem 2

