---
id: 970-mipt-field-theory-lecture-14-05-25
aliases:
  - MIPT field theory lecture 14-05-25
tags: []
---

# MIPT field theory lecture 14-05-25

Последняя лекция

# Спрошлой лекции

Запаздывающий потенциал

$$
\Gather{
\vec{A}(x,t) = \frac{e}{c} \frac{\vec{v}(t_{ret})}{\abs{x - x_e(t_{ret})}} \\
t_{ret} = t - \frac{\abs{x - x_e(t)}}{c} \\
x_e(t) = \Matrix{
0 \\ 0 \\ z_0 \cos \omega t
} = z_0 \Re \Matrix{
0 \\ 0 \\ e^{i \omega t}
}
}
$$

Диаграмма Минковского

![14-05-25_10-23-31_632_IMG_20250514_091102.jpg](assets/imgs/14-05-25_10-23-31_632_IMG_20250514_091102.jpg)

Решаем систему методом последовательных приближений

1. Если $x_e \ll x$
   $\Align{
t_{ret} \approx t - \frac{\abs{x}}{c} + \frac{\vec{n} \cdot \vec{x_e}(t)}{c} \\
\vec{n} = \frac{\vec{x}}{\abs{x}} \\
\frac{\frac{\vec{n} \cdot \vec{x_e}(t)}{c}}{t - \frac{\abs{x}}{c}} \sim \frac{v_e}{c} \\
\textit{Релятивисткое приближение}: \frac{v_e}{c} \to 0
}$

<br>

0. Нулевое (ведущее) приближение $t_{ret} = t - \frac{\abs{x}}{c}$
1. Первое приближение $t_{ret} = t - \frac{\abs{x}}{c} + \frac{\vec{n} \cdot \vec{x_e}(t - \frac{\abs{x}}{c})}{c}$

$$
A(x,t) = \frac{e}{c} \frac{v_e(t - \abs{x} / c)}{\abs{x - x_e(t - \abs{x} / c)}}
$$

Мультипольное разложение

$$
A(x,t) = \frac{e}{c} \frac{v_e(t - \abs{x} / c)}{\abs{x}}
$$

Ответ:

$\Align{
d(t) \defeq e x_e
}$

$$
\Gather{
\varphi = \frac{1}{c} \frac{\veccross{\dot{d}}{n}}{\abs{x}} + \frac{\veccross{d}{n}}{\abs{x}^2} \\
B =
\frac{\dot{d} \times n}{c \abs{x}^2} +
\frac{\ddot{d} \times n}{c^2 \abs{x}} =
B_1 + B_2 \\
E =
\frac{3 \veccross{d}{n} \vec{n} - \vec{d}}{\abs{x}^3} +
\frac{3 \veccross{\dot{d}}{n} \vec{n} - \dot{\vec{d}}}{c \abs{x}^2} +
\frac{\veccross{\ddot{d}}{n} \vec{n} - \ddot{\vec{d}}}{c^2 \abs{x}} =
E_1 + E_2 + E_3
}
$$

Для $B$:

$
\frac{B_2}{B_1} \sim \frac{\abs{x}}{\lambda}
$

Для $E$:

3 случая (3 зоны):

1. Квазистатическая зона $\abs{z_0} \ll \abs{x} \ll \lambda$
2. Переходная зона $\abs{z_0} \ll \abs{x} \sim \lambda$
3. Зона излучения (волновая) $\abs{z_0} \ll \lambda \ll \abs{x}$

Описание результата
В зоне излучения:

$$
\Gather{
E \approx E_3 = \frac{\veccross{\ddot{d}}{n} \vec{n} - \ddot{\vec{d}}}{c^2 \abs{x}} \\
B \approx B_2 = \frac{\ddot{d} \times n}{c^2 \abs{x}}
}
$$

1. $n \perp E \perp B$
2. $\abs{E} = \abs{B}$

Совпадают с условиями распространение ЭМ волн

# Диаграмма направленности электро-дипольного излучения

$$
\vec{S} = \frac{c}{4\pi} \vec{E} \times \vec{B}
$$

![14-05-25_10-25-35_959_IMG_20250514_100154.jpg](assets/imgs/14-05-25_10-25-35_959_IMG_20250514_100154.jpg)

$\Align{
\abs{S} = \frac{\abs{\ddot{d}^2}}{4\pi c^3 \abs{x}^2} \sin^2 \theta \\
\textit{Поток энергии}:\\
\dv{t}{\varepsilon} = \abs{S} \d S = \abs{S} R^2 \d \Omega = \frac{\abs{\ddot{d}}^2}{4\pi c^3} \sin^2 \theta \d \Omega
}$

Диаграмма направленности: в какую сторону больше излучение?
Получается трехмерный бублик.

![бублик](assets/imgs/14-05-25_10-23-31_376_IMG_20250514_100547.jpg)

Поток энергии не зависит от $R$.
$\same$
$\abs{S} \sim \frac{1}{R^2}$
$\same$
$\abs{E} = \abs{B} \sim \frac{1}{R}$

# Полная мощность излучения ЭМ волн, Формула Лармора

$\Align{
I = \int_{4\pi}{\dv{t}{\varepsilon} \d \Omega}
}$

Формула Лармора

$$
I = \frac{2}{3 c^3} \abs{\ddot{d}}^2 = \frac{2 e^2}{3 c^3} \abs{\dot{{v}_{e}}}^2
$$

Следствие:
ЭМ волны излучаются только ускоренными зарядами

Дифференциальное сечение рассеяния

$$
\dv{\Omega}{\sigma} = \frac{1}{\avrg{\abs{j_{пад}}}} \dv{\Omega}{\group{\dv{t}{\varepsilon}}} =
\group{\frac{e^2}{m c^2}} \frac{\omega^4}{(\omega_0^2 - \omega^2)^2} \sin^2\theta
$$
