---
id: 230-mipt-field-theory-seminar-19-02-25
aliases:
  - MIPT field theory seminar 19-02-25
tags: []
---

# MIPT field theory seminar 19-02-25
[[768-прецессия-Томаса|прецессия Томаса]]
$$
\AlignLeft{
\delta_{ij} \delta_{jk} = \delta_{ik} \\
\delta_{ij} \delta_{kj} = \delta_{ik} \\
\delta_{ij} \delta_{ij} = 3 \\
e_{ijk} e_{ijk} = 3! = 6 \\
e_{ijk} e_{ijl} = \alpha \delta_{kl} = \frac{6}{3} \delta_{kl} = 2 \delta_{kl} \\
e_{ikl} e_{imn} = \alpha \delta_{km} \delta_{ln} + \beta \delta_{kn} \delta_{lm} + \gamma \delta_{kl} \delta_{mn} \\
Переставим\ k,l \implies \gamma = 0 \\
\alpha = -\beta \\
e_{ikl} e_{ikn} = 2 \delta_{ln} = \alpha (3 \delta_{ln} - \delta_{ln}) = \alpha 2 \delta_{ln} \\
\alpha = 1 \\
e_{ikl} e_{imn} = \delta_{km} \delta_{ln} - \delta_{kn} \delta_{lm}
}
$$
$$
\Gather{
e_{ijk} e_{ijk} = 6 \\
e_{ijk} e_{ijl} = 2 \delta_{kl} \\
e_{ikl} e_{imn} = \delta_{km} \delta_{ln} - \delta_{kn} \delta_{lm}
}
$$
$$
\AlignLeft{
1)\ a \times (b \times c) \\
= e_{ijk} a_j e_{klm} b_l c_m = 
e_{kij} e_{klm} a_j b_l c_m = 
(\delta_{il} \delta_{jm} - \delta_{im} \delta_{jl}) a_j b_l c_m = \\
b_i \veccross{a}{c} - c_i \veccross{a}{b} \\
\\
2)\ (a \times b) \cdot (c \times d) \\
e_{ijk} a_j b_k e_{imn} c_m d_n = 
e_{ijk} e_{imn} a_j b_k c_m d_n =
(\delta_{jm} \delta_{kn} - \delta_{jn} \delta_{km}) a_j b_k c_m d_n = \\
\veccross{a}{c} \veccross{b}{d} - \veccross{a}{d} \veccross{b}{c}
}
$$
