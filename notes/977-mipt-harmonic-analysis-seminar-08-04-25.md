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
\Phi \in \tilde{C} \\
\same \\
\forall \varepsilon > 0 \exists b_0 \in [a,b) :
\forall y \in [c,d) \forall b_1,b_2 \in [b_0,b) \hthen
\abs{\int_{b_1}^{b_2}{f(x,y) \d x}} < \varepsilon
}
$

# Следствие

$
\Align{
f(x,y) \in C \\
\Cases{
\Phi[c,d) \in \RR \\
\Phi(d) \not\in \RR \\
} \implies
?
}
$

# $\Phi \in C$

$
\Align{
\Cases{
f(x,y) \in C \\
\Phi \in \tilde{C} \\
}
\implies 
\Phi(y) \in C
}
$

# $\Phi \in D_y$

$
\Align{
\Cases{
f(x,y) \in D_y \\
\int_a^b{f_y(x,y) \d x} \in \tilde{C}
}
\implies 
\Phi(y) \in D_y, \\
\Phi_y = \int_a^b{f_y \d x} \\
}
$

# $\Phi \in R$

$
\Align{
\Cases{
f(x,y)\ инт.\ на\ [a,b_1] \times [c,d_1],\quad b_1 \in [a,b), d_1 \in [c,d) \\
\int_a^b{f(x,y) \d x} \in \tilde{C}
}
\implies \\
\int_c^d{\d y \int_a^b{f(x,y) \d x}} = \int_a^b{\d x \int_c^d{f(x,y) \d y}}
}
$

# Признак Вейерштрасса

$
\Align{
0 \le \abs{f(x,y)} < g(x) \\
\int_a^b{g(x)} \in \RR \\
\implies \\
\Phi(y)\ \textit{сх-ся абсолютно и равномерно}
}
$

# Дирихле и Абель

$\int_a^b{f(x,y) \d x}$

Дирихле:
$
\Cases{
f \rightrightarrows 0,\quad x \to b \\
\int_a^b{g(x,y) \d x}\ \textit{равн. огр.}
}
$
Абель:
$
\Cases{
f \rightrightarrows 0,\quad x \to b \\
\int_a^b{g(x,y) \d x}\ \textit{сх-ся равн.}
}
$
