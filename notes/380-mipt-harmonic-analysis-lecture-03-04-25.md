---
id: 380-mipt-harmonic-analysis-lecture-03-04-25
aliases:
  - MIPT harmonic analysis lecture 03-04-25
tags: []
---

# MIPT harmonic analysis lecture 03-04-25

![1.jpg](assets/imgs/03-04-25_14-39-12_590_IMG_20250403_140357.jpg)

# Интеграл зависимый от параметра

Бывают собственные и несобственные.

# Собственные

$f : X \times Y \to \ol{\RR}$
$\forall y \hthen f \in L_1(X)$

$$
J(y) \defeq \int_X{f(x,y) \d \mu(x)}
$$

![2.jpg](assets/imgs/03-04-25_14-39-12_782_IMG_20250403_140402.jpg)

# Вопросы?

1. Когда можно интегрировать по параметру?
2. Дифференцировать?
3. Переходить к пределу?

![3.jpg](assets/imgs/03-04-25_14-39-12_411_IMG_20250403_140405.jpg)

# Ответы!

1. Практически т. Фубини

![4.jpg](assets/imgs/03-04-25_14-39-12_532_IMG_20250403_140637.jpg)

# Theorem 1.

## If:

1. $Y \defeq (Y, d)$ - [[1728837879-метрическое-пространство|метрическое пространство]]
2. $y_0$ - предельная точка в Y (сущ. посл-ть к y)
3. $X_0 \subset X$ :
4. $\mu(X \setminus X_0) = 0$
5. $\forall x \in X_0 \hthen \exists \lim_{y\to y_0}{f(x,y)} \defeq f_0(x)$
6. $
\exists g \in L_1(X) : \forall \delta > 0 \hthen \abs{f(x,y)} \le g(x)\quad
\forall x \in X_0 \forall y \in B_\delta(y_0)
$

## Then:

$f_0 \in L_1(X)$

$$
   \exists \lim_{y\to y_0}{\int_X{f(x,y) \d \mu(x)}} = \int_X{\lim_{y\to y_0} f(x,y) \d \mu(x)}
$$

## Photos:

![5.jpg](assets/imgs/03-04-25_14-39-12_574_IMG_20250403_141352.jpg)
![6.jpg](assets/imgs/03-04-25_14-39-12_329_IMG_20250403_141355.jpg)

## Proof:

![7.jpg](assets/imgs/03-04-25_14-39-12_208_IMG_20250403_141653.jpg)
![8.jpg](assets/imgs/03-04-25_14-39-12_466_IMG_20250403_141714.jpg)

# Theorem 2. Дифф. по параметру

## If:

1. $Y = \lceil c,d \rfloor$
2. $X_0 \subset X$ :
3. $\mu(X \setminus X_0) = 0$
4. $\forall x \in X_0, \forall y \in Y \hthen \exists \pdv{y}{f}$
5. $
\exists g \in L_1(X) : \forall \delta > 0 \hthen \abs{f_y(x,y)} \le g(x)\quad
\forall x \in X_0 \forall y \in B_\delta(y_0)
$

## Then:

