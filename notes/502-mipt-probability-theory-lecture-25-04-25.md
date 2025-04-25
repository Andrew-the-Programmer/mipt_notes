---
id: 502-mipt-probability-theory-lecture-25-04-25
aliases:
  - MIPT probability theory lecture 25-04-25
tags: []
---

# MIPT probability theory lecture 25-04-25

# Хар. ф-ия нормального вектора

$$
\varphi_\vec{\xi}(\vec{t}) = e^{i t^T m_\xi - \frac{1}{2} t^T R_\xi t}
$$

# Definition. Обобщенный нормальный вектор

Случайный вектор, который соответствует хар. ф-ии нормального вектора.

# Claim

Мн-во обобщенных нормальных векторов замкнуто отн. линейных преобразований.

# .

1. $\omega \to \xi$
2. $\omega \to \vec{\xi}$
3. $\omega \to \set{\xi_n}_{n\in\NN}$

$\Align{
\sup \xi_n \\
\inf \xi_n \\
\limsup \xi_n \\
\liminf \xi_n
}$

# Сходимости

# .

$$
\Gather{
\xi_n \xrightarrow{d} \xi \\
\same \\
F_{\xi_n} \xrightarrow{гладко} F_\xi
}
$$

# P-сходимость почти наверное

$$
\Gather{
\xi_n \xrightarrow{P} \xi \\
\same \\
\forall \varepsilon > 0\quad
P(\abs{\xi_n - \xi} > \varepsilon) \xrightarrow{n\to\infty} 0
}
$$

# .

$$
\Gather{
r \ge 1 \\
\xi_n \xrightarrow{(r)} \xi \\
\same \\
E\abs{\xi_n - \xi}^r \xrightarrow{n\to\infty} 0
}
$$

# Сходимость почти наверное

$$
\Gather{
\xi_n \xrightarrow{п.н.} \xi \\
\same \\
P\set{\omega : \xi_n(\omega) \xrightarrow{n\to\infty} \xi(\omega)} = 1
}
$$

# Критерий сходимости

$$
\Gather{
\xi_n \xrightarrow{P} \xi \\
\implies \\
\exists \set{n_k}: \xi_{n_k} \xrightarrow{п.н.} \xi
}
$$
