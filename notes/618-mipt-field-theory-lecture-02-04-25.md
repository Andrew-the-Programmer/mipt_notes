---
id: 618-mipt-field-theory-lecture-02-04-25
aliases:
  - MIPT field theory lecture 02-04-25
tags: []
---

# MIPT field theory lecture 02-04-25

Опоздал на минут 10.

# Движение релятив. частицы под действием постоянной силы

Из конца предыдущей лекции:

$$
f^\mu \defeq \dv{s}{P^\mu} = \Pmatrix{
\frac{\gamma}{c} \veccrossv{F}{v} \\
\vec{F} + (\gamma - 1) \veccrossv{F}{v} \frac{\vec{v}}{v^2}
}
$$

![1.png](assets/imgs/02-04-25_09-35-56_995_02-04-25_09-35-50_596.png)
![2.png](assets/imgs/02-04-25_09-37-00_761_02-04-25_09-36-55_992.png)
![3.png](assets/imgs/02-04-25_09-38-28_299_02-04-25_09-38-23_350.png)
![4.jpg](assets/imgs/02-04-25_09-52-30_436_IMG_20250402_091643.jpg)

# Закон изменения энергии

$$
\Dv{t}{\gamma mc^2} = F v = N
$$

$N$ - мощность

# Закон изменения импульса

$$
\Dv{t}{\gamma m \vec{v}} = \vec{F}
$$

# Парадокс близнецов

![6.jpg](assets/imgs/02-04-25_09-52-30_329_IMG_20250402_092642.jpg)
![9.jpg](assets/imgs/02-04-25_09-52-30_086_IMG_20250402_093409.jpg)
![11.jpg](assets/imgs/02-04-25_09-52-30_907_IMG_20250402_094101.jpg)
![10.jpg](assets/imgs/02-04-25_09-52-30_442_IMG_20250402_094057.jpg)
![12.jpg](assets/imgs/02-04-25_09-52-30_621_IMG_20250402_094553.jpg)

# Мысленный парадокс Эйнштейна с лифтм

![7.jpg](assets/imgs/02-04-25_09-52-30_459_IMG_20250402_093014.jpg)

# Интегрирование уравнений движения

![8.jpg](assets/imgs/02-04-25_09-52-30_730_IMG_20250402_093020.jpg)

# Ковариантная форма [[1730271345-уравнения-Максвелла|уравнений Максвелла]] отн. преобр. Лоренца.

**_Гипотеза_**: <u>эл. заряд сохраняется и явл. инвариантом</u>.

Рассмотрим кубик.

Плотность заряда:
$\rho_1 = \frac{q}{a^3},\quad \rho = \gamma \frac{q}{a^3} = \gamma \rho_1$
Плотность токо:
$j_1 = 0,\quad j = \rho v$

4-вектор тока:

$$
j^\mu = \Pmatrix{
\rho c \\
\vec{j}
}
$$

$j_1^\mu = \Lambda_x(v) j^\mu$

$$
\pdv{t}{\rho} + \divv \vec{j} = 0
$$

$$
\partial_\mu j^\mu = 0
$$

# Скалярный векторный потенциал э-м поля.

$\divv \vec{B} = 0 \implies$

$$
 \vec{B} = \rot \vec{A}
$$

$\vec{A}$ - векторный поренциал
$\rot \vec{E} = -\frac{1}{c}\pdv{t}{B} \implies 
\rot\group{E + \frac{1}{c} \pdv{t}{\vec{A}}} = 0 \implies 
$

$$
\vec{E} = -\grad\varphi - \frac{1}{c}\pdv{t}{\vec{A}}
$$

Потенциал определен не однозначно.
