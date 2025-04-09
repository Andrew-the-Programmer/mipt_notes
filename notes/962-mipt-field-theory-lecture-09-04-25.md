---
id: 962-mipt-field-theory-lecture-09-04-25
aliases:
  - MIPT field theory lecture 09-04-25
tags: []
---

# MIPT field theory lecture 09-04-25

Конспект получился хороший, поэтому фотографии в одном месте.

# Photos

![1.jpg](assets/imgs/09-04-25_10-45-35_830_IMG_20250409_090816.jpg)
![5.jpg](assets/imgs/09-04-25_10-45-35_916_IMG_20250409_090958.jpg)
![6.jpg](assets/imgs/09-04-25_10-45-35_730_IMG_20250409_091124.jpg)
![7.jpg](assets/imgs/09-04-25_10-45-35_458_IMG_20250409_091350.jpg)
![8.jpg](assets/imgs/09-04-25_10-45-35_704_IMG_20250409_091354.jpg)
![9.jpg](assets/imgs/09-04-25_10-45-36_635_IMG_20250409_092415.jpg)
![10.jpg](assets/imgs/09-04-25_10-45-36_765_IMG_20250409_092429.jpg)
![11.jpg](assets/imgs/09-04-25_10-45-36_115_IMG_20250409_092446.jpg)
![13.jpg](assets/imgs/09-04-25_10-45-36_733_IMG_20250409_092731.jpg)
![14.jpg](assets/imgs/09-04-25_10-45-36_869_IMG_20250409_092936.jpg)
![15.jpg](assets/imgs/09-04-25_10-45-36_116_IMG_20250409_093931.jpg)
![16.jpg](assets/imgs/09-04-25_10-45-36_109_IMG_20250409_093937.jpg)
![17.jpg](assets/imgs/09-04-25_10-45-36_072_IMG_20250409_094439.jpg)
![18.jpg](assets/imgs/09-04-25_10-45-36_111_IMG_20250409_094909.jpg)
![19.jpg](assets/imgs/09-04-25_10-45-36_155_IMG_20250409_095423.jpg)
![21.jpg](assets/imgs/09-04-25_10-45-36_270_IMG_20250409_095539.jpg)
![22.jpg](assets/imgs/09-04-25_10-45-36_133_IMG_20250409_100401.jpg)
![23.jpg](assets/imgs/09-04-25_10-45-36_075_IMG_20250409_100802.jpg)
![25.jpg](assets/imgs/09-04-25_10-45-36_699_IMG_20250409_101834.jpg)
![26.jpg](assets/imgs/09-04-25_10-45-36_296_IMG_20250409_101839.jpg)
![27.jpg](assets/imgs/09-04-25_10-45-36_369_IMG_20250409_102032.jpg)

# Электромагнитное поле как механическая система со связями.

$$
\textit{Ур-ия Максвелла} - \Cases{
\left.
\Array{l}{
\divv B = 0 \\
\divv E = 4\pi \rho
}
\right\} - \textit{ур-ия связи}\\
\left.
\Array{l}{
\rot E = -\frac{1}{c} \pdv{t}{B} \\
\rot B = \frac{4\pi}{c} j - \frac{1}{c} \pdv{t}{E}
}
\right\} - \textit{динамические ур-ия}
}
$$

6 неизвестных - 2 связи = 4 ур-ия.

# Потенциалы

Векторный потенциал.

$$
B = \rot A
$$

$$
E = -\grad \varphi - \frac{1}{c} \pdv{t}{A}
$$

# Калибровочное преобразование.

(остовляет инвариантными E и B)

