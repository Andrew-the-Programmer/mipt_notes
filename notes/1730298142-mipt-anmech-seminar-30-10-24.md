---
id: 1730298142-mipt-anmech-seminar-30-10-24
aliases:
  - MIPT anmech seminar 30-10-24
tags: []
---

# MIPT anmech seminar 30-10-24
[[1731145139-тензор-инерции|тензор инерции]]
$$
\alignleft{
\vec{{K}_{A}} = \sum_{i}^{}{\vec{{r}_{Ai}} \times m {v}_{i}} =
m \vec{{R}_{AC}} \times \vec{{V}_{A}} +
\vec{\omega} \left( \sum_{i}^{}{m_i J_i} \right)
}
$$
$$
J(r) = \Pmatrix{
y^2 + z^2 & -xy & -xz \\
-yx & x^2 + z^2 & -yz \\
-zx & -zy & x^2 + y^2
} = \Pmatrix{
A & -F & -E \\
-F & B & -D \\
-E & -D & C
}
$$
Условие физической реализации тела.
$$
A + B \ge C
$$

Найдем C для цилиндра в качестве примера.
$$
\alignleft{
C = \int_G{(x^2 + y^2) \d m} \\
\Cases{
x = r \cos \phi \\
y = r \sin \phi \\
z = z
}\\
D = \Pmatrix{
\cos \phi & \sin \phi & 0 \\
-r \sin \phi & r \cos \phi & 0 \\
0 & 0 & 1
} \\
J = \det D = r \\
\d m = \rho \d V = \rho \d x \d y \d z \\
C = \rho \int{\int{\int{(x^2 + y^2) \d x \d y \d z}}} \\
C = \rho \int_0^R \int_0^{2\pi} \int_{-\frac{\pi}{2}}^{\frac{\pi}{2}}{
(r^2 \cdot J) \d r \d \phi \d z = 
\rho \frac{R^4}{4} 2\pi H = \frac{m R^2}{2}
}
}
$$
$$
\alignleft{
A = B = \frac{1}{2} C + \int{z^2 \d m} \\
\int_0^R \int_0^{2\pi} \int_{-\frac{\pi}{2}}^{\frac{\pi}{2}}{
z^2 r \d r \d \phi \d z
} =
\frac{mH^2}{2} \\
}
$$
$$
A = B = \frac{mR^2}{2} + \frac{mH^2}{12}
$$
$$
F = E = D = 0
$$

[[1730299611-главные-оси|главные оси]]
[[1730299627-главные-центральные-оси|главные центральные оси]]

