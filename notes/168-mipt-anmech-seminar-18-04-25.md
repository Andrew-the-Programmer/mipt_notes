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

![1.jpg](assets/imgs/18-04-25_18-39-45_936_IMG_20250418_171546.jpg)
![2.jpg](assets/imgs/18-04-25_18-39-45_337_IMG_20250418_171555.jpg)
![3.jpg](assets/imgs/18-04-25_18-39-45_231_IMG_20250418_171725.jpg)

# Полный интеграл

это решение ур-ия Гамильтона-Якоби $S(t,q_i,\alpha_i)$:

$$
\Cases{
\pdv{t}{S} + H(t,q,\pdv{q}{S}) = 0 \\
\det \matrix{\frac{\partial^2 S}{\partial q_i \partial \alpha_j}} \neq 0
}
$$

![4.jpg](assets/imgs/18-04-25_18-39-45_243_IMG_20250418_172101.jpg)

# Дежурные полные интегралы

## Главная ф-ия Гамильтона

$q^0 \equiv \alpha$

$$
W(t,q^0,p^0) = \int_{t_0}^t{L(s, q(s,q^0,p^0), \dot{q}(s,q^0,p^0))\d s}
$$

$p^0 = p^0(t,q,q^0)$

![5.jpg](assets/imgs/18-04-25_18-39-45_729_IMG_20250418_172105.jpg)

## Полуглавная ф-ия Гамильтона

$p^0 \equiv \alpha$

$$
V(t,q,p^0) = W(t, q^0(t,q,p^0), p^0) + \sum_{i=1}^{n}{p_i^0 q_i^0(t,q,p^0)}
$$

# Метод разделения переменных

![7.jpg](assets/imgs/18-04-25_18-39-45_909_IMG_20250418_172432.jpg)

$$
S(t,q,\alpha) = S_0(t,\alpha) + \sum_{i=1}^{n}{S_i(q_i, \alpha)}
$$

$$
S_i = \int{p_i(q_i, \alpha) \d q_i}
$$

![6.jpg](assets/imgs/18-04-25_18-39-45_505_IMG_20250418_172226.jpg)

## 1. Обобщенно-консервативные системы

$$
\dv{t}{H} = 0 \implies H = h = const
$$

$$
S_0 = -h(\alpha) \cdot t
$$

![8.jpg](assets/imgs/18-04-25_18-39-45_470_IMG_20250418_172735.jpg)

## 2.

$$
H = f(t) \cdot g(q)
$$

$$
S_0 = -h \int{f(t) \d t}, \quad h = g(q)
$$

![9.jpg](assets/imgs/18-04-25_18-39-45_865_IMG_20250418_172938.jpg)

## 3.

$$
H = H(f_1(q_1, p_1), \dots, f_n(q_n, p_n))
$$

$$
\Gather{
\alpha_i = f_i(q_i, p_i) = const - \textit{ПИ} \\
p_i = p_i(q_i, \alpha_i)
}
$$

![10.jpg](assets/imgs/18-04-25_18-39-45_351_IMG_20250418_173206.jpg)

# Примеры

# Анизотропный осциллятор

![11.jpg](assets/imgs/18-04-25_18-39-45_980_IMG_20250418_173359.jpg)
![12.jpg](assets/imgs/18-04-25_18-39-45_339_IMG_20250418_173630.jpg)

# Матрешка

![13.jpg](assets/imgs/18-04-25_18-39-45_747_IMG_20250418_173833.jpg)

# Движение Кеплера в поле тяжести

![14.jpg](assets/imgs/18-04-25_18-39-45_246_IMG_20250418_174130.jpg)
![15.jpg](assets/imgs/18-04-25_18-39-45_320_IMG_20250418_174304.jpg)
![16.jpg](assets/imgs/18-04-25_18-39-45_608_IMG_20250418_175249.jpg)
![17.jpg](assets/imgs/18-04-25_18-39-45_012_IMG_20250418_175502.jpg)
![18.jpg](assets/imgs/18-04-25_18-39-45_805_IMG_20250418_175725.jpg)

# "Смякалка, как говорят в простонародии".

![19.jpg](assets/imgs/18-04-25_18-39-45_308_IMG_20250418_175816.jpg)

# 24.44

![20.jpg](assets/imgs/18-04-25_18-39-45_454_IMG_20250418_180118.jpg)
![21.jpg](assets/imgs/18-04-25_18-39-45_311_IMG_20250418_180329.jpg)
![22.jpg](assets/imgs/18-04-25_18-39-45_392_IMG_20250418_180815.jpg)
![23.jpg](assets/imgs/18-04-25_18-39-45_379_IMG_20250418_180923.jpg)
