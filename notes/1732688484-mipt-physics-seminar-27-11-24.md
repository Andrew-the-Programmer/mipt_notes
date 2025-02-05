---
id: 1732688484-mipt-physics-seminar-27-11-24
aliases:
  - MIPT physics seminar 27-11-24
tags: []
---

# MIPT physics seminar 27-11-24
[[1730271345-уравнения-Максвелла|уравнения Максвелла]]
## 12.81
![[1732688719.png]]
![[1732691847.png]]
$$
\alignleft{
\sigma, \sigma_1, \sigma_2 \\
\sigma_2 = \varepsilon \sigma_1 \\
q = q_1 + q_2 = S_1 \sigma_1 + S_2 \sigma_2 = 
\pi R_1^2 \sigma_1 + \pi (R_2^2 - R_1^2) \varepsilon \sigma_1 = 
\pi \sigma_1 (\varepsilon R_2^2 - R_1^2 (\varepsilon - 1)) \\
I = \dot{q} = \pi \dot{{\sigma}_{1}} (\varepsilon R_2^2 - R_1^2 (\varepsilon - 1)) \\
\dot{{\sigma}_{1}} = \frac{I}{\pi (\varepsilon R_2^2 - R_1^2 (\varepsilon - 1))} \\

H(x) 2\pi x = \frac{4\pi}{c} (I + I_{tr}) \\

x \le R_1: \\
E = 4\pi \sigma_1 \\
D = E \\
\dot{D} = \dot{E} = 4\pi \dot{{\sigma}_{1}} \\
I = 0, \quad j_{tr} = \frac{1}{4\pi} \dv{t}{D} \\
j_{tr} = \frac{1}{4\pi} \dv{t}{D} = \dot{{\sigma}_{1}} = \frac{I}{\pi (\varepsilon R_2^2 - R_1^2 (\varepsilon - 1))} \\
I_{tr} = \pi x^2 j_{tr} \\
H(x) 2\pi x = \frac{4\pi}{c} I_{tr} = \frac{4\pi}{c} j_{tr} \pi x^2 \\
H = \frac{2\pi}{c} x j_{tr} = \frac{1}{c} \frac{2I x}{\varepsilon R_2^2 - R_1^2 (\varepsilon - 1)} \\
H(x > R_2) = 0 \\
}
$$
![[1732691912.png]]
## 12.27
![[1732690572.png]]
![[1732690605.png]]
$$
\alignleft{
\oint{H \d l} = H_z l = \frac{4\pi}{c} n I l \\
H_z = \frac{4\pi}{c} n I \\
2\pi x H_\varphi = \frac{4\pi}{c} I \\
H_\varphi = \frac{I}{c x} \\
2\pi x n E = n \ae 4\pi E - \frac{2\ae}{x} \\
\Delta \varphi = I R = \int_{r_1}^{r_2}{\frac{2\ae}{x}} = 2 \ae \ln{\frac{r_2}{r_1}} \\
\ae = \frac{IR}{\ln\frac{r_2}{r_1}} \\
E = \frac{2 IR}{x \ln\frac{r_2}{r_1}} \\
S = \frac{c}{4\pi} E \times H \\
S_z = \frac{c}{4\pi} E H_\varphi = \frac{I^2 R}{2\pi x^2 \ln\frac{r_2}{r_1}}\\
S_\varphi = \frac{I^2 R n}{x \ln\frac{r_2}{r_1}}\\
W = I^2 R = \int_{r_1}^{r_2}{S_z 2\pi x \d x} \\
}
$$
![[1732691590.png]]
## T19
![[1732692085.png]]
$$
\alignleft{
E_1 = e_3 E_o \exp{i (kx - \omega t)} \\
E_2 = e_3 E_o \exp{i (ky - \omega t)} \\
\rot E_1 = -\frac{1}{c} \dv{t}{H} = i \vecprod{e_1}{e_3} k E_0 \exp{i(kx - \omega t)} \\
H
}
$$
