---
id: 896-mipt-field-theory-lecture-12-03-25
aliases:
  - MIPT field theory lecture 12-03-25
tags: []
---

# MIPT field theory lecture 12-03-25

> Сегодня мало кто выжил...

# 4-вектор

![1.jpg](assets/imgs/12-03-25_10-44-29_424_IMG_20250312_090626.jpg)
![2.jpg](assets/imgs/12-03-25_10-44-29_112_IMG_20250312_090640.jpg)
![3.jpg](assets/imgs/12-03-25_10-44-29_786_IMG_20250312_090714.jpg)
![4.jpg](assets/imgs/12-03-25_10-44-29_791_IMG_20250312_090848.jpg)

# 4-ускорение

![7.jpg](assets/imgs/12-03-25_10-44-29_700_IMG_20250312_091304.jpg)

# Принцып наименьшего действия

# Симметрии законов преобразования

# Def. Действие

![12.jpg](assets/imgs/12-03-25_10-44-29_326_IMG_20250312_092218.jpg)

$$
\Gather{
S - \textit{функционал от траектории}\ x(t) \\
S: x(t) \to \RR
}
$$

Пусть $\exists L$, такой что:

$$
S = \int_{t_1}^{t_2}{L(x,\dot{x},t) \d t}
$$

$L$ - лагранжиан.

![11.jpg](assets/imgs/12-03-25_10-44-29_249_IMG_20250312_092005.jpg)

# Принцып Гамильтона (наименьшего действия)

На действительной траектории $S$ локально минимальна.

# Теорема Нётера

$S$ инвариантно относительно некоторого преобразования
$\implies$
имеется некоторый интеграл движения

# Уравнения Лагранжа

![14.jpg](assets/imgs/12-03-25_10-44-29_959_IMG_20250312_093023.jpg)

$$
\AlignLeft{
x(t) = x_0(t) + \delta x(t) - \textit{вариация} \\
\delta x(t_1) = \delta x(t_2) = 0 \\
\delta S = \int_{t_1}^{t_2}{\group{\pdv{x}{L} \delta x + \pdv{\dot{x}}{L} \delta \dot{x}} \d t} =
\pdv{\dot{x}}{L} \delta x \rvert_{t_1}^{t_2} +
\int_{t_1}^{t_2}{\group{\pdv{x}{L} - \Dv{t}{\pdv{\dot{x}}{L}}} \delta x \d t} = \\
= \int_{t_1}^{t_2}{\group{\pdv{x}{L} - \Dv{t}{\pdv{\dot{x}}{L}}} \delta x \d t} \\
\pdv{\dot{x}}{L} \delta x \rvert_{t_1}^{t_2} = 0 \\
}
$$

# Преобразование траектории и однородность пространства.

## 1 (ЗСИ)

`Пусть:`

$$
\AlignLeft{
x(t) \to x(t) + \varepsilon \\
S - inv
}
$$

`Тогда:`

$$
\AlignLeft{
0 = \delta S =
\int_{t_1}^{t_2}{\group{\pdv{x}{L} \delta x + \pdv{\dot{x}}{L} \delta \dot{x}} \d t} \\
\delta x = \varepsilon,\quad \delta \dot{x} = 0 \\
\Dv{t}{\pdv{\dot{x}}{L}} = \pdv{x}{L} = 0 \\
p \defeq \pdv{\dot{x}}{L} - \textit{канонический импульс} \\
p = const - \textit{З.С.И.} \\
}
$$

![15.jpg](assets/imgs/12-03-25_10-44-29_532_IMG_20250312_093847.jpg)
![16.jpg](assets/imgs/12-03-25_10-44-29_390_IMG_20250312_093850.jpg)
![17.jpg](assets/imgs/12-03-25_10-44-29_946_IMG_20250312_093856.jpg)

## 2 (ЗСЭ)

`Пусть:`

$$
\AlignLeft{
t \to t + \varepsilon \\
x(t) \to x(t - \varepsilon) \\
S - inv
}
$$

`Тогда:`

