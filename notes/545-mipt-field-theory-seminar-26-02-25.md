---
id: 545-mipt-field-theory-seminar-26-02-25
aliases:
  - MIPT field theory seminar 26-02-25
tags: []
---

# MIPT field theory seminar 26-02-25
$$
\AlignLeft{
T_i = \frac{1}{2} e_{ijk} \tilde{T_{jk}} \\
T_i e_{ilm} = \frac{1}{2} e_{ijk} e_{ilm} \tilde{T_{jk}} =
\frac{1}{2} \tilde{T_{jk}} (\delta_{jl} \delta_{km} - \delta_{jm} \delta_{kl}) =
\frac{1}{2} (\tilde{T_{lm}} - \tilde{T_{ml}}) =  \\
\tilde{T_{lm}} = \Pmatrix{
0 & T_3 & -T_2 \\
-T_3 & 0 & T_1 \\
T_2 & -T_1 & 0 \\
}
\\
}
$$

# Усреднение единичной нормали
![[1740562744.png]]
$$
\AlignLeft{
\d V = r^2 \d r \sin\theta \d \theta \d \varphi = r^2 \d r \d \Omega \\
\d \omega = \frac{\d \Omega}{4\pi} = 
\frac{\sin\theta \d \theta \d \varphi}{4\pi} \\
\avrg{f} = \int{f(\theta, \varphi) \d \omega} \\
\avrg{n_i} = 0 \\
\avrg{n_i n_j} = \frac{1}{3} \delta_{ij} \\
\avrg{n_i n_j n_k} = 0 \\
\avrg{n_i n_j n_k n_l} = \frac{1}{15} 
(\delta_{ij} \delta_{kl} + \delta_{ik} \delta_{jl} + \delta_{il} \delta_{jk}) \\
(15 = 3^2 + 2 \cdot 3)
}
$$

# 2D
$$
\AlignLeft{
\avrg{n_i} = 0 \\
\avrg{n_i n_j} = \frac{1}{2} \delta_{ij} \\
\avrg{n_i n_j n_k} = 0 \\
\avrg{n_i n_j n_k n_l} = \frac{1}{8} 
(\delta_{ij} \delta_{kl} + \delta_{ik} \delta_{jl} + \delta_{il} \delta_{jk}) \\
(8 = 2^2 + 2 \cdot 2)
}
$$

# div, rot
$$
\AlignLeft{
\divv{a} = d_i a_i \\
d_i = \pdv{x_i}{} \\
}
$$
