---
id: 925-mipt-harmonic-analysis-seminar-25-02-25
aliases:
  - MIPT harmonic analysis seminar 25-02-25
tags: []
---

# MIPT harmonic analysis seminar 25-02-25

# [[1730454310-ряд-Фурье-fourier-series|ряд Фурье]]

Пример.
Коэффиценты из симметрии функции.

# Пример

## 1 $f(x) = \frac{\pi - x}{2},\quad [0, 2\pi]$

$$
\AlignLeft{
a_0 = 0 \\
a_n = 0 \\
b_n = \frac{1}{\pi} \int_0^{2\pi}{\frac{\pi - x}{2} \sin{nx} \d x} =
-\frac{1}{2\pi} \int_0^{2\pi}{x \sin{nx} \d x} =
\frac{1}{n} \\
f(x) = \frac{\pi - x}{n} \sim \frac{ \sin{nx} }{n} \\
\norm{f}_2^2 = \int_0^{2\pi}{f \d x} = \frac{\pi^3}{6} \\
\norm{f}_2^2 = \pi \sum_{n=1}^{\infty}{\frac{1}{n^2}} \\
\frac{\pi^2}{6} = \sum_{n=1}^{\infty}{\frac{1}{n^2}} (= \zeta(2))
}
$$

## 2

$$
f(x) = \Cases{
    1, & 0 \le x \le \pi \\
    0, & \pi \le x \le 2\pi
}
$$

$$
\AlignLeft{
a_0 = \frac{1}{2} \\
a_n = 0 \\
b_n = -\frac{1}{\pi} \left(\frac{(-1)^n}{n} - \frac{1}{n}\right)\\
b_{2n-1} = \frac{2}{\pi (2n - 1)}
}
$$

## 3
$$
f(x) = \cos(\alpha x), \quad [-\pi, \pi]
$$
$$
\AlignLeft{
a_0 = \frac{\sin(\pi \alpha)}{\pi \alpha} \\
b_n = 0\\
a_n = (-1)^n \frac{2\alpha \sin(\pi \alpha)}{\pi(\alpha^2 - n^2)} \\
\cos{\alpha x} = \frac{\sin(\pi \alpha)}{\pi} \left(\frac{1}{\alpha} + 
\sum_{}^{}{}
\right) \\
}
$$

# Claim.

$$
\Gather{
1)\ f - \textit{нечетная} \same a_n = 0 \\
2)\ f - \textit{четная} \same b_n = 0 \\
}
$$

# Поточечная сходимость
# Признак Дини
$$
\AlignLeft{
1)\quad f \in L_1[-\pi, \pi] \\
2)\quad \exists f(x-0) = \lim_{x \to x_0-0}{f(x)} \\
3)\quad \exists f(x+0) = \lim_{x \to x_0+0}{f(x)} \\
4)\quad \exists \delta > 0: \textit{интеграл сходится}:\\
}
$$
$$
I = \int_0^{\delta}{\frac{1}{t} (f(x_0 + t) - f(x_0 + 0) + f(x_0 - t) - f(x_0 - 0)) \d t}
$$
Тогда:
Ряд Фурье в точке $x_0$ сходится к $\frac{f(x+0) + f(x-0)}{2}$.

# Признак Жордана
$$
\AlignLeft{
\exists \varepsilon > 0 : f(x) \in BV \forall x \in U_\varepsilon(x_0)
}
$$

# Условие Липшица
$$
\AlignLeft{
f - \textit{гельдерова} \\
\same \\
\exists \alpha [0,1], L > 0 : \abs{f(x) - f(y)} < L \abs{x - y}^\alpha
}
$$

# Равномерная сходимость
