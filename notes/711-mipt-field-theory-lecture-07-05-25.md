---
id: 711-mipt-field-theory-lecture-07-05-25
aliases:
  - MIPT field theory lecture 07-05-25
tags: []
---

# MIPT field theory lecture 07-05-25

# Решение неоднородных уравнений Максвелла

# Задача об измерении ЭМ поля зарядами

$\Align{
\textit{Ур-ия Максвелла}
\to
\partial_\mu F^{\mu\nu} = \frac{4\pi}{c} j^\nu
\to \textit{калибровка Лоренца} \to
\Cases{
\DAlambert \varphi = 4\pi \rho \\
\DAlambert A = \frac{4\pi}{c} j
}\\
\textit{Схема решения}: \\
1 \textit{Из волнового уравнения находим } \vec{A} \\
2 \textit{Находим } \varphi \\
\frac{1}{c} \pdv{t}{\varphi} + \divv \vec{A} = 0 \\
3 \textit{Находим } \vec{E}, \vec{B} \\
E = -\grad \varphi - \frac{1}{c} \pdv{t}{\vec{A}} \\
B = \rot \vec{A}
}$

# Сферические волны

$$
\DAlambert f = 0 \implies f(t,x) = f_0 e^{i (\omega t - \vec{k} \vec{x})}
$$

# ЭМ статика

Ур-ие Пуассона

$$
-\grad \varphi = 4\pi \rho
$$

# Функция Грина $G$

$$
D G = \delta
$$

$D$ - дифференциальный оператор
(было на семинаре по матану на этой неделе)

$$
-\Laplace_x G = \delta
$$

# Решение

$$
\varphi(x) = 4\pi \int{\d^3 y\ G(x, y) \rho(y)}
$$

# Для точечного заряда

$$
-\Laplace_x \group{\frac{e}{\abs{x-y}}} = 4\pi e \delta(x - y)
$$

$$
G(x,y) = \frac{1}{4\pi} \frac{1}{\abs{x - y}}
$$

# Для магнитостатики

$$
\vec{A}(x) = \frac{4\pi}{c} \int{\d^3 y\ G(x,y) \vec{j}(y)}
$$

# Мультипольное разложение

# Заряженное облако

Ф-ия грина приближенно раскладывается на компоненты
Дипольный момент
Квадрупольный момент

$$
\varphi(x) = \frac{Q}{\abs{x}} + \grad_i \group{\frac{1}{\abs{x}}} \vec{d}_i +
\frac{1}{2} \grad_i \grad_j \group{\frac{1}{\abs{x}}} D_{ij} + \dots
$$

$Q = \int{\rho(x) \d^3 x}$ - полный заряд (тензор 0 ранга)
$\vec{d} = \int{x \rho(x) \d^3 x}$ - дипольный момент (тензор 1 ранга)
$D_{ij} = \int{\group{x_i x_j - \frac{1}{3} \delta_{ij} \abs{x_i}^2} \rho(x) \d^3 x}$
$-$ квадрупольный момент (тензор без следа)

# Частное решение неодн. волнового ур-ия

$\DAlambert \varphi = 4\pi \rho(x,t)$
$\rho(x,t) = e(t) \delta(x)$
$x \neq 0 \implies \DAlambert \varphi = 0 \implies \textit{сферические волны}$
$\varphi = \frac{u \group{t \pm \frac{r}{c}}}{r}$

Квазистатическое приближение
$e(t)$ - периодическая функция с периодом $T$

$\lambda \defeq c T$
$\frac{\abs{x}}{\lambda} \ll 1$ - квазистатическое приближение
$\implies$
$\pdv[2]{t}{\varphi} \ll 1$
$\implies$ ур-ие Пуассона:
$-\Laplace \varphi(x,t) = 4\pi \rho(x,t)$

В малой области можно найти решение с помощью ф-ии Грина и по единственности
решения продолжить на все пр-во.

$\varphi(x \in U,t) = \frac{e(t)}{\abs{x}}$
Угадаем решение

$\varphi(x \in \RR^3,t) = \frac{e\group{t \pm \frac{\abs{x}}{c}}}{\abs{x}}$

Запаздывающим потенциал

$$
\varphi = \frac{e\group{t - \frac{\abs{x}}{c}}}{\abs{x}}
$$

Частное решение с полностью запаздывающим потенциалом

$$
\varphi(x,t) = \int{\frac{\d^3 y}{\abs{x-y}} \rho\group{y, t - \frac{\abs{x-y}}{c}}}
$$

$$
A(x,t) = \int{\frac{\d^3 y}{\abs{x-y}} \vec{j}\group{y, t - \frac{\abs{x-y}}{c}}}
$$

Измерение точечного заряда в нерелятивистком приближении

$\Align{
\vec{j}(x,t) = \rho(t) \vec{v}(t) = e \delta(x - x_e(t)) \vec{{v}_{e}}(t) \\
\vec{{v}_{e}}(t) = \dv{t}{\vec{{x}_{e}}} \\
}$
$x_e(t)$ - траектория движения точечного заряда

$$
A(x,t) = \frac{e}{c} \frac{v_e(t_{ret})}{\abs{x - x_e(t_{ret})}}
$$

Диаграмма Минковского
