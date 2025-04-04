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
\bbE x^{[n]} = n! \group{\frac{q}{p}}^n \\
\Phi_x(z) = \frac{p}{1 - zq}
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
P(x=k) = \frac{1}{2\pi i} \oint{\frac{\Phi(z)}{z^{k+1}}\d z}
$$

$\set{x_i}$ - НСВ

$$
\Phi_{\sum{x_i}}(z) = \prod{\Phi_{x_i}(z)}
$$

# $NBinom(r,p)$

$$
\bbP\set{y=k} = C_{k+r}^{k} q^k p^r
$$

$$
NBinom(r,p) \sim \sum_{k=1}^{r}{Geom(p)}
$$

$$
\Gather{
\bbE y = r \frac{q}{p} \\
D y = r \frac{q}{p^2} \\
\Phi_y(z) = \group{\frac{p}{1 - zr}}^r
}
$$

# $Poiss(\lambda)$

$$
\bbP(x=k) = e^{-\lambda}\frac{\lambda^k}{k!}
$$

$$
\Gather{
\Phi_x(z) = e^{\lambda(z-1)} \\
\bbE x^{[n]} = \lambda^n
}
$$

$$
X_i \sim Poiss(\lambda_i) \implies \sum{X_i} \sim Poiss(\sum{\lambda_i})
$$

$
\AlignCenter{
\Phi_{\sum{x_i}}(z) = \prod{\Phi_{x_i}(z)} = \prod{e^{-\lambda_i(z-1)}} = 
e^{-\sum{\lambda_i(z-1)}} \sim Poiss(\sum{\lambda_i}) \\
\bbP\set{x+y=k} = \sum_{l=0}^{\infty}{\bbP\set{x+y = k \mid y = l}} =
\sum_{l=0}^{k}{\bbP\set{x = k - l} \bbP\set{y=l}} = \dots
}
$

# Задача

$
\AlignCenter{
Y_N = \sum_{i=0}^{N-1}{x_i} \\
x_i \sim 1 + Geom(1 - \frac{i}{N}) \\
\bbE Y_N = \sim_{i=0}^{N-1}{\bbE x_i} = N \sum_{n=1}^{N}{\frac{1}{n}} \\
\bbE Y_N \to N \ln{N} \\
D Y_N = N^2 \sum_{n=1}^{N}{\frac{1}{n^2}} - N \sum_{n=1}^{N}{\frac{1}{n}} \\
D Y_N \to N^2 \frac{\pi^2}{6}
}
$

$$
\Gather{
Y_N = \sum_{i=0}^{N-1}{x_i} \\
D Y_N \to N^2 \frac{\pi^2}{6}
}
$$