$$
{A}^{'} = A + \grad f
$$

$$
{\varphi}^{'} = \varphi + \frac{1}{c} \pdv{t}{f}
$$

# Ур-ия Максвелла для потенциалов.

$
\Align{
\divv E = 4\pi \rho \implies \\
-\Laplace \varphi - \frac{1}{c} \pdv{t}{} \divv A = 4\pi\rho \implies \\
\frac{1}{c^2} \pdv[2]{t}{\varphi} - \Laplace \varphi -\frac{1}{c} 
\pdv{t}{} \group{\frac{1}{c} \pdv{t}{\varphi} + \divv A} = 
4\pi\rho c \\
\rot B = \frac{4\pi}{c} j + \frac{1}{c} \pdv{t}{E} \implies \\
\frac{1}{c^2} \pdv[2]{t}{A} - \Laplace A - \frac{1}{c} 
\grad \group{\frac{1}{c} \pdv{t}{\varphi} + \divv A} = 
\frac{4\pi}{c} j \\
\Cases{
\frac{1}{c^2} \pdv[2]{t}{\varphi} - \Laplace \varphi -
\frac{1}{c} \pdv{t}{} &\group{\frac{1}{c} \pdv{t}{\varphi} + \divv A} = 
4\pi (\rho c) \\
\frac{1}{c^2} \pdv[2]{t}{A} - \Laplace A +
\grad &\group{\frac{1}{c} \pdv{t}{\varphi} + \divv A} = 
\frac{4\pi}{c} j \\
} \\
}
$

[[868-оператор-Д'Аламбера|оператор Д'Аламбера]]

$
\Align{
j^\mu = \Pmatrix{
pc \\
\vec{j}
} \\
\DAlambert = \frac{1}{c^2} \pdv[2]{t}{} - \Laplace
}
$

# 4-потенциал.

$$
A^\mu \defeq \Pmatrix{
\varphi \\
\vec{A}
}
$$

$\partial_\mu A^\mu = \frac{1}{c} \pdv{t}{\varphi} + \divv A$

# Ур-ия Максвелла для 4-потенциала.

(ковариантная форма)

$$
\DAlambert A^\nu - \partial^\nu (\partial_\mu A^\mu) = \frac{4\pi}{c} j^\nu
$$

$$
\partial_\mu \group{\partial^\mu A^\nu - \partial^\nu A^\mu} =\frac{4\pi}{c} j^\nu
$$

# Тензор электромагнитного поля.

$$
F^{\mu\nu} \defeq \partial^\mu A^\nu - \partial^\nu A^\mu
$$

$$
\partial_\mu F^{\mu\nu} = \frac{4\pi}{c} j^\nu
$$

# Свойства $F^{\mu\nu}$

1.  $$
    F^{\mu\nu} = -F^{\nu\mu}
    $$
2.  6 независимых компонент.
3.  $$
    \Gather{
    F^{0i} = -E_i \\
    F^{ij} = - e^{ijk} B^k
    }
    $$

$$
F^{\mu\nu} = \Pmatrix{
0 & -E_1 & -E_2 & -E_3 \\
E_1 & 0 & -B_3 & B_2 \\
E_2 & B_3 & 0 & -B_1 \\
E_3 & -B_2 & B_1 & 0
}
$$

4. Калибровачная инвариантность.
   $$
   ({A}^{'})^{\mu} = A^\mu + \partial^\mu f
   $$

# 1-ая пара ур-ий Максвелла в ковариантной форме и дуальный тензор.

$
\Align{
\Cases{
\divv E = 4\pi \rho \\
\rot B = \frac{4\pi}{c} j + \frac{1}{c} \pdv{t}{E} \\
} \to 
\left\{
\Array{l}{
\rho = j = 0 \\
E = B \\
B = -E
}
\right\} \to 
\Cases{
\divv B = 0 \\
\rot E = -\frac{1}{c} \pdv{t}{B}
}
}
$

# Дуальный тензор $F^{\mu\nu}$

$$
\tilde{F}_{\mu\nu} = \frac{1}{2!} e_{\mu\nu\rho\sigma} F^{\rho\sigma}
$$

$$
\tilde{F}^{\mu\nu} = \eta^{\mu\rho} \eta^{\nu\sigma} \tilde{F}_{\rho\sigma} = \Pmatrix{
0 & -B_1 & -B_2 & -B_3 \\
B_1 & 0 & E_3 & -E_2 \\
B_2 & -E_3 & 0 & E_1 \\
B_3 & E_2 & -E_1 & 0
}
$$

# Преобразования Лоренца для ЭМ полей

$\Align{
({F}^{'})^{\mu\nu} = \Lambda_\rho^\mu \Lambda_\sigma^\nu F^{\rho\sigma} \\
\textit{Муторные вычисления, которых на лекции не было}\dots \\
\implies
}$
(относительно направления $\vec{v}$)

$$
\Align{
E^{'}_{\parallel} = E_{\parallel} \\
E^{'}_{\perp} = \gamma \group{E_{\perp} + \frac{1}{c} \vecprod{v}{B}} \\
B^{'}_{\parallel} = B_{\parallel} \\
B^{'}_{\perp} = \gamma \group{B_{\perp} - \frac{1}{c} \vecprod{v}{E}} \\
}
$$

# Инварианты ЭМ поля

Линейная комбинация инвариантов: $F^{\mu\nu}, A^\mu, \tilde{F}^{\mu\nu}$.

1. $$
   F^{\mu\nu} F_{\mu\nu} = 2 (B^2 - E^2)
   $$
2. $$
   \tilde{F}^{\mu\nu} F_{\mu\nu} = 4 \veccross{E}{B}
   $$

3. $$
   A_\mu A^\mu = \varphi^2 - A^2
   $$

Обычно, когда говорят об инвариантах эм поля, имеют в виду (1) и (2), которые также являются инвариантами отн. калибровки.

# Пример 1 - ЭМ поля равномерно движущегося заряда.

![24.jpg](assets/imgs/09-04-25_10-45-36_932_IMG_20250409_101201.jpg)

$\Align{
{K}^{'}: \\
{E}^{'} = e \frac{\vec{{x}^{'}}}{\abs{{x}^{'}}^3} \\
K: \\
E = E_\perp + E_\parallel = 
{{E}^{'}}_{\parallel} + \gamma \group{{{E}^{'}}_{\perp} - \frac{1}{c} \vecprod{v}{{B}^{'}}} \\
B = B_\perp + B_\parallel =
{{B}^{'}}_{\parallel} + \gamma \group{{{B}^{'}}_{\perp} + \frac{1}{c} \vecprod{v}{{E}^{'}}} \\
{B}^{'} = 0 \\
E = {{E}^{'}}_{\parallel} + \gamma {{E}^{'}}_{\perp} \\
B = \frac{\gamma}{c} \vecprod{v}{{E}^{'}} = \frac{1}{c} \vecprod{v}{E} \\
E = \frac{e \gamma}{(\gamma^2(x - vt)^2 + y^2 + z^2)^{3 / 2}} \Pmatrix{
x - v t \\
y \\
z
} = \textit{в полярных координатах} = \\
= \frac{\vec{x}}{\abs{x}^3} \frac{e}{\gamma^2 \group{1 - \frac{v^2}{c^2} \sin^2{\theta}}^{3 / 2}}
}$

Силовые линиии как-бы сгущаются.

![28.jpg](assets/imgs/09-04-25_10-45-36_166_IMG_20250409_102611.jpg)
![29.jpg](assets/imgs/09-04-25_10-45-36_475_IMG_20250409_102750.jpg)
