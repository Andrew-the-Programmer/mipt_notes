---
id: 186-mipt-field-theory-seminar-02-04-25
aliases:
  - MIPT field theory seminar 02-04-25
tags: []
---

# MIPT field theory seminar 02-04-25

[[868-оператор-Д'Аламбера|оператор Д'Аламбера]]

$$
\partial_\mu \defeq \Pmatrix{
\frac{1}{c} \pdv{t}{} \\
\gradv
}
$$

$$
\Gather{
\vec{B} = \rot \vec{A} \\
\vec{E} = -\grad \varphi - \frac{1}{c} \pdv{t}{\vec{A}}
}
$$

**_4-потенциал_**.

$$
A^\mu \defeq \Pmatrix{
\varphi \\
\vec{A}
}
$$

$j^\mu$ - 4-вектор тока
$F^{\mu\nu}$ - 4-вектор ЭМ поля

Из ур-ий Максвелла можно получить:

$$
\partial_\nu F^{\nu\mu} = \frac{4\pi}{c} j^\mu
$$

$$
F^{\nu\mu} \defeq \partial^\nu A^\mu - \partial^\mu A^\nu = \Pmatrix{
0 & -E_1 & -E_2 & -E_3 \\
E_1 & 0 & -B_3 & B_2 \\
E_2 & B_3 & 0 & -B_1 \\
E_3 & -B_2 & B_1 & 0
}
$$
