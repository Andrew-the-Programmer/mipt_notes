---
id: 896-mipt-field-theory-lecture-12-03-25
aliases:
  - MIPT field theory lecture 12-03-25
tags: []
---

# MIPT field theory lecture 12-03-25

> Сегодня мало кто выжил...

4-вектор
4-ускорение

# Принцып наименьшего действия

# Симметрии законов преобразования

# Def. Действие

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

# Принцып Гамильтона (наименьшего действия)

На действительной траектории $S$ локально минимальна.

# Теорема Нётера

$S$ инвариантно относительно некоторого преобразования
$\implies$
имеется некоторый интеграл движения

# Уравнения Лагранжа

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

## 3 (ЗС момента импульса - ЗСМИ)

# Преобразование Лежандра

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

# Принцып относительности и действие

# Пример 1

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
Частица в потенциальном поле.
$$
\AlignLeft{
L = \frac{m}{2} {\dot{x}}^{2} - V(x) \\
m \ddot{x} = F = -\pdv{x}{V} \\
p = \pdv{\dot{x}}{L} = m \dot{x} \\
H = p \dot{x} - L = m \dot{x}^2 - m {\dot{x}}^{2} + V(x) = 
\frac{p^2}{2m} + V(x) \\
}
$$
