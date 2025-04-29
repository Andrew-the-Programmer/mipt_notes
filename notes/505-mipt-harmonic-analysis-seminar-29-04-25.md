---
id: 505-mipt-harmonic-analysis-seminar-29-04-25
aliases:
  - MIPT harmonic analysis seminar 29-04-25
tags: []
---

# MIPT harmonic analysis seminar 29-04-25

$$
L_2^R - \textit{ф-ии с носителем R}\quad (f = 0\quad \forall x \not\in [-R, R])
$$

$$
{L}_{2}^{loc} \defeq \bigcup_{n\in\NN}{L_2^n}
$$

# Claim

$L_2^{loc}$ всюду плотно в $L_2(\RR)$
$S$ всюду плотно в $L_2(\RR)$

$$
F: L_1(\RR) \to C_0(\RR)
$$

$$
F_2: L_2(\RR) \xrightarrow{\sim} L_2(\RR)
$$

# Собственные вектора $F_2$

$\Align{
\dv[2]{x}{f} - x^2 f = \mu f \\
f - \textit{решение} \same F[f] - \textit{решение} \implies f - \textit{собственный вектор} \\
\textit{Ищем в виде: } f_n = P_n(x) \cdot e^{-\frac{x^2}{2}} \\
{f}_{n}^{''} = e^{-\frac{x^2}{2}} \group{{P}_{n}^{''} - P_n + x^2 P_n - 2x {P}_{n}^{'}} \\
{P}_{n}^{''} - 2x {P}_{n}^{'} = (\mu - 1) P_n \\
x^k: (k+2)(k+1) a_{k+2} - 2k a_k = (\mu - 1) a_k \\
x^n: -2n a_n = (\mu - 1) a_n \\
\implies \mu = -2n + 1 \\
a_{n-1} = 0 \\
a_{n-1-2k} = 0,\quad \forall k < \frac{n}{2} \\
P_n - \textit{полиномы Эрмита} \\
f_n - \textit{функции Эрмита}
}$

# Lemma

Ф-ии Эрмита ортогональны

# Claim. Орт. Г.Ш.

# Полнота и замкнутость

$x^k f \in L_2(\RR) \forall k$
