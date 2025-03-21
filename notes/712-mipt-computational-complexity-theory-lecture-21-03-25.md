---
id: 712-mipt-computational-complexity-theory-lecture-21-03-25
aliases:
  - MIPT computational complexity theory lecture 21-03-25
tags: []
---

# MIPT computational complexity theory lecture 21-03-25
# Вероятностная модель вычислений
# ПВМТ (Полиномиальная Вероятностная Машина Тьюринга)
$M(x,r)$ - МТ
$p$ - полином.
$r \in U\group{\set{0,1}^{p(\abs{x})}}$ - ветка вычислений
$U$ - равномерное распределение

Результат работы - случайная величина.
$$
L \in PP
\stackrel{def}{\same}
\exists\ \text{ПВМТ}\ M(x,r) :
\forall x \in L \hthen
P(M(x,r) = 1) > \frac{1}{2} \\
P(M(x,r) = 0) < \frac{1}{2} \\
P(M(x,r) = 1) > \frac{1}{2} \\
P(M(x,r) = 0) < \frac{1}{2} \\
$$
