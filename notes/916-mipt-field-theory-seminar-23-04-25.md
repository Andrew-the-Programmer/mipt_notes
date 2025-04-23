---
id: 916-mipt-field-theory-seminar-23-04-25
aliases:
  - MIPT field theory seminar 23-04-25
tags: []
---

# MIPT field theory seminar 23-04-25

Магнитный момент частицы.
В слабо меняющемся поле

$$
\vec{\mu} \defeq \frac{e}{2c} \avrg{\vecprodv{x}{v}}
$$

Замкнутая траектория (контур) $\implies$

$$
\vec{\mu} = \frac{I}{c} \vec{S}
$$

$\Align{
F = \frac{e}{c} v \times B(x*0 + \xi(t)) \\
R_L - \textit{Ларморовский радиус} \\
\grad B \cdot R_L \ll B \\
\avrg{F_i} = \frac{e}{c} e_{ijk} \avrg{v_j B_k({x_0}\_l + \xi_l(t))} =
\frac{e}{c} e_{ijk} (\partial*l B_k) \avrg{\xi_l v_j} +
\frac{e}{c} e_{ijk} B_k(x_0) \avrg{v_j} \\
\avrg{v_j} = 0 \\
\hline
\textit{Claim:} \avrg{\xi_l v_j} = - \avrg{\xi_j v_l} \\
v_j = \dv{t}{\xi_j} \\
T \cdot \avrg{\xi_l v_j} = \oint{\xi_l \d \xi_j} = \xi_l \xi_j - \oint{\xi_j \d \xi_l} \\
\xi_l \xi_j = 0 \\
\hline
\avrg{F_i} = \frac{e}{c} e_{ijk} (\partial_l B_k) \avrg{\xi_l v_j}
}$

$$
\vec{F} = (\vec{\mu} \cdot \grad) \vec{B}
$$