$$
\AlignLeft{
0 = \delta S =
\int_{t_1}^{t_2}{L(x(t - \varepsilon),\dot{x}(t - \varepsilon),t - \varepsilon)) \d t} -
\int_{t_1}^{t_2}{L(x(t), \dot{x}(t), t)) \d t}
= \\
= \int_{t_1}^{t_2}{\group{-
\pdv{x}{L} \dot{x}_\varepsilon -
\pdv{\dot{x}}{L} \ddot{x}_\varepsilon -
\pdv{t}{L} \varepsilon
} \d t} +
\varepsilon L \rvert_{t_1}^{t_2}
\\
\textit{Здесь произошло что-то страшное } 🙃 \dots
\\
H \defeq L - p \dot{x} - \textit{гамильтониан} \\
H(x, \dot{x}, t) = E - \textit{энергия} \\
H = const - \textit{З.С.Э.}
}
$$

![18.jpg](assets/imgs/12-03-25_10-44-29_487_IMG_20250312_094905.jpg)
![19.jpg](assets/imgs/12-03-25_10-44-29_384_IMG_20250312_095014.jpg)
![20.jpg](assets/imgs/12-03-25_10-44-29_700_IMG_20250312_095146.jpg)
![21.jpg](assets/imgs/12-03-25_10-44-29_617_IMG_20250312_095451.jpg)
![22.jpg](assets/imgs/12-03-25_10-44-29_812_IMG_20250312_095452.jpg)
![23.jpg](assets/imgs/12-03-25_10-44-29_069_IMG_20250312_095508.jpg)

## 3 (ЗС момента импульса - ЗСМИ)

![26.jpg](assets/imgs/12-03-25_10-44-29_744_IMG_20250312_100016.jpg)

На семинаре:

![12-03-25_12-33-39_769.png](assets/imgs/12-03-25_12-33-39_769.png)
![12-03-25_12-33-58_694.png](assets/imgs/12-03-25_12-33-58_694.png)
![12-03-25_12-34-06_070.png](assets/imgs/12-03-25_12-34-06_070.png)

# Преобразование Лежандра

![27.jpg](assets/imgs/12-03-25_10-44-29_579_IMG_20250312_100547.jpg)
![29.jpg](assets/imgs/12-03-25_10-44-29_973_IMG_20250312_100729.jpg)

Типа замена переменных.

$$
\AlignLeft{
\d U = T \d S - p \d V = \pdv{S}{U} \d S + \pdv{V}{U} \d V \\
\implies U(S,V) \\
F \defeq U - TS - \textit{свободная энергия} \\
\d F = -S \d T - p \d V \\
\implies F(T,V) \\
}
$$

# Уравнения Гамильтона

$$
\Cases{
\dot{x} = \pdv{p}{H} \\
\dot{p} = -\pdv{x}{H}
}
$$

![30.jpg](assets/imgs/12-03-25_10-44-29_121_IMG_20250312_101041.jpg)

# Принцып относительности и действие

![31.jpg](assets/imgs/12-03-25_10-44-29_752_IMG_20250312_101435.jpg)

# Пример 1

![34.jpg](assets/imgs/12-03-25_10-44-29_184_IMG_20250312_102218.jpg)
![33.jpg](assets/imgs/12-03-25_10-44-29_923_IMG_20250312_102204.jpg)

Свободная частица.
Найдем действие.

$$
\AlignLeft{
S = \int_{t_1}^{t_2}{L(x,\dot{x},t) \d t}\\
\textit{ЗСИ} \implies \pdv{x}{L} = 0 \\
\textit{ЗСЭ} \implies \pdv{t}{L} = 0 \\
\implies \\
L = L(\dot{x}) \\
L = L(\abs{\dot{x}}) \\
L = \frac{c}{2} \abs{\dot{x}}^2 \\
\textit{Ур-ия лагранжа} \implies c \ddot{x} = 0 \implies c = m \\
L - \textit{кинетическая энергия} \\
}
$$

# Пример 2

![35.jpg](assets/imgs/12-03-25_10-44-29_252_IMG_20250312_102452.jpg)
![37.jpg](assets/imgs/12-03-25_10-44-29_222_IMG_20250312_102808.jpg)
![38.jpg](assets/imgs/12-03-25_10-44-29_897_IMG_20250312_102809.jpg)

Частица в потенциальном поле.

$$
\AlignLeft{
L = \frac{m}{2} {\dot{x}}^{2} - V(x) \\
m \ddot{x} = F = -\pdv{x}{V} \\
p = \pdv{\dot{x}}{L} = m \dot{x} \\
H = p \dot{x} - L = m \dot{x}^2 - \frac{m}{2} {\dot{x}}^{2} + V(x) =
\frac{p^2}{2m} + V(x) \\
}
$$
