---
id: 977-mipt-harmonic-analysis-seminar-08-04-25
aliases:
  - MIPT harmonic analysis seminar 08-04-25
tags: []
---

# MIPT harmonic analysis seminar 08-04-25

9104306649
$
\Align{
\Phi(y) = \int_a^b{f(x,y) \d x} \\
f: [a,b) \times [c,d) \to \RR \\
\forall b_1 < b,\forall y \in [c,d) \hthen \int_a^{b_1}{f(x,y) \d x} \in \RR \\
}
$

# Равномерная сходимость

$
\Align{
\forall \varepsilon > 0 \exists b_1 \in [a,b) : 
\forall y \in [c,d) \forall b_2 > b_1 \hthen 
\abs{\int_{b_2}^{b}{f(x,y) \d x}} < \varepsilon
}
$

# Критерий Коши

$
\Align{
\forall \varepsilon > 0 \exists b_0 \in [a,b) :
\forall y \in [c,d) \forall b_1,b_2 \in [b_0,b) \hthen
\abs{\int_{b_1}^{b_2}{f(x,y) \d x}} < \varepsilon
}
$

# Следствие
$
\Align{
f(x,y) \in C \\

}
$
