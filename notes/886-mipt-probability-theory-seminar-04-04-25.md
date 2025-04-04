---
id: 886-mipt-probability-theory-seminar-04-04-25
aliases:
  - MIPT probability theory seminar 04-04-25
tags: []
---

# MIPT probability theory seminar 04-04-25

# Факториальный момент
$$
E x^{[n]} \defeq E \group{\prod_{i=0}^{n-1}{x - i}}
$$

# Geom(p)
$$
\bbP\set{X = k} = q^k p, \quad p+q=1
$$
$$
\Gather{
\bbE X = \frac{q}{p}\\
D X = \frac{q}{p^2}\\
\bbE x^{[n]} = n! \group{\frac{q}{p}}^n
}
$$

# Производящая функция
$$
\Phi_X(z) \defeq \bbE(z^x),\quad z \in (0,1)
$$
$$
\dv[n]{z}{} \Phi_x(z) \rvert_{z=1} = \bbE x^{[n]}
$$
$$
\Phi_x(z) = \sum_{n=0}^{\infty}{\frac{\bbE x^{[n]}}{n!} (z-1)^n}
$$
$$
P(x=k)
$$
