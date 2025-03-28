---
id: 670-mipt-probability-theory-lecture-21-03-25
aliases:
  - MIPT probability theory lecture 21-03-25
tags: []
---

# MIPT probability theory lecture 21-03-25

# Функция распределения случайного вектора

![1.jpg](assets/imgs/21-03-25_13-10-40_399_IMG_20250321_122458.jpg)

# Свойства

![2.jpg](assets/imgs/21-03-25_13-10-40_898_IMG_20250321_122513.jpg)
![4.jpg](assets/imgs/21-03-25_13-10-41_922_IMG_20250321_123342.jpg)

# Lemma

![5.jpg](assets/imgs/21-03-25_13-10-41_002_IMG_20250321_123554.jpg)

$B_n \defeq \bigcup_{k=1}^{n}{\set{\omega \mid a_k \le \xi_k(\omega) < b_k}}$

$$
\Gather{
\forall D \in F \hthen \\
P(B_n D) =
\sum_{\set{k_1, \dots, k_n} \in \set{0,1}^n}{
(-1)^{\sum{k_j}}
P\group{\bigcap_{j=1}^{n}\set{\omega \mid \xi_j(\omega) < x_j^{k_j}} \cap D}
}
}
$$

$x_j^0 \defeq b_j$
$x_j^1 \defeq a_j$

## Proof (by induction)

![7.jpg](assets/imgs/21-03-25_13-10-42_647_IMG_20250321_124241.jpg)
![8.jpg](assets/imgs/21-03-25_13-10-42_725_IMG_20250321_124414.jpg)
![9.jpg](assets/imgs/21-03-25_13-10-42_962_IMG_20250321_124645.jpg)

## $D = \Omega$

![10.jpg](assets/imgs/21-03-25_13-10-42_566_IMG_20250321_125131.jpg)

$$
\Gather{
P(B_n) =
\sum_{\set{k_1, \dots, k_n} \in \set{0,1}^n}{
(-1)^{\sum{k_j}} F(x_1^{k_1}, \dots, x_n^{k_n})
}
}
$$

# 5 свойств не задают функцию распределения

![12.jpg](assets/imgs/21-03-25_13-10-43_560_IMG_20250321_125641.jpg)

# Пример - Pol

![14.jpg](assets/imgs/21-03-25_13-10-43_792_IMG_20250321_130901.jpg)

# Построение случайной величины по ф-ии распределения

# Claim

$$
F_\xi(\xi) = U(0,1)
$$

# Условная функция распределения

$$
F_{\xi \mid \eta}(x \mid \eta \in B) \defeq
P(\xi < x \mid \eta \in B)
$$

# Функция плотности случайного вектора

$$
F_\xi(\vec{x}) = \int_{-\infty}^{x_1} \dots \int_{-\infty}^{x_n}{
f(u_1, \dots, u_n) \d u_1 \dots \d u_n
}
$$

# Нормальный случайный вектор

отмена...

# Математическое ожидание

$$
E \xi \defeq \int_{\Omega}{\xi(\omega) P(\d \omega)}
$$

# Свойства математического ожидания

1. $E(\xi \equiv c) = c$
2. $E(\alpha \xi) = \alpha E(\xi)$ 
3. $E(\xi_1 + \xi_2) = E(\xi_1) + E(\xi_2)$
4. $\xi = \eta\ (\textit{почти наверное - п.н. - P почти всюду})
\implies E(\xi) = E(\eta)$
5. $\xi \le \eta\ (п.н.) \implies E(\xi) \le E(\eta)$ 
6. $\xi \ge 0\ (п.н.),\quad E(\xi) \ge 0 \implies \xi = 0\ (п.н.)$
