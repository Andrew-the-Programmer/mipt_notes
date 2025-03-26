---
id: 909-mipt-differential-equations-lecture-26-03-25
aliases:
  - MIPT differential equations lecture 26-03-25
tags: []
---

# MIPT differential equations lecture 26-03-25

# АСДУ

автономная система ду

$$
\dv{t}{\vec{x}} = \vec{f}(x)
$$

# Lemma 1

![1.jpg](assets/imgs/26-03-25_15-29-20_659_IMG_20250326_110554.jpg)
![2.jpg](assets/imgs/26-03-25_15-29-20_841_IMG_20250326_110558.jpg)

АСОДУ можно свести к неавтономной в окр. точки неравновесия.

# Устойчивое решение

![2.jpg](assets/imgs/26-03-25_15-29-20_841_IMG_20250326_110558.jpg)

мало меняется при изменении начальных условий.

# Устойчивость по Ляпунову

![4.jpg](assets/imgs/26-03-25_15-29-20_079_IMG_20250326_111341.jpg)

Решение $\vec{x}(t)$ АСОДУ $\dv{t}{x} = f(x)$ называется **_устойчивым по Ляпунову_**, если:

1. $\forall x^\star \in U_\delta(x_0)$ - решение ЗК $\Cases{
\dv{t}{x} = f(x) \\
x(t_0) = x^\star
}$ существует $\forall t > t_0$

2. $$
   \forall \varepsilon > 0 \ \exists \delta_\varepsilon > 0 :
   \forall x^\star \in U_{\delta_\varepsilon}(x_0) \hthen
   \abs{\vec{x}(t, x^\star) - \vec{x}(t_0, x_0)} < \varepsilon
   \quad
   \forall t > t_0
   $$

# Ассимптотическая устойчивость

![3.jpg](assets/imgs/26-03-25_15-29-20_657_IMG_20250326_111328.jpg)

1. Устойчивость по Ляпунову
2. $x_0$ - положение равновесия
3. $$
   \forall \varepsilon \exists \delta^\star \le \delta_\varepsilon :
   \forall x^\star \in U_{\delta^\star}(x_0) \hthen
   \abs{\vec{x}(t, x^\star) - \vec{x}(t_0, x_0)} \to 0,\quad t \to \infty
   $$

# Пример Ф.889

![5.jpg](assets/imgs/26-03-25_15-29-20_072_IMG_20250326_114221.jpg)

# Линейная система

![6.jpg](assets/imgs/26-03-25_15-29-20_255_IMG_20250326_114224.jpg)

$$
\dv{t}{z} = A z
$$

$A = (a_{ij})$
$a_{ij} = const = \pdv{x_j}{f_i}\rvert_{x=x_0}$

# Th 1

![7.jpg](assets/imgs/26-03-25_15-29-20_924_IMG_20250326_114227.jpg)
![8.jpg](assets/imgs/26-03-25_15-29-20_535_IMG_20250326_114416.jpg)
![9.jpg](assets/imgs/26-03-25_15-29-20_455_IMG_20250326_120134.jpg)
![10.jpg](assets/imgs/26-03-25_15-29-21_166_IMG_20250326_120138.jpg)
![11.jpg](assets/imgs/26-03-25_15-29-21_634_IMG_20250326_120143.jpg)

$\set{\lambda_i}_{i=1}^{n}$ - собственные значения A

$$
\AlignCenter{
\forall i \Re \lambda_i < 0 \implies x_0 - пр \\
\exists i \Re \lambda_i > 0 \implies x_0 - не\ пр
}
$$

# Th 2

![12.jpg](assets/imgs/26-03-25_15-29-21_090_IMG_20250326_120348.jpg)
![13.jpg](assets/imgs/26-03-25_15-29-21_881_IMG_20250326_121258.jpg)
![14.jpg](assets/imgs/26-03-25_15-29-21_982_IMG_20250326_121301.jpg)

$\dv{t}{x} = f(x) = f(x_0) + A (x - x_0) + o(x - x_0)$
$\set{\lambda_i}_{i=1}^{n}$ - собственные значения A

$$
\forall i \Re \lambda_i < 0 \implies x_0 - \textit{ассимптотически устойчивое пр}\\
$$
