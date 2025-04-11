---
id: 648-mipt-probability-theory-seminar-11-04-25
aliases:
  - MIPT probability theory seminar 11-04-25
tags: []
---

# MIPT probability theory seminar 11-04-25

# Характеристическая функция

# Примеры

1. $\xi \equiv const$

$$
\varphi_{c}(t) = e^{itc}
$$

2. $\xi = 0$

$$
\varphi_0 = 1
$$

# 3. $\xi \sim \mcN(0,1)$

$\Align{
f_\xi(x) = \frac{1}{\sqrt{2\pi}} e^{-\frac{x^2}{2}} \\
\varphi_\xi(t) = \frac{1}{\sqrt{2\pi}} \int_{-\infty}^{+\infty}{e^{itx} e^{-\frac{x^2}{2}} \d x} = \\
\frac{1}{\sqrt{2\pi}} \int_{-\infty}^{+\infty}{\cos(tx) e^{-\frac{x^2}{2}} \d x} \\
\sqrt{2\pi} \pdv{t}{} \varphi_\xi(t) = 
\int_{-\infty}^{+\infty}{\sin(tx) (-x) e^{-\frac{x^2}{2}} \d x} = \\
\int_{-\infty}^{+\infty}{\sin(tx) \d\group{e^{-\frac{x^2}{2}}}} = \\
-t \int_{-\infty}^{+\infty}{\cos(tx) e^{-\frac{x^2}{2}} \d x}\\
\pdv{t}{} \varphi_\xi(t) = -t \varphi_\xi(t) \\
\varphi_\xi(t) = e^{-\frac{t^2}{2}}
}$

$$
\varphi_{\mcN(0,1)}(t) = e^{-\frac{t^2}{2}}
$$

$f_{\mcN(m,\sigma^2)}(x) = \frac{1}{\sqrt{2\pi\sigma^2}} e^{-\frac{(x-m)^2}{2\sigma^2}}$
$\mcN(m,\sigma^2) = m + \sigma \mcN(0,1) \implies$

$$
\varphi_{\mcN(m,\sigma^2)}(t) = e^{itm - \frac{(\sigma t)^2}{2}}
$$

# 4. $\xi \sim Be(p)$

$$
\varphi_{Be(m,\sigma^2)}(t) = p e^{it} + q
$$

# 5. $\xi \sim Binom(n,p)$

$\Align{
Binom(n,p) \sim \sum_{i=1}^{n}{Be(p)}
}$

$$
\varphi_{Binom(n,p)} = \group{p e^{it} + q}^n
$$

# 6. Стремление к нормальному.

$\Align{
P(\xi = 1) = P(\xi = -1) = \frac{1}{2} \\
\varphi\_\xi(t) = \frac{1}{2} e^{it} + \frac{1}{2} e^{-it} = \cos(t)\\
\xi_1,\dots,\xi_n \\
\eta_n \defeq \frac{1}{\sqrt{n}} \sum{\xi_i} \\
\varphi_{\eta_n} = \cos^n(t) \\
\varphi_{\eta_n}(t) \to e^{-\frac{t^2}{2}},\quad n \to \infty \\
\eta_n \to \mcN(0,1),\quad n \to \infty
}$

# 7 

$$
\varphi_{U(0,1)}(t) = \frac{e^{it} - 1}{it}
$$
$U(a,b) = (b-a) U(0,1) + a$
$$
\varphi_{U(a,b)}(t) = \frac{e^{itb} - e^{ita}}{it(b-a)}
$$
$$
\varphi_{U(-1,1)}(t) = \frac{\sin t}{t}
$$

$\Align{
\xi_1,\dots,\xi_n - \textit{норсв}\ U(-1,1) \\
\eta_n \defeq \frac{1}{\sqrt{n}} \sum{\xi_i} \\
\varphi_{\eta_n} = \cos^n(t) \\
\varphi_{\eta_n}(t) \to e^{-\frac{t^2}{2}},\quad n \to \infty \\
\eta_n \to \mcN(0,1),\quad n \to \infty
}$
