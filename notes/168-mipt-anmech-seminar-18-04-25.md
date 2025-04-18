---
id: 168-mipt-anmech-seminar-18-04-25
aliases:
  - MIPT anmech seminar 18-04-25
tags: []
---

# MIPT anmech seminar 18-04-25

# Уравнение Гамильтона-Якоби

Свободные канонические преобразования.

$$
\Cases{
\pdv{q_i}{S} = c p_i \\
\pdv{\tilde{q_i}}{S} = -\tilde{p_i} \\
\tilde{H} = \pdv{t}{S} + c H
}
$$

$\tilde{H} = 0,\quad c = 1 \implies$
Уравнение Гамильтона-Якоби:

$$
\pdv{t}{S} + H(t,q,\pdv{q}{S}) = 0
$$

$\Align{
\Cases{
\dot{\tilde{q_i}} = \pdv{\tilde{p_i}}{\tilde{H}} = 0 \\
\dot{\tilde{p_i}} = \pdv{\tilde{q_i}}{\tilde{H}} = 0
} \\
\Cases{
\tilde{q_i} = \alpha_i = const \\
\tilde{p_i} = \beta_i = const
} \\
}$

Уравнения движения

$$
\Cases{
\pdv{q_i}{S} = p_i \\
\pdv{\alpha_i}{S} = -\beta_i
}
$$

# Полный интеграл

это решение ур-ия Гамильтона-Якоби $S(t,q_i,\alpha_i)$:

$$
\Cases{
\pdv{t}{S} + H(t,q,\pdv{q}{S}) = 0 \\
\det \matrix{\frac{\partial^2 S}{\partial q_i \partial \alpha_j}} \neq 0
}
$$

# Дежурные полные интегралы

## Главная ф-ия Гамильтона

$q^0 \equiv \alpha$

$$
W(t,q^0,p^0) = \int_{t_0}^t{L(s, q(s,q^0,p^0), \dot{q}(s,q^0,p^0))\d s}
$$

$p^0 = p^0(t,q,q^0)$

## Полуглавная ф-ия Гамильтона

$p^0 \equiv \alpha$

$$
V(t,q,p^0) = W(t, q^0(t,q,p^0), p^0) + \sum_{i=1}^{n}{p_i^0 q_i^0(t,q,p^0)}
$$

# Метод разделения переменных

$$
S(t,q,\alpha) = S_0(t,\alpha) + \sum_{i=1}^{n}{S_i(q_i, \alpha)}
$$

$$
S_i = \int{p_i(q_i, \alpha) \d q_i}
$$

## 1. Обобщенно-консервативные системы

$$
\dv{t}{H} = 0 \implies H = h = const
$$

$$
S_0 = -h(\alpha) \cdot t
$$

## 2.

$$
H = f(t) \cdot g(q)
$$

# Примеры

# Анизотропный осциллятор

# Матрешка

# Движение Кеплера в поле тяжести

# 24.44
