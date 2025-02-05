---
id: 1729104266-mipt-anmech-seminar-16-10-24
aliases:
  - MIPT anmech seminar 16-10-24
tags: []
---

# MIPT anmech seminar 16-10-24

$m \vec{{{W}_{abs}}} = \vec{R}$
$\vec{{W}_{abs}} = \vec{{W}_{rel}} + \vec{{W}_{tr}} + \vec{{W}_{cor}}$
$m \vec{{W}_{rel}} = \vec{R} - m \vec{{W}_{tr}} - m \vec{{W}_{abs}} = \vec{R} + \vec{{I}_{tr}} + \vec{{I}_{cor}}$
$\dv{t}{\vec{{Q}_{rel}}} = \vec{R} - \sum_{i}^{}{m_i \vec{{W}_{tr}}} - \sum_{}^{}{m_i \vec{{W}_{cor}}}$ 
$\dv{t}{\vec{K_O}} = \vec{{M}_{O}} - \vec{{v}_{O}} \times m \vec{{v}_{C}} - \sum_{i}^{}{\vec{{r}_{i}} \times m_i \vec{{W}_{tr}}} - \sum_{i}^{}{\vec{{r}_{i}} \times m_i \vec{{W}_{cor}}}$

## Exercises
### 1
![[1729089075-16-10-anmech-1.svg]]
$\omega \equiv const$
$\phi(t)$ 
$m \vec{{W}_{rel}} = m \vec{g} + \vec{{I}_{tr}} + \vec{{I}_{cor}} + \vec{N}$
$\vec{{I}_{in}} = \vec{{I}_{tr}} + \vec{{I}_{cor}}$ 
$$
\vec{OA} = \begin{pmatrix}
r \sin \phi \\
-r \cos \phi
\end{pmatrix};\quad
\dot{\vec{OA}} = \begin{pmatrix}
r \cos \phi\ \omega \\
r \sin \phi\ \omega
\end{pmatrix}
$$
$$
\vec{{K}_{O}} = \vec{OA} \times m \dot{\vec{OA}} = \begin{pmatrix}
0 \\
0 \\
r^2 \omega m
\end{pmatrix}
$$

$$
\dv{t}{\vec{{K}_{O}}} = \vec{{M}_{tr}} + \vec{{M}_{mg}} + \vec{{M}_{cor}} + \vec{{M}_{N}}
$$
$$
\vec{{W}_{tr}} = \omega \times \omega \times OA = \begin{pmatrix}
-w^2 r \sin{\phi} \\
0 \\
0
\end{pmatrix}
$$
$$
\vec{{M}_{tr}} = \vec{OA} \times \vec{{I}_{tr}} = \begin{pmatrix}
0 \\
0 \\
m \omega^2 r^2 \sin{\phi} \cos{\phi}
\end{pmatrix}
$$
$$
\vec{{I}_{cor}} = -m \vec{{W}_{cor}} = -m 2 \vec{\omega} \times \vec{{v}_{rel}} = \begin{pmatrix}
0 \\
0 \\
2 \omega r \cos{\phi} \omega m
\end{pmatrix}
$$

$$
\vec{{N}_{z}} + \vec{{I}_{cor}} = 0 \implies \vec{{M}_{N_z}} = - \vec{{M}_{cor}}
$$
$$
mr^2\phi^2 = m \omega^2 r^2 \sin{\phi} \cos{\phi} - mg r \sin{\phi}
$$
### 9.16
![[1729090347-16-10-anmech-9-16.svg]]
$F_{fr}(t), N(t) - ?$
$\phi(t) = \omega t$

$m \vec{{W}_{C}} = \vec{mg} + \vec{N} + \vec{{F}_{fr}} + \vec{{I}_{cor}} + \vec{{I}_{tr}}$ 
$\vec{OC} = \begin{pmatrix}l\\r\\0\end{pmatrix}$
$\vec{{I}_{tr}} = -m \cdot w \times w \times OC = m \omega^2 \begin{pmatrix}l\\r\\0\end{pmatrix}$
${I}_{cor} = -m (2 \omega \times {v}_{rel}) = -2m \begin{pmatrix}0\\\dot{\phi} \dot{l}\\0\end{pmatrix}$
$$
\begin{cases}
O\xi: & m \ddot{l} = mg \cos{\phi} - {F}_{fr} + m {\dot{\phi}}^{2} l\\
O\nu: & 0 = N - mg \sin{\phi} + m {\dot{\phi}}^{2} - 2 m \dot{\phi} \dot{l}
\end{cases}
$$
$\Omega = - \frac{\dot{l}}{r}$
$$
\vec{{{K}_{C}}^{rel}} = J_C \vec{\Omega} = \begin{pmatrix}
0\\0\\
\frac{m r^2}{2} \frac{-\dot{l}}{{r}}\end{pmatrix}
$$
$\dot{\vec{{{K}_{C}}^{rel}}} = \begin{pmatrix}0\\0\\-\frac{m r \ddot{l}}{2}\end{pmatrix}$
$$
\begin{gather}
\vec{{M}_{cor}} = -2 \sum_{i}^{}{m_i (\vec{{r}_{i}} \times \vec{{I}_{cor}}_i)}\\
\vec{{I}_{{cor}_i}} = 2 m_i \vec{{\omega}_{i}} \times (\vec{{{v}_{C}}^{rel}} + \vec{\Omega} \times \vec{{r}_{i}}) \\
\vec{{M}_{cor}} = 0
\end{gather}
$$
$$
\begin{gather}
{I}^{tr}_{i} = -m (w \times w \times (OC + r_i)) \\
{M}^{tr} = -\sum_{i}^{}{m_i r_i \times {I}^{tr}_{i}} = 0
\end{gather}
$$