$$
\exists \dv{y}{J}(y_0) = \int_X{f_y^{'}(x,y) \d \mu(x)}
$$

## Photos:

![9.jpg](assets/imgs/03-04-25_14-39-12_146_IMG_20250403_142411.jpg)
![10.jpg](assets/imgs/03-04-25_14-39-12_550_IMG_20250403_142608.jpg)

## Proof:

![10.jpg](assets/imgs/03-04-25_14-39-12_550_IMG_20250403_142608.jpg)
![11.jpg](assets/imgs/03-04-25_14-39-12_499_IMG_20250403_142613.jpg)
![12.jpg](assets/imgs/03-04-25_14-39-12_381_IMG_20250403_143140.jpg)
![13.jpg](assets/imgs/03-04-25_14-39-12_731_IMG_20250403_143223.jpg)

# Несобственные интегралы с параметром

![27.jpg](assets/imgs/03-04-25_15-26-02_257_IMG_20250403_151516.jpg)
![28.jpg](assets/imgs/03-04-25_15-26-02_662_IMG_20250403_151730.jpg)
![29.jpg](assets/imgs/03-04-25_15-26-02_288_IMG_20250403_151908.jpg)
![30.jpg](assets/imgs/03-04-25_15-26-02_989_IMG_20250403_152047.jpg)

# Несобственный интеграл лебега

## If:

1. $-\infty < a < b \le +\infty$
2. $f \in L_1([a,b_1])\quad \forall b_1 < b$
3. $\exists \lim_{b_1 \to b+0}{\int_a^{b_1}{f(x) \d x}} \in \RR$

## Then:

Говорят, что несобственный интеграл лебега от $f$ по $[a,b)$ сходится

$$
\int_a^{\to b}{f(x) \d x} \defeq \lim_{b_1 \to b+0}{\int_a^{b_1}{f(x) \d x}}
$$

![14.jpg](assets/imgs/03-04-25_15-26-02_948_IMG_20250403_144404.jpg)

# Example

$$
\int_0^{+\infty}{\frac{\sin x}{x} \d x}
$$

![15.jpg](assets/imgs/03-04-25_15-26-02_817_IMG_20250403_144408.jpg)

# Def. Несобственный интеграл Лебега от параметра.

## If:

1. $f : [a,b) \times Y \to \ol{\RR}$
2. $\forall y \hthen \exists \int_a^{\to b}{f(t,y)\d t}$

## Then:

$$
J(y) \defeq \int_a^{\to b}{f(t,y)\d t}
$$

называется несобственным интегралом Лебега от параметра.

![16.jpg](assets/imgs/03-04-25_15-26-02_983_IMG_20250403_144527.jpg)

# Def. Расномерная сходимость по параметру.

Будем говорить, что $\int_a^{\to b}{f(t,y)\d t}$ **_сходится равномерно_**\
по $y \in Y$, если

$$
\sup_{y\in Y}{\int_{b_1}^{\to b}{f(t,y) \d t}} \to 0,\quad b_1 \to b-0
$$

![19.jpg](assets/imgs/03-04-25_15-26-02_572_IMG_20250403_145241.jpg)

# Theorem 3. О пределе по параметру.

## If:

1. $Y$ - [[1728837879-метрическое-пространство|метрическое пространство]]
2. $y_0$ - предельная т. в Y
3. $f: [a,b) \times Y \to \ol{\RR}$
4. $\forall t \in [a,b) \setminus 0 \hthen
\exists \lim_{y \to y_0}{f(t,y)} \rdefeq f_0(t)
$
   $\forall b_1 \in (a,b) \hthen$
5. $f_0 \in L_1[a,b_1]$
6. $\exists \lim_{y \to y_0}{\int_a^{b_1}{f(t,y)\d t}} = \int_a^{b_1}{f_0(t) \d t}$
7. $\int_a^{\to b}{f(t,y)\d t}$ сходится равномерно по $y$

## Then:

$$
\exists \lim_{y \to y_0}{\int_a^{\to b}{f(t,y)\d t}} = \int_a^{\to b}{f_0(t)\d t}
$$

## Photos:

![17.jpg](assets/imgs/03-04-25_15-26-02_573_IMG_20250403_144754.jpg)
![18.jpg](assets/imgs/03-04-25_15-26-02_867_IMG_20250403_145236.jpg)

## Proof:

![20.jpg](assets/imgs/03-04-25_15-26-02_925_IMG_20250403_145725.jpg)
![21.jpg](assets/imgs/03-04-25_15-26-02_066_IMG_20250403_145728.jpg)
![22.jpg](assets/imgs/03-04-25_15-26-02_470_IMG_20250403_145935.jpg)
![23.jpg](assets/imgs/03-04-25_15-26-02_161_IMG_20250403_150133.jpg)
![24.jpg](assets/imgs/03-04-25_15-26-02_756_IMG_20250403_150749.jpg)
![26.jpg](assets/imgs/03-04-25_15-26-02_749_IMG_20250403_150943.jpg)

# Theorem 4. Об интегрировании по параметру.

## If:

1. $Y = \group{Y, \mcN, \nu}$ - [[1729420252-измеримое-пространство|измеримое пространство]]
2. $\nu(Y) < +\infty$
3. $f: \left[a,b\right) \times Y \to \ol{\RR}$
4. $\int_a^{\to b}{f(t,y)\d t}$ сходится равномерно по $y$
5. $\forall b_1 \in (a,b) \hthen f \in L_1([a,b_1] \times Y)\ по\ (\mcL^1 \otimes \nu)$

## Then:

$$
J \in L_1(Y)
$$

$$
\int_Y\int_a^{\to b}{f(t,y) \d t \d \nu(y)} = \int_a^{\to b}{\groupr{\int_Y{f(t,y) \d \nu(y)}} \d t}
$$
