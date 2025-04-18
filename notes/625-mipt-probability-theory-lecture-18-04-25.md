---
id: 625-mipt-probability-theory-lecture-18-04-25
aliases:
  - MIPT probability theory lecture 18-04-25
tags: []
---

# MIPT probability theory lecture 18-04-25

$$
\varphi\groupr{Be(p)}(t) = q + p e^{it}
$$

$$
\varphi\groupr{Binom(n,p)}(t) = (q + p e^{it})^n
$$

$$
\varphi\groupr{N(0,1)}(t) = e^{-\frac{t^2}{2}}
$$

$$
\varphi\groupr{N(m,\sigma^2)}(t) = e^{itm - \frac{t^2}{2} \sigma^2}
$$

$$
\sum N(m_i,\sigma_i^2) = N(\sum m_i, \sum \sigma_i^2)
$$

$$
\varphi\groupr{U(-a,a)} = \frac{\sin{at}}{at}
$$

# Theorem.

$$
\forall t\quad \varphi_{\xi_n} \xrightarrow[n \to \infty]{} \varphi_\xi
\implies
F_{\xi_n} \xrightarrow[n \to \infty]{d} F_\xi
$$

# Theorem. Муавра-Лапласа.

## If:

$\mu_n \sim Binom(n,p)$
$\eta_n \defeq \frac{\mu_n - E_{\mu_n}}{\sqrt{D_{\mu_n}}}$

## Then:

$$
F_{\eta_n}(x) \rightrightarrows F_{N(0,1)}(x),\quad n\to\infty
$$

## Proof:

$\Align{
E \mu_n = np, \quad D \mu_n = npq \\
\eta_n = \frac{\mu_n - np}{\sqrt{npq}}\\
\varphi_{\eta_n}(t) = \textit{арифметика} = \\
= \group{1 - \frac{t^2}{2n} + o(\frac{1}{n})}^n 
\xrightarrow{n \to \infty} e^{-\frac{t^2}{2}}
}$

# Замечание

$\Align{
\mu_n \sim U(-n,n) \\
\mu_n \to \mu - \textit{не случайная величина} \\
\varphi_{\mu_n} \to \Cases{
0, & t \neq 0\\
1, & t = 0
} - \textit{разрывна} \\
F_{\mu_n} \to \frac{1}{2} - \textit{не ф-ия распределения} \\
\hline
\mu_n \sim U(-\frac{1}{n},\frac{1}{n}) \\
\mu_n \to \mu \equiv 0 \\
\varphi_{\mu_n} \to 1 \\
F_{\mu_n} \to \Cases{
0, & t < 0\\
\frac{1}{2}, & t = 0 \\
1, & t \ge 0
} - \textit{не ф-ия распределения} \\
\textit{Но можно поменять в точке разрыва (в 0) так, чтобы она стала ф-ией распределения } \mu.
}$

# Gamma

$\Align{
\alpha,\lambda > 0 \\
Gamma(\alpha, \lambda) \sim
f(x) = \frac{\lambda^\alpha}{\Gamma(\alpha)} x^{\alpha - 1} e^{-\lambda x}
}$

# Def. Монетная функция

$$
M_\xi(t) \defeq E e^{t\xi}
$$
