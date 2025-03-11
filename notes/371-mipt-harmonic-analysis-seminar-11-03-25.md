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
c_n = O(\frac{1}{n^\alpha})
}
$$

# 3
$$
\AlignLeft{
\exists \alpha \in (0,1) : c_n = O(\frac{1}{n^{1+\alpha}}) \\
\implies \\
\textit{f гельдерова} \\
}
$$
