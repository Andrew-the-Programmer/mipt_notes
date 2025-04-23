---
id: 604-mipt-differential-equations-seminar-23-04-25
aliases:
  - MIPT differential equations seminar 23-04-25
tags: []
---

# MIPT differential equations seminar 23-04-25

# Ф 1064

![23-04-25_15-47-25_439.png](assets/imgs/23-04-25_15-47-25_439.png)

$\Align{
\circled{1} \\
\textit{Вырожденное ДУ}: \mu \equiv 0 \\
\boxed{y = e^x} \\
\circled{2} \\
\pdv{\mu}{y} \defeq u(x,\mu) \\
\textit{Ур-ие в вариациях}: \\
\Cases{
u_x = u + x + ysr + 2 \mu y u \\
u \rvert_{x=0} = 0
} \\
\mu \equiv 0 \implies\\
u_x = u + x + y^2 = u + x + e^{2x} \\
\implies \\
u = - x - 1 + e^{2x} \\
\textit{Ассимптотические ряды} \\
y(x,\mu) = y(x,0) + \mu \pdv{\mu}{y}(x,0) + \frac{\mu^2}{2} \pdv[2]{\mu}{y}(x,0) + o(\mu^2) \\
y(x,\mu) = \sum_{i\in\NN_0}{\mu^i y_i(x)}
}$
