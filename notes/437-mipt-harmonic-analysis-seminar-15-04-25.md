---
id: 437-mipt-harmonic-analysis-seminar-15-04-25
aliases:
  - MIPT harmonic analysis seminar 15-04-25
tags: []
---

# MIPT harmonic analysis seminar 15-04-25

# Немного несобственных интегралов

# 1.

$$
I(\alpha) = \int_0^{+\infty}{e^{-x^2} \cos\group{2\alpha x} \d x} \\
$$

$\Align{
I^1(\alpha) = -\int_0^{+\infty}{2x e^{-x^2} \sin\group{2\alpha x} \d x} \\
\textit{По пр. Вейерштрасса.} \\
I^1(\alpha) = \textit{по частям} = 
2 \alpha \int_0^{+\infty}{e^{-x^2} \cos\group{2\alpha x}} \\
{I}^{'} = 2 \alpha I \\
I = c e^{-\alpha^2} \\
I(0) = \frac{\sqrt{\pi}}{2} \\
}$

$$
I(\alpha) = \frac{\sqrt{\pi}}{2} e^{-\alpha^2} \\
$$

# Интеграл Френеля

$$
I = \int_0^{+\infty}{\sin x^2 \d x}
$$

$\Align{
t = x^2 \\
I = \frac{1}{2} \int_0^{+\infty}{\frac{\sin t}{\sqrt{t}} \d t} \\
\textit{Заметим:} \\
\frac{1}{\sqrt t} = \frac{2}{\sqrt{t}} \int_0^{+\infty}{e^{-t x^2} \d x} \\
I = \frac{1}{\sqrt\pi} \int_0^{\infty}{\d t \sin t \int_0^{\infty}{e^{-t x^2} \d x}} \\
\textit{Можно ли переставить интегралы?}\\
\textit{Ответ: почему бы и нет. (я не понял почему...) По теореме.} \\
I = \frac{1}{\sqrt\pi} \int_0^{\infty}{\d x \int_0^{\infty}{\d t e^{-t x^2} \sin t}} \\
J \defeq \int_0^{\infty}{e^{-t x^2} \sin t \d t} = \textit{по частям} = \\
= -\int_0^{\infty}{x^2 e^{-t x^2} \cos t \d t} = \textit{по частям} = \\
= 1 + \int_0^{\infty}{x^4 e^{-t x^2} \sin t \d t} \\
J = 1 + x^4 J \\
J = \frac{1}{1 + x^4} \\
I = \frac{1}{\sqrt\pi} \int_0^{\infty}{\d x \frac{1}{1 + x^4}}\\
G \defeq \int_0^{\infty}{\frac{\d x}{1 + x^4}}
H \defeq \int_0^{\infty}{\frac{x^2}{1 + x^4} \d x} = 
-\int_{\infty}^{0}{\frac{\d \group{\frac{1}{x}}}{1 + \group{\frac{1}{x}}^4}} =
\int_0^{\infty}{\frac{\d u}{1 + u^4}} \\
2 G = G + H = \int_0^{\infty}{\frac{1 + x^2}{1 + x^4} \d x} =
\int_0^{\infty}{\frac{x^{-2} + 1}{x^{-2} + x^2} \d x} = \\
\int_{-\infty}^{+\infty}{\frac{\d \group{x - \frac{1}{x}}}{x^{-2} + x^2} \d x} = \\
\int_{-\infty}^{+\infty}{\frac{\d u}{2 + u^2}} =\\
\frac{\pi}{\sqrt{2}} \\
G = \frac{\pi}{2\sqrt{2}} \\
}$

$$
I = \frac{\sqrt\pi}{2\sqrt{2}}
$$

# Формулы Фруллани

# 1.

## Let:

1. $f \in C[0,+\infty]$
2. $\int_A^{\infty}{\frac{f(x)}{x} \d x}$ сх-ся $\forall A > 0$

## Then:

$$
\int_0^{+\infty}{\frac{f(\alpha x) - f(\beta x)}{x} \d x} = f(0) \ln \frac{\beta}{\alpha}
$$

$\forall \alpha,\beta > 0$

## Proof:

$\Align{
I = \lim_{A \to 0}\group{\int_A^{+\infty}{\frac{f(\alpha x)}{x} \d x} - 
\int_A^{+\infty}{\frac{f(\beta x)}{x} \d x}} = \\
\lim_{A \to 0}\group{\int_{\alpha A}^{+\infty}{\frac{f(t)}{t} \d x} - 
\int_{\alpha A}^{+\infty}{\frac{f(t)}{t} \d t}} = \\
\lim_{A \to 0}\group{\int_{\alpha A}^{\beta A}{\frac{f(t)}{t} \d t}} = \\
\lim_{A \to 0}\group{f(\xi) \int_{\alpha A}^{\beta A}{\frac{\d t}{t}}} = \\
\xi \in [\alpha A, \beta A] \\
= f(0) \ln \frac{\beta}{\alpha} \\
}$

# 2.

## Let:

1. $f \in C[0,+\infty]$
2. $\exists f(+\infty)$

## Then:

$$
\int_0^{+\infty}{\frac{f(\alpha x) - f(\beta x)}{x} \d x} =
(f(0) - f(\infty)) \ln \frac{\beta}{\alpha}
$$

$\forall \alpha,\beta > 0$

## Proof:

$\Align{
Null
}$

# 3.

## Let:

1. $f \in C[0,+\infty]$
2. $\exists f(+\infty)$
3. $\int_0^{A}{\frac{f(x)}{x} \d x}$ сх-ся $\forall A > 0$

## Then:

$$
\int_0^{+\infty}{\frac{f(\alpha x) - f(\beta x)}{x} \d x} =
f(\infty) \ln \frac{\beta}{\alpha}
$$

$\forall \alpha,\beta > 0$

## Proof:

$\Align{
Null
}$

# Преобразование Фурье

# Итнеграл Фурье

# Напоминание

$f \in L_1[-R, R]$

$$
c_k = \frac{1}{2R} \int_{-R}^{R}{f(x) e^{ik \frac{\pi}{R} x} \d x}
$$

$$
f(x) \sim \sum_{k\in\ZZ}{c_k e^{ikx}}
$$

# $R \to \infty$

$f$ - "хорошая"

$\Align{
f(x) = \sum_{k\in\ZZ}{c_k e^{ikx}} = \\
\frac{\pi}{R} \sum_{k\in\ZZ}{\group{c_k \frac{R}{\pi}} e^{ikx}} \\
c_k \frac{R}{\pi} = \frac{1}{2\pi} \int_{-R}^{R}{f(x) e^{-ik \frac{\pi}{R} x} \d x} \\
y_k \defeq k \frac{\pi}{R} \\
c(y_k) \defeq c_k \frac{R}{\pi} \\
f(x) = \frac{\pi}{R} \sum_{k\in\ZZ}{c(y_k) e^{i y_k x}} \\
f(x) \xrightarrow{R \to \infty} \int_{-\infty}^{+\infty}{c(y) e^{iyx} \d x} \\
}$

$$
f(x) \sim \int_{-\infty}^{+\infty}{c(y) e^{iyx} \d x} \\
$$

$$
c(y) = \frac{1}{2\pi} \int_{-\infty}^{+\infty}{f(x) e^{-iyx} \d x}
$$

# Преобразование Фурье

$$
F[f](y) = \frac{1}{2\pi} \int_{-\infty}^{+\infty}{f(x) e^{-iyx} \d x}
$$

$$
F: L_1(\RR) \to C_0(\RR)
$$

$C_0(\RR) \defeq \set{y \in C(\RR) \mid y(+\infty) = 0}$

# Свойства

# Claim

$$
F[f]\ \textit{инъективно, но не сюрьективно}
$$

# Замечания

$C_0(\RR)$ - банахова алгебра
(поточечное перемножение)
($\norm{g} \defeq \sup\abs{g}$)
$L_1(\RR)$ - тоже банахова алгебра
($f \cdot g \defeq f \star g$) - [[709-свертка-функций|свертка функций]]

# Claim

$2\pi F$ - гомоморфизм алгебр

$\Align{
\textit{Хотим показать:}\\
2\pi F[f \star g] = 2\pi F[f] \cdot 2\pi F[g] \\
\int_{-\infty}^{+\infty}{(f \star g)(x) e^{-iyx} \d x} = \\
\int_{-\infty}^{+\infty}{\d x \int_{-\infty}^{+\infty}{\d t f(t) g(x - t) e^{-iyx}}} = \\
\textit{т. Фуббини} \\
= \int_{-\infty}^{+\infty}{\d t f(t)} \cdot \int_{-\infty}^{+\infty}{\d x g(x - t) e^{-iyx}} = \\
= \int_{-\infty}^{+\infty}{\d t f(t) e^{-iyt}} \cdot \int_{-\infty}^{+\infty}{\d x g(x - t) e^{-it (x - t)}} = \\
= 2\pi J[f] \cdot 2\pi J[g] \\
}$

# Пример. $f \in L_1: F[f] \not\in L_1$

$\Align{
f = \chi_{[-1,1]} \\
F[f](y) = \frac{\sin y}{\pi y} 
}$
