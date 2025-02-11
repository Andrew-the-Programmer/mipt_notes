---
id: 1730454310-ряд-Фурье-fourier-series
aliases:
  - Fourier series
  - ряд Фурье
  - интеграл Фурье
tags: []
---

# Ряд Фурье | Fourier series
# В [[1738654869-интегрируемая-по-лебегу-функция|L2]]
$L_2$ - Гильбертово пространство

$f$ - [[1729932429-периодическая-функция|периодическая функция]].

Тогда разложение $f$ в ***ряд Фурье***:
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
