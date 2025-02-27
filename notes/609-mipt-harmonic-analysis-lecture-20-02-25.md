---
id: 609-mipt-harmonic-analysis-lecture-20-02-25
aliases:
  - MIPT harmonic analysis lecture 20-02-25
tags: []
---

# MIPT harmonic analysis lecture 20-02-25

# Lemma

![[1740067802.png]]

$$
g(u) = \frac{1}{\tg{\frac{u}{2}}} - \frac{2}{u}
$$

## Proof

![[1740667518.png]]
![[1740667583.png]]

# Theorem

![[1740068457.png]]

## Proof

![[1740667942.png]]

$$
\AlignLeft{
n \to \infty \\
S_n[f](x) \sim \int_{-\pi}^{\pi}{f(x+u) \frac{\sin{nu}}{u} \d x} =
\int_{-\pi}^{\pi}{f(x-u) \frac{\sin{nu}}{u} \d x} \\
S_n[f](x) \sim \int_{-\pi}^{\pi}{(f(x+u) + f(x-u)) \frac{\sin{nu}}{u} \d x}
\sim \int_{0}^{\pi}{(f(x+u) + f(x-u)) \frac{\sin{nu}}{u} \d x}
\\
\forall \delta > 0 \hthen \\
S_n[f](x) \sim \int_{0}^{\delta}{(f(x+u) + f(x-u)) \frac{\sin{nu}}{u} \d x} \\
}
$$

# Принцип локализации для рядов Фурье

![[1740669964.png]]

# Признаки сходимости ряда Фурье в точке

## Theorem. Признак Дини[-Липшица]

![[1740670500.png]]

## Proof
![[1740670964.png]]
![[1740670992.png]]
![[1740671049.png]]









