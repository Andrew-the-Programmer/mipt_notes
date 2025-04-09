---
id: 879-mipt-differential-equations-lecture-09-04-25
aliases:
  - MIPT differential equations lecture 09-04-25
tags: []
---

# MIPT differential equations lecture 09-04-25

# Первые Интегралы АСОДУ

# Пример 1

![1.png](assets/imgs/09-04-25_11-29-16_511_09-04-25_11-29-12_739.png)
![2.jpg](assets/imgs/09-04-25_11-29-34_977_IMG_20250409_105417.jpg)

# Вопрос-Ответ

Вопрос: как найти решение не в окр. ПР?
Ответ: первые интегралы!

# Def. Первый интеграл АСОДУ.

$U: \RR^n \to \RR$

1. $U \in C^1$
2. $U \not\equiv const$
3. $x(t)$ - решение АСОДУ $\dot{x} = f(x) \implies U(x(t)) \equiv const$

# Claim 1

Есть хотябы один ПИ, то есть и бесконечно много.

# Независимые ПИ

Ф-ии $U_1(x),\dots,U_m(x)$ называют **_функционально зависимыми_**, если одну из них можно "выразить" через другие, т.е.

$$
\exists j:
U_j(x) = W(U_1(x), \dots, U_{j-1}(x), U_{j+1}(x), \dots, U_m(x))
$$

# Пример

$u_1 = x_1,\quad u_2 = x_2,\quad u_3 = x_1^2 + x_2^2$
Линейно не зависимы.
Но функционально зависимы.

# Lemma 1.

Функциональная [не]зависимость инвариантна отн. гладкой невырожденной замены переменных.

## Proof

# Def. Производная в силу системы. Производная Ли.

$V: \RR^n \to \RR$
Производная ф-ии $V(x)$ в силу системы $\dot{x} = f(x)$:

$$
\veccross{\grad V}{f}
$$

Синонимы:

- Производная в силу системы
- Производная Ли
- Производная вдоль векторного поля
- Производная вдоль траектории

# Theorem 1. Критерий ПИ

$$
\Gather{
U - \textit{ПИ} \\
\same \\
\veccross{\grad U}{f} = 0
}
$$

## Proof

$\Align{
0 = \dv{t}{} U(x(t)) = \sum{\pdv{x_k}{u} f_k} \stackrel{x - \textit{решение}}{=} \sum{\pdv{x_k}{u} \pdv{t}{x_k}} = \veccross{\grad U}{f}
}$

# Пример 3

![3.jpg](assets/imgs/09-04-25_11-35-03_764_IMG_20250409_113429.jpg)

# Lemma 2.

ПИ АСОДУ инвариантны отн. гладкой невырожденной замены переменных.

## Proof

$\Align{
u - \textit{ПИ} \same \veccross{\grad u}{f} = 0 \\
y = g(x) \\
G_{ij} \defeq \group{\pdv{x_j}{g_i}} \\
\dot{y} = G f = F \\
\grad_x u(x) = G^T \grad_y u(y) \\
0 = \dot{u} = \veccross{\grad_x u}{f} = \veccross{G^T \grad_y u}{G\inv F} =
\veccross{\grad_y u}{F} \\
\blacksquare
}$

# Claim.

Градиенты функционально зависимых ф-ий линейно зависимы во всех точках.

$$
\sum{\alpha_k(x) \grad u_k(x)} = 0
$$

## Proof

$\Align{
u_j = W(u_1, \dots, u_{j-1}, u_{j+1}, \dots, u_m) \\
(\grad u_j)_i = \sum_{k\neq j}{\pdv{u_k}{W} \pdv{x_i}{u_k}} \\
\grad u_j = \sum_{k \neq j}{\pdv{u_k}{W} \grad u_k}
}$

# Claim 2.

Если хотя бы в одной точке нет лин. зав. градиентов, то ф-ии функц. независимы.

# Пример 2

![4.jpg](assets/imgs/09-04-25_12-02-23_993_IMG_20250409_115504.jpg)

# Theorem 2. О выпрямлении траектории.

## Let:

АСОДУ: $\dot{x} = f(x)$
$b \in \RR^n: f(b) \neq 0$ (b - не ПР)

## Then:

В некоторой окр. т. b сущ. гладкая невырожденная замена переменных, т.ч.
$\Cases{
\dot{{y}_{k}} = 0, & k \in [1,n-1] \\
\dot{{y}_{n}} = 1
}$

## Proof:

![6.jpg](assets/imgs/09-04-25_12-25-11_908_IMG_20250409_120642.jpg)
![7.jpg](assets/imgs/09-04-25_12-25-11_707_IMG_20250409_120645.jpg)
![8.jpg](assets/imgs/09-04-25_12-25-11_174_IMG_20250409_121539.jpg)
