---
id: 1731479149-mipt-physics-seminar-13-11-24
aliases:
  - MIPT physics seminar 13-11-24
tags: []
---

# MIPT physics seminar 13-11-24
[[1729328970-колебательный-контур|колебательный контур]]

# Exersises
## 10.92
![[1731479748.png]]
![[1731479891.png]]
![[1731479773.png]]

$$
\alignleft{
\omega_0 = 1000 \\
\Delta \omega \approx 10 \\
Q = \frac{\omega_0}{2 \omega} = 50 \\
Q \varepsilon = 100 \implies \varepsilon = 2 \\
Q = \frac{1}{r} \sqrt{\frac{L}{C}} \implies \frac{L}{C} = 10^4 \\
\omega_0 = \frac{1}{\sqrt{LC}} \implies LC = 10^{-6} \\
L = 10^{-1} \\
C = 10^{-5} \\
r + R = \sqrt{\frac{L}{C}} = 10^2 \\
R = 98 \\
\delta = \frac{r}{2L} = 10 \\
}
$$
![[1731480649.png]]

## T14
![[1731480757.png]]
$$
\alignleft{
\Cases{
R \dot{{q}_{1}} + \frac{q_1}{C} = 
\varepsilon e^{i \omega t} - L_1 \ddot{{q}_{1}} - M \ddot{{q}_{2}}\\
L_2 \ddot{{q}_{2}} + M \ddot{{q}_{1}} = 0
} \\
\ddot{{q}_{1}} + \dot{{q}_{1}} \frac{R}{L_1 + \frac{M^2}{L_2}} + 
q_1 \frac{1}{C(L_1 + \frac{M^2}{C_2})} = 
\varepsilon \cdot e^{i \omega t} \frac{1}{L_1 + \frac{M^2}{L_2}} \\
\gamma = \frac{R}{2(L_1 + \frac{M^2}{L_2})}, \quad \omega_0^2 = \frac{1}{C(L_1 + \frac{M^2}{C_2})} \\
\tg{\delta} = \frac{2 \gamma \omega}{\omega_0^2 - \omega^2} \\
\delta = \frac{3}{4} \pi \\
-1 = \frac{\frac{R}{L_1 + \frac{M^2}{L_2}} \omega}{\frac{1}{C(L_1 + \frac{M^2}{C_2})} - \omega^2}
}
$$
## 10.25
![[1731481720.png]]
![[1731481743.png]]
$$
\alignleft{
\frac{1}{z} = \frac{1}{i\omega L} + i \omega C +
\frac{2}{i \omega L + \frac{1}{i \omega C}} \\
\text{Резонанс:}\ z = 0 \lor z = \infty \\
z = \infty \implies \\
\omega_0^2 = \frac{1}{LC} \\
z = 0 \implies \\
\omega_1^2 = \frac{2 - \sqrt{3}}{LC} \\
\omega_2^2 = \frac{2 + \sqrt{3}}{LC} \\
}
$$

![[1731481677.png]]

## 10.23
![[1731482416.png]]
$$
\alignleft{
C = \frac{\varepsilon_0 S}{h} \\
\d C = -\frac{\varepsilon_0 S}{h^2} \d h \\
\frac{\d C}{C} = - \frac{\d h}{h}\\
\omega_0 = \frac{1}{\sqrt{LC}} \\
\d \omega_0 = -\frac{1}{2} \frac{\d C}{\sqrt{L} C^{\frac{3}{2}}} \\
\frac{\d \omega_0}{\omega_0} = -\frac{1}{2} \frac{\d C}{C} = \frac{1}{2} \frac{\d h}{h} \\
V(\omega) = \frac{V Q}{\sqrt{1 + Q \left(\frac{2 \Delta \omega}{\omega_0}\right)^2}} \approx
VQ \left(1 - \frac{1}{2} Q \left(\frac{2 \Delta \omega}{\omega_0}\right)^2 \right)\\
\Delta V(\omega) = \abs{V(\omega) - VQ} = \frac{1}{2} V Q^2 \left(\frac{2 \Delta \omega}{\omega_0}\right)^2 =\\
\Delta V = \frac{1}{2} V Q^2 \frac{{\Delta h}^2}{h^2} \\
\Delta h = \frac{h}{Q} \sqrt{\frac{2 \Delta V}{V}}
}
$$
![[1731492767.png]]
