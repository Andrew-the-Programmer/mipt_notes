---
id: 144-mipt-anmech-seminar-21-03-25
aliases:
  - MIPT anmech seminar 21-03-25
tags: []
---

# MIPT anmech seminar 21-03-25

# Гамильтонова механика

# Уравнения Гамильтона

![1.jpg](assets/imgs/21-03-25_17-52-34_955_IMG_20250321_171750.jpg)
![2.jpg](assets/imgs/21-03-25_17-52-34_278_IMG_20250321_171754.jpg)
![3.jpg](assets/imgs/21-03-25_17-52-34_080_IMG_20250321_171841.jpg)

обобщенный импульс

$$
p_i \defeq \pdv{\dot{{q}_{i}}}{L}
$$

гамильтониан

$$
H \defeq \sum\group{p_i \dot{{q}_{i}}} - L \vert_{\dot{{q}_{i}} = \psi_i(t,q,p)}
$$

$$
\Cases{
\dot{{q}_{i}} = \pdv{p_i}{H} \\
\dot{{p}_{i}} = -\pdv{q_i}{H}
}
$$

# Первый интеграл

![4.jpg](assets/imgs/21-03-25_17-52-34_105_IMG_20250321_172302.jpg)

$q(t), p(t)$ - решения уравнений Гамильтона
Функция $f(q,p,t)$, т.ч.

$$
\dv{t}{} f(q(t), p(t), t) = 0
$$

# Циклическая координата

![5.jpg](assets/imgs/21-03-25_17-52-34_864_IMG_20250321_172416.jpg)

Циклическая координата $q_i$:

$$
\pdv{q_i}{H} = 0
$$

$\implies p_i = const$

## Пример

![6.jpg](assets/imgs/21-03-25_17-52-34_507_IMG_20250321_172420.jpg)

# $H = E = T + \Pi$

![7.jpg](assets/imgs/21-03-25_17-52-34_473_IMG_20250321_172814.jpg)

натуральная система
склерономная связь
реономная связь

# 19.24

![8.jpg](assets/imgs/21-03-25_17-52-34_592_IMG_20250321_172929.jpg)
![9.jpg](assets/imgs/21-03-25_17-52-34_036_IMG_20250321_173055.jpg)
![11.jpg](assets/imgs/21-03-25_17-52-34_391_IMG_20250321_174242.jpg)

# Скобки Пуассона

![12.jpg](assets/imgs/21-03-25_17-52-34_026_IMG_20250321_174431.jpg)

$$
(\varphi, \psi) \defeq \sum_{i=1}^{n}\group{\pdv{q_i}{\varphi} \pdv{p_i}{\psi} - \pdv{p_i}{\varphi} \pdv{q_i}{\psi}}
$$

## Свойства

1. Антисимметричность
   $$
   (\varphi, \psi) = -(\psi, \varphi)
   $$
2. Линейность
   $$
   \group{\sum{\lambda_i \varphi_i}, \psi} = \sum{\lambda_i (\varphi_i, \psi)}
   $$
3. $$
   ((\psi, \varphi), f) + ((\varphi, f), \psi) + ((f, \psi), \varphi) = 0
   $$
4. $$
   \pdv{t}{(\varphi, \psi)} = \group{\pdv{t}{\varphi}, \psi} + \group{\varphi, \pdv{t}{\psi}}
   $$

# Критерий первого интеграла ур-ий Гамильтона

![14.jpg](assets/imgs/21-03-25_17-52-34_848_IMG_20250321_175123.jpg)

$$
\pdv{t}{f} + (f, H) = 0
$$

# Теорема Якоби-Пуассона

![15.jpg](assets/imgs/21-03-25_18-02-23_463_IMG_20250321_175248.jpg)

$$
f,g - ПИ \implies (f,g) - ПИ
$$

# Отделимая координата

![16.jpg](assets/imgs/21-03-25_18-02-23_138_IMG_20250321_175825.jpg)
![17.jpg](assets/imgs/21-03-25_18-02-23_207_IMG_20250321_175829.jpg)

# Ур-ия Гамильтона через скобки Пуассона

![18.jpg](assets/imgs/21-03-25_18-02-23_286_IMG_20250321_180017.jpg)

$$
\Cases{
\dot{{q}_{i}} = (q_i, H) \\
\dot{{p}_{i}} = (p_i, H)
}
$$

# 19.31

![22.jpg](assets/imgs/21-03-25_18-15-54_924_IMG_20250321_180713.jpg)
![20.jpg](assets/imgs/21-03-25_18-15-54_536_IMG_20250321_180354.jpg)
![21.jpg](assets/imgs/21-03-25_18-15-54_705_IMG_20250321_180704.jpg)
![23.jpg](assets/imgs/21-03-25_18-15-54_487_IMG_20250321_180947.jpg)
![24.jpg](assets/imgs/21-03-25_18-15-54_691_IMG_20250321_181423.jpg)
![25.jpg](assets/imgs/21-03-25_18-15-54_432_IMG_20250321_181430.jpg)
