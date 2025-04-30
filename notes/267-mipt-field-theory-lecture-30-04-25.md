---
id: 267-mipt-field-theory-lecture-30-04-25
aliases:
  - MIPT field theory lecture 30-04-25
tags: []
---

# MIPT field theory lecture 30-04-25

![8.jpg](assets/imgs/30-04-25_10-53-12_055_IMG_20250430_093916.jpg)
![9.jpg](assets/imgs/30-04-25_10-53-12_928_IMG_20250430_094614.jpg)
![10.jpg](assets/imgs/30-04-25_10-53-12_056_IMG_20250430_094941.jpg)
![12.jpg](assets/imgs/30-04-25_10-53-12_887_IMG_20250430_095652.jpg)
![13.jpg](assets/imgs/30-04-25_10-53-12_170_IMG_20250430_100452.jpg)
![14.jpg](assets/imgs/30-04-25_10-53-12_767_IMG_20250430_100456.jpg)
![16.jpg](assets/imgs/30-04-25_10-53-12_127_IMG_20250430_100901.jpg)
![17.jpg](assets/imgs/30-04-25_10-53-12_588_IMG_20250430_101532.jpg)
![18.jpg](assets/imgs/30-04-25_10-53-12_716_IMG_20250430_101535.jpg)
![19.jpg](assets/imgs/30-04-25_10-53-12_441_IMG_20250430_101816.jpg)
![20.jpg](assets/imgs/30-04-25_10-53-12_696_IMG_20250430_102024.jpg)
![21.jpg](assets/imgs/30-04-25_10-53-12_975_IMG_20250430_102520.jpg)
![22.jpg](assets/imgs/30-04-25_10-53-12_090_IMG_20250430_102710.jpg)
![23.jpg](assets/imgs/30-04-25_10-53-12_923_IMG_20250430_102808.jpg)
![24.jpg](assets/imgs/30-04-25_10-53-12_153_IMG_20250430_103102.jpg)

Опоздал на минут 20...

# Гамильтониан для ЭМ поля

# Калибровка Вейля

калибровочное условие
калибровачное преобразование
Общий вид:

$$
A_\mu^{'} = A_\mu + \partial_\mu f
$$

$$
\vec{{A}^{'}} = \vec{A} + \grad f
$$

![1.jpg](assets/imgs/30-04-25_09-39-36_361_IMG_20250430_092421.jpg)
![2.jpg](assets/imgs/30-04-25_09-39-36_972_IMG_20250430_092424.jpg)

# Гамильтон ЭМ поля в калибровке Вейля

## Канонический импульс

$$
\vec{\pi} = \pdv{\group{\pdv{t}{A}}}{\mcL}
$$

$$
\vec{\pi} = -\frac{\vec{E}}{2\pi c}
$$

![3.jpg](assets/imgs/30-04-25_09-39-36_108_IMG_20250430_092921.jpg)

## Гамильтониан

$$
\mcH = \veccrossv{\pi}{A} - \mcL
$$

$$
\mcH = \frac{E^2 + B^2}{8\pi} = T^{00}
$$

# Общее решение ур-ий Максвелла

$\Align{
\partial_\mu F^{\mu\nu} = \frac{4\pi}{c} j^\nu \\
\group{\partial^2 \eta_{\mu\nu} - \partial_\mu \partial_\nu} A^\mu = \frac{4\pi}{c} j^\mu \\
\dv{x}{f} \to \Matrix{
} \\
\textit{Рассмотрим оператор}:\ \partial^2 \eta_{\mu\nu} - \partial_\mu \partial_\nu \\
\textit{Он не обратим}
}$

# Калибровка Кулона $\divv{A} = 0$

$\Align{
\Cases{
-\Laplace \varphi = 4\pi \rho \\
\DAlambert A + \grad\group{\frac{1}{c} \pdv{t}{\varphi}} = \frac{4\pi}{c} j
}
}$

Электростатика ($\pdv{t}{A^\mu} = 0$)

$$
\Cases{
-\Laplace \varphi = 4\pi \rho \\
-\Laplace A = \frac{4\pi}{c} j
}
$$

Уравнение Пуассона

# Калибровка Лоренца $\partial_\mu A^\mu = 0$

Ковариантная калибровка

$$
\Cases{
\DAlambert \varphi = 4\pi \rho \\
\DAlambert A = \frac{4\pi}{c} j
}
$$

# Калибровка Вейля $\varphi = 0$

$$
\Cases{
-\Laplace \varphi - \frac{1}{c} \pdv{t}{} \group{\divv A} = 4\pi \rho \\
\DAlambert A + \grad \divv A = \frac{4\pi}{c} j
}
$$

# Калибровка излучения $\varphi = 0,\quad \divv A = 0$

нет токов и зарядов

Волновое уравнение

$$
\DAlambert A = 0
$$

# Метод преобразования Фурье

$$
\vec{A}(x,t) = \frac{1}{(2\pi)^3} \int_{\RR^3}{\vec{A}(\vec{k},t) e^{i \vec{k} \cdot \vec{x}} \d^3 k}
$$

Условие поперечности

$$
\vec{k} \perp \vec{A}(\vec{k}, t)
$$

Разложение по поляризациям

$$
A(x,t) = \frac{1}{(2\pi)^3} \int{\d^3 k}
$$
