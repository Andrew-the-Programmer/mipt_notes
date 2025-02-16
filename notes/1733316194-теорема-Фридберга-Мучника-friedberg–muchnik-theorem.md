---
id: 1733316194-теорема-Фридеберга-Мучника-friedberg–muchnik-theorem
aliases:
  - теорема Фридеберга-Мучника
  - Friedberg–Muchnik theorem
tags: []
---
# Friedberg–Muchnik theorem

$$
\exists X, Y \in \mcR\mcE : X \not\le^T Y \land Y \not\le^T X
$$

$\Gamma$ упорядочен.
$\Gamma^*$ упорядочен [[1733316734-shortlex-order|shortlex]].
FM - МТ, перечислитель для X и Y.
FM имеет 3 доп. ленты.

1. словарь X
2. словарь Y

Слова красного или синего слова.
Изначально слова красные.
Если слово в X / Y, слово становится синим.

3. $\left(M_j^{\cdot}, m_j, z_j, n_j\right)$
   $M_j^{\cdot}$ - МТ.
   $m_j \in \set{X, Y}$ - метка.
   $m_j = \Cases{X, & j =^2 1 \\ Y, & j =^2 0}$
   $z_j \in \Gamma^*$
   $n_j \in \NN \lor \square$

$z_1 = \varepsilon$
$n_1 = 1$

Моделируем работу $M_j^{\cdot}$ на $z_j$ $n_j$ шагов.
При запросе оракула:
Ищем слово в словаре $\ol{m_j}$.

1. слово есть $\to$ ответ да.
2. слова нет $\to$ ответ нет.
   $M_j^{(\cdot)}$ может остановиться или не остановится.
3. Не остановилась: $n_{j} += 1$.
4. Остановилась:
   1. $n_j = \square$
   2. Принала:
