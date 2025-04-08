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

# Дирихле:

$
\Cases{
f\ \textit{монотонно убывает по}\ x \\
f \rightrightarrows 0,\quad x \to b \\
\int_a^b{g(x,y) \d x}\ \textit{равн. огр.}
}
$

# Абель:

$
\Cases{
f\ \textit{монотонна по}\ x\ и\ \textit{равн. огр.} \\
\int_a^b{g(x,y) \d x}\ \textit{сх-ся равн.}
}
$

# Примеры

Показать равномерную сходимость.

$$
\Gather{
\Phi(x) \defeq \int_0^{+\infty}{x^\alpha y^{\alpha + \beta + 1} e^{-(1+x)y}\d y} \\
F(y) \defeq \int_0^{+\infty}{x^\alpha y^{\alpha + \beta + 1} e^{-(1+x)y}\d x} \\
}
$$

$\alpha,\beta > 0$

$
\Align{
\Phi(x) \le C(y) \int_0^{+\infty}{y^{\beta + 1} e^{-y} \d y} \\
\dots \\
F(y) \le y^\beta e^{-y} \int_{by}^{+\infty}{t^\alpha e^{-t}\d t} \\
\dots \\
}
$

# Интеграл Дирихле

$$
I(\alpha) \defeq \int_0^{+\infty}{\frac{\sin{\alpha x}}{x} \d x}
$$

$\Align{
I(\alpha, \beta) \defeq \int_0^{\infty}{e^{-\beta x} \frac{\sin{\alpha x}}{x} \d x} \\
I(\alpha, 0) = I(\alpha) \\
I(0,\beta) = 0 \\
I_\alpha = \int_0^{\infty}{e^{-\beta x} \cos{\alpha x} \d x} = 
\frac{\beta}{\alpha^2 + \beta^2} \\
I(\alpha, \beta) - I(0,\beta) = 
\int_0^\alpha{\frac{\beta}{t^2 + \beta^2} \d t} =
\arctan{\frac{\alpha}{\beta}} \\
I(\alpha, \beta) \to sign(\alpha) \frac{\pi}{2},\quad
\beta \to +0 \\
I(\alpha,\beta) \in C_\beta \\
I(\alpha, 0) = I(\alpha) = \lim_{\beta \to +0}{I(\alpha, \beta)} 
}$

$$
I(\alpha) = sign(\alpha) \frac{\pi}{2}
$$

# Пример 2. Интеграл Пуассона

$$
I \defeq \int_0^{+\infty}{e^{-x^2} \d x}
$$

$\Align{
x = y t \\
I = \int_0^{+\infty}{e^{-y^2 t^2} t \d y} \\
I e^{-t^2} = \int_0^{+\infty}{e^{-(y^2 + 1) t^2} t \d y} \\
I \int_0^{\infty}{e^{-t^2} \d t} = 
\int_0^{\infty}{\d t \int_0^{\infty}{e^{-(y^2 + 1) t^2} t \d y}} = \\
\int_0^{\infty}{\d t \int_0^{\infty}{e^{-(y^2 + 1) t^2} t \d y}} =
}$
