---
id: 371-mipt-harmonic-analysis-seminar-11-03-25
aliases:
  - MIPT harmonic analysis seminar 11-03-25
tags: []
---

# MIPT harmonic analysis seminar 11-03-25

# 1

$$
\AlignLeft{
c_n = \frac{1}{2\pi} \int_{-\pi}^{\pi}{f(x) e^{-inx} \d x} \\
\implies \\
c_n = \frac{1}{4\pi} \int_{-\pi}^{\pi}{\left[f(x) - f(x + \frac{\pi}{n})\right] e^{-inx} \d x} \\
}
$$

# 2

$$
\AlignLeft{
\alpha \in (0,1) \\
\abs{f(x) - f(y)} \le L \abs{x - y}^\alpha \\
(\textit{f гельдерова}) \\
\implies \\
c_n = o(\frac{1}{n^\alpha})
}
$$

# 3

$$
\AlignLeft{
\exists \alpha \in (0,1) : c_n = o(\frac{1}{n^{1+\alpha}}) \\
\implies \\
\textit{f гельдерова} \\
\\
\abs{\frac{e^{-inx} - e^{-iny}}{x - y}} \le \min\set{\frac{2}{x-y}, 2n} \\
\abs{f(x) - f(y)} = \abs{\sum{c_n \group{e^{-inx} - e^{-iny}}}} \le
\sum{\abs{c_n} \abs{e^{-inx} - e^{-iny}}} = \\
= \sum_{n < \frac{1}{\abs{x-y}}}{2n \abs{c_n} \abs{x-y}} +
\sum_{n > \frac{1}{\abs{x-y}}}{2 \abs{c_n}} \le \\
A_1 \sum_{n < \frac{1}{\abs{x-y}}}{\abs{x-y} n^{-\alpha}} +
A_2 \sum_{n > \frac{1}{\abs{x-y}}}{n^{-(1 + \alpha)}} \le
A \abs{x - y}^\alpha
}
$$

# 4

Пример непр. ф-ии, у которой ряд фурье расходится в точке.

$$
f(x) = \sum_{p=1}^{\infty} \frac{1}{p^2} \sin{((2^{(p^3)} + 1) \frac{x}{2})}
$$
$$
\AlignLeft{
f \in C,\quad f(0) = 0 \\
g_\nu(x) \defeq \sin\group{\frac{2\nu + 1}{2} x} \\
a_{n,\nu} \defeq \int_0^\pi{\cos{(nx)} g_\nu(x) \d x} =
\frac{\nu + \frac{1}{2}}{(\nu + \frac{1}{2})^2 - n^2} \\
a_{n,\nu} > 0, \quad n \le \nu \\
a_{n,\nu} < 0, \quad n > \nu \\
\sum_{n\in\NN}{a_{n,\nu}} = \frac{1}{2} a_{0,\nu}
}
$$
