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
\varphi_{\eta_n}(t) = 
}$
