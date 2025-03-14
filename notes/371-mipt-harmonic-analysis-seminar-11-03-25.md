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
a_{n,\nu} \defeq a_n(g_\nu) = \int_0^\pi{\cos{(nx)} g_\nu(x) \d x} =
\frac{\nu + \frac{1}{2}}{(\nu + \frac{1}{2})^2 - n^2} \\
a_{n,\nu} > 0, \quad n \le \nu \\
a_{n,\nu} < 0, \quad n > \nu \\
S_{k,\nu} \defeq \sum_{n=1}^{k}{a_{n,\nu}} \\
S_{\infty, \nu} = \frac{1}{2} a_{0,\nu} \\
S_{k,\nu} \le \frac{1}{2} a_{0,\nu},\quad k > \nu \\
S_{\nu,\nu} \ge \frac{1}{2} \ln\group{4\nu + 3} \ge \frac{1}{2} \ln\group{\nu} \\
a_n(f) = \frac{2}{\pi} \sum_{p\in\NN}{\frac{1}{p^2} a_{n,2^{(p^3)}}} \\
S_k(f) = \frac{2}{\pi} \sum_{p\in\NN}{\frac{1}{p^2} S_{k,2^{(p^3 - 1)}}} \\
S_{2^{(p^3 - 1)}} \ge C \frac{1}{p^2} S_{2^{(p^3 - 1)},2^{(p^3 - 1)}} \ge
C p \to \infty
}
$$

# 5

$$
f(x) \defeq \sum_{}^{}{\frac{\sin{nx}}{n^2}}
$$

Исследуем дифф. в 0.

$$
\AlignLeft{
f(0) = 0 \\
f(x) = \sum_{}^{}{S_n(x) \group{\frac{1}{n^2} - \frac{1}{(n+1)^2}}} \\
S_n(x) \defeq \sum_{k\in\NN}{\sin{kx}} \\
\abs{S_n(x)} \le \frac{\pi}{x} \\
\textit{В общем,} \\
\frac{f(x)}{x} \to \infty,\quad x \to 0
}
$$

# Банахова алгебра

$$
\Gather{
\group{V, \norm{\cdot}, \cdot} \\
\cdot : V \times V \to V \\
\norm{ab} \le \norm{a} \norm{b}
}
$$

# Свертка

$f,g \in L_1$

$$
(f \star g)(x) \defeq \int_{-\infty}^{+\infty}{f(t) g(x - t) \d t}
$$

1. Ассоциативна
2. Коммутативна
3. Липшецевость
4. $$
   f \in C^n \implies f \star g \in C^n
   $$

# Апроксимационная единица
