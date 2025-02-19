---
id: 1730454310-ряд-Фурье-fourier-series
aliases:
  - Fourier series
  - ряд Фурье
  - интеграл Фурье
tags: []
---
# Ряд Фурье | Fourier series

# [[582-l2-как-гильбертово-пространство|$L_2$ как гильбертово пространство]]
# В $L_1$

$f \in L_1[-\pi, \pi]$

Сопоставим $f$ ряд, который будем называть рядом Фурье:
$$
\Gather{
f \sim a_0 + \sum_{n\in\NN}{a_n \cos{nx} + b_n \sin{nx}} \\
a_0 = \frac{1}{2\pi} \int_{-\pi}^{\pi}{f \d x} \\
a_n = \frac{1}{\pi} \int_{-\pi}^{\pi}{f \cos{nx} \d x} \\
b_n = \frac{1}{\pi} \int_{-\pi}^{\pi}{f \sin{nx} \d x} \\
}
$$
При этом:
$$
\norm{f}^2 = 2\pi a_0^2 + \pi \sum_{n\in\NN}{a_n^2 + b_n^2}
$$

Комплексный ряд:
$$
\Gather{
f \sim \sum_{n\in\ZZ}{c_n e^{inx}} \\
c_n = \frac{1}{\pi} \int_{-\pi}^{\pi}{f(x) e^{inx} \d x} \\
a_0 = c_0 \\
2 a_n = c_n + c_{-n} \\
2 b_n = c_{n} - c_{-n} \\
}
$$

# Note
Мы не знаем сходиться ли ряд.

# [[567-теорема-Римана-Лебега|Теорема Римана-Лебега]]





# Из курса физики...

$f$ - [[1729932429-периодическая-функция|периодическая функция]].

Тогда разложение $f$ в **_ряд Фурье_**:

$$
f(t) = \frac{Q_0}{2} + \sum_{n\in\NN}{a_n \cos{\omega_n t} + b_n \sin{\omega_n t}}
$$

$$
\alignleft{
\omega_n = n \omega_0 \\
\omega_0 = \frac{2\pi}{T} \\
a_n \cos{\omega_n t} + b_n \sin{\omega_n t} = A_n \cos{\left(\omega_n t + \varphi_n\right)} \\
A_n = \sqrt{a_n^2 + b_n^2}
}
$$

$$
f(t) = \frac{Q_0}{2} + \sum_{n\in\NN}{A_n \cos{\left(\omega_n t + \varphi_n\right)}}
$$

$$
f(t) = \sum_{n \in \ZZ}{C_n \exp{i \omega_n t}}
$$

$$
\alignleft{
C_n = \begin{cases}
\frac{1}{2} A_n \exp{i \varphi_n} & n \ge 0  \\
\frac{1}{2} A_n \exp{- i \varphi_n} & n < 0  \\
\end{cases}
}
$$

$$
\Gather{
a_n = \frac{2}{T} \int_{-\frac{T}{2}}^{\frac{T}{2}}{f(t) \cos{\omega_n t} \d t} \\
b_n = \frac{2}{T} \int_{-\frac{T}{2}}^{\frac{T}{2}}{f(t) \sin{\omega_n t} \d t} \\
c_n = \frac{1}{T} \int_{-\frac{T}{2}}^{\frac{T}{2}}{f(t) \exp{-i \omega_n t} \d t} \\
}
$$

# Интеграл Фурье

$$
\alignleft{
2\pi \cdot g(\omega_n) \ldefeq \int_{-\frac{T}{2}}^{\frac{T}{2}}{f(t) \exp{-i \omega_n t} \d t} \\
c_n = g(\omega_n) \frac{2\pi}{T} = g(\omega_n) \Delta \omega \\
T \to \infty \implies \\
f(t) = \int_{-\infty}^{+\infty}{g(\omega) \exp{i \omega t} \d t}
}
$$

$$
f(t) = \int_{-\infty}^{+\infty}{g(\omega) \exp{i \omega t} \d t}
$$

$$
g(\omega_n) \eq \frac{1}{2\pi} \int_{-\infty}^{+\infty}{f(t) \exp{-i \omega_n t} \d t} \\
$$
