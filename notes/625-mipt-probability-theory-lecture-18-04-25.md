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

# Def. Моментная функция.

$$
M_\xi(t) \defeq E e^{t\xi}
$$

$$
M_\xi(it) = \varphi_\xi(t)
$$

# Gamma

$\Align{
\alpha,\lambda > 0 \\
\xi \sim Gamma(\alpha, \lambda) \sim
f(x) = \frac{\lambda^\alpha}{\Gamma(\alpha)} x^{\alpha - 1} e^{-\lambda x} \\
M_\xi(t) = \group{\frac{\lambda}{\lambda - t}}^{\alpha} \\
}$

$$
\Gather{
\varphi\groupr{Gamma(\alpha, \lambda)}(t) = \group{\frac{\lambda}{\lambda - it}}^{\alpha} \\
\sum Gamma(n_i,\lambda) = Gamma(\sum n_i,\lambda)
}
$$

# Exp

$Exp(\lambda) \sim Gamma(1,\lambda)$

$$
\Gather{
\varphi\groupr{Exp(\lambda)}(t) = \frac{\lambda}{\lambda - it} \\
Gamma(n,\lambda) = \sum_{i=1}^{n}{Exp_i(\lambda)}
}
$$

# $\chi^2$

$\chi^2(n) \sim Gamma(\frac{n}{2}, \frac{1}{2})$

$$
\Gather{
\varphi\groupr{\chi^2(n)}(t) = \group{\frac{\frac{1}{2}}{\frac{1}{2} - it}}^{\frac{n}{2}} \\
\chi^2(n) \sim \sum_{j=1}^{n}{\chi^2_j(1)}
}
$$

$\chi^2(1) \sim N^2(0,1)$
$N^2(0,1) + N^2(0,1) \sim Exp(\frac{1}{2})$

# Распределение Коши - $K$

$$
K(a,\sigma) \sim f(x) = \frac{1}{\pi \sigma (1 + \group{\frac{x-a}{\sigma}}^2)}
$$

$\Align{
\varphi_{K(0,1)}(t) = e^{-\abs{t}}
}$

$$
\varphi\groupr{K(a,\sigma)} = e^{ita - \sigma \abs{t}}
$$

# Обобщенное нормальное распределение

$$
N(m_\xi, R_\xi) \sim
f(x) = \frac{1}{(2\pi)^{n/2} \sqrt{\det R_\xi}}
\exp{-\frac{1}{2}\groupr{(x - m_\xi)^T R_\xi\inv (x - m_\xi)}}
$$

# Def. Хар. ф-ия случайного вектора

$$
\varphi_{\vec{\xi}}(\vec{t}) = E e^{i t^T \xi}
$$

$\eta = B \xi$
$B$ - невырожденное лин. преобразование

$$
\Gather{
m_\eta = B m_\xi \\
R_\eta = B R_\xi B^T \\
\xi \sim N(m_\xi, R_\xi) \implies \eta \sim N(m_\eta, R_\eta)
}
$$
