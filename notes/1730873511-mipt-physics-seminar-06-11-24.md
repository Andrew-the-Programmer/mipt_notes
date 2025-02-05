---
id: 1730873511-mipt-physics-seminar-06-11-24
aliases:
  - MIPT physics seminar 06-11-24
tags: []
---

# MIPT physics seminar 06-11-24
[[1730535552-mipt-physics-lecture-02-11-24|MIPT physics lecture 02-11-24]]

# Theory
[[1729328970-колебательный-контур|колебательный контур]]
[[1730876231-метод-комплексных-амплитуд|метод комплексных амплитуд]]
[[1730876318-импеданс|импеданс]]
[[1729324863-правила-Кирхгофа|правила Кирхгофа]]

# Exercises
## 9.36
![[1730874841.png]]
![[1730874856.png]]

$$
\alignleft{
R = R_{кр} = 2 \sqrt{\frac{L}{C}} \\
q(t) = (A t + B) \exp{-\gamma t} \\
\dot{q}(0) = 0 \implies A - \gamma B = 0 \\
\Cases{
B = C U_0 \\
A = \gamma C U_0
} \\
I = \dot{q} = I(t) \\
\dv{t}{I} = 0 \implies \dots
}
$$

## 9.54
![[1730875158.png]]
![[1730875218.png]]
$$
\alignleft{
q = A \cos{(\omega_0 t + \phi_0)} + C \varepsilon_0 \\
\Cases{
\phi_0 = 0 \\
A = -C \varepsilon_0
} \\
U = \varepsilon_0 (1 - \cos{(\omega_0 t)}) \\
2T = \tau \\
U(0) = 0 \\
U(\frac{T}{4}) = \varepsilon_0 \\
U(\frac{T}{2}) = 2 \varepsilon_0 \\
U_{ср} = \frac{1}{T_0} \int_0^\tau{U(t) \d t} \implies \\
}
$$
$$
T_0 = \frac{\varepsilon_0 \tau}{U_{ср}}
$$
## Т12
![[1730876630.png]]
$$
\alignleft{
I R = -\Dv{t}{B_{вн} S N} - L \dot{I} \\
I = I_0 e^{i(\omega t + \phi)} \\
I_0 e^{i(\omega t + \phi)} R = 
-S N B_0 e^{i \omega t} - L I_0 i \omega e^{i (\omega t + \phi)} \\
\implies \\
I_0 e^{i \phi} = -\frac{B_0 S N i \omega}{R + i \omega L} \\
L I = B_1 S N \\
B = B_{вн} + B_1 \\
B_1 = -\frac{L B_0 i \omega}{R + i \omega L} e^{i \omega t} \\
B = B_0 t^{i\omega t} \left(1 - \frac{i \omega L}{R + i\omega L}\right) =
B_0 t^{i\omega t} \frac{R}{R + i\omega L} \implies \\
}
$$
$$
\Gather{
\abs B = B_0 \frac{1}{\sqrt{2}} \\
\phi = -\frac{\pi}{4}
}
$$
