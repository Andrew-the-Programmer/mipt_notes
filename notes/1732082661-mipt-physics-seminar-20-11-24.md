---
id: 1732082661-mipt-physics-seminar-20-11-24
aliases:
  - MIPT physics seminar 20-11-24
tags: []
---

# MIPT physics seminar 20-11-24
# Theory
## [[1730456261-модуляция-принцип-радиосвязи|Амплитудная модуляция АМ]]
$$
\alignleft{
U = U_0 (1 + m \cos{\Omega t}) \cos{\omega t} \\
U = U_0 \Re{\left(e^{i \omega t} + \frac{m}{2} e^{i (\omega + \Omega) t} + \frac{m}{2} e^{i (\omega - \Omega) t}\right)} \\
}
$$
## [[1730456261-модуляция-принцип-радиосвязи|Фазовая модуляция ФМ]]
$$
\alignleft{
U = U_0 \cos{(\omega t + m \cos{\Omega t})} \\
U = U_0 \Re{e^{i \omega t} e^{i m \cos{\Omega t}}} =
e^{i m \cos{\Omega t}} = 1 + i m \frac{e^{i \Omega t} + e^{-i \Omega t}}{2} \\
U = U_0 \Re{\left(e^{i \omega t} + \frac{m}{2} e^{i (\omega + \Omega) t +
\frac{\pi}{2}} + \frac{m}{2} e^{i (\omega - \Omega) t + \frac{\pi}{2}}\right)} \\
}
$$
# Exercises
## 11.10
![[1732082881.png]]
![[1732082897.png]]
$$
\alignleft{
\varepsilon = \varepsilon_0 \cos^2{\omega t} \\
2 \omega = \frac{1}{\sqrt{LC}}
\varepsilon = \frac{\varepsilon_0}{2} + \frac{\varepsilon_0 \cos{(2 \omega t)}}{2} \\
\text{Разделим ток на постоянный и гармонический} \\
J_{11} = \frac{\varepsilon_0}{2(R + R_1)}, \quad
J_{12} = 0 \\
Z_{LC} = \frac{i n \omega^2 LC - i}{2 \omega C} = 0 \\
J_{21} = 0 \\
\frac{\varepsilon_0 e^{i 2 \omega t}}{2} = R J_{22} \\
J_{22} = \frac{\varepsilon_0 e^{i 2 \omega t}}{2 R} \\
}
$$
![[1732086705.png]]
## T15
![[1732083880.png]]
![[1732084168.svg]]
$$
\alignleft{
Q \varepsilon_0 \cdot \frac{m}{2} \varepsilon_0 = \varepsilon_0 U(\omega_0) \\
U(\omega_0) = \frac{U_0 Q}{\sqrt{Q^2 \left(\frac{2\Delta \omega}{\omega_0}\right)}} =
\frac{U_0}{3} \\
m = \frac{2}{75}
}
$$
## T16 (решал у доски)
![[1732085912.png]]
![[1732087286.png]]
![[1732087296.png]]
![[1732087309.png]]
## 11.36
![[1732085730.png]]
$$
\alignleft{
T = 2\pi \sqrt{LC} \gg \tau \\
W = \frac{q^2}{2 C} \\
\d W = -\frac{q^2}{2} \frac{\d C}{C^2} \\
q(t) = q_0 \sin{\omega t} \\
\d W = \frac{q_0^2 \frac{\tau^2}{LC}}{2 C^2} \d C \\
Q = 2\pi \frac{W}{\Delta W} \\
\d W = \frac{2\pi W}{Q} = \frac{q_0^2 \tau^2}{2 L C^3} \d C \\
\Delta C = \frac{\pi R C^{\frac{5}{2}} \sqrt{L}}{\tau^2}
}
$$
![[1732086730.png]]
## T18
![[1732086845.png]]
$$
\alignleft{
I = I_0 + S U_1 = I_0 + \frac{q}{C_1} S \\
\dot{q} = I + I_L \\
\dot{I} = \dot{q} \frac{S}{C_1} \\
\ddot{q} - \dot{q} \frac{S}{C_1} = \dot{{I}_{1}} = -\frac{q}{L C_1} \\
\ddot{q} - 2 \gamma \dot{q} + \omega_0 q = 0 \\
\gamma = \frac{S}{2 C_1}, \quad \omega_0 = \frac{1}{\sqrt{LC}} \\
q = q_0 e^{i \omega t} \\
\omega = -i\gamma \pm \sqrt{\omega_0^2 - \gamma^2}
}
$$

