---
id: 454-mipt-differential-equations-seminar-07-05-25
aliases:
  - MIPT differential equations seminar 07-05-25
tags: []
---

# MIPT differential equations seminar 07-05-25

Подготовка

# 6.35

МВП - метод введения переменной

![1.jpg](assets/imgs/07-05-25_16-02-25_518_IMG_20250507_155109.jpg)
![2.jpg](assets/imgs/07-05-25_16-02-25_913_IMG_20250507_155601.jpg)
![3.jpg](assets/imgs/07-05-25_16-02-25_433_IMG_20250507_155606.jpg)
![4.jpg](assets/imgs/07-05-25_16-02-25_299_IMG_20250507_160015.jpg)

# 7.56

![5.jpg](assets/imgs/07-05-25_16-40-38_632_IMG_20250507_162513.jpg)
![6.jpg](assets/imgs/07-05-25_16-40-38_030_IMG_20250507_162517.jpg)

МПП - метод понижения порядка

# 8.126

Линейное неоднородное уравнение

![7.jpg](assets/imgs/07-05-25_16-40-38_574_IMG_20250507_163031.jpg)
![8.jpg](assets/imgs/07-05-25_16-40-38_166_IMG_20250507_163036.jpg)
![9.jpg](assets/imgs/07-05-25_16-40-38_786_IMG_20250507_163812.jpg)
![10.jpg](assets/imgs/07-05-25_16-40-38_369_IMG_20250507_163915.jpg)

# 9.34

На формулу Лиувилля-Остроградского

$$
\Gather{
x^2 {y}^{''} + x (-2 + x \tg x) {y}^{'} (2 - x \tg x) y = x^3 e^x \cos x \\
a(x) {y}^{''} + b(x) {y}^{'} + c(x) y = f(x)
}
$$

- Находим решение однородного

  - Находим частное решение однородного - $y_1$
    В виде $x^\alpha, e^{\alpha x}, x^\beta P_k(x) e^{\alpha x}$

  - По формуле Лиувилля-Остроградского находим общее решение неоднородного - $y_2$

  $$
  y_2 = y_1 \cdot \int{\frac{c}{y_1^2} \exp{-\int{\frac{b(x)}{a(x)}}\d x}\d x} = C_1 f_1(x) + C_2 f_2(x)
  $$

- Находим $C_1$ и $C_2$
  $$
  \Cases{
  C_{1}^{'} f_1(x) + {C}_{2}^{'} f_2(x) = 0 \\
  C_{1}^{'} f_1^{'}(x) + {C}_{2}^{'} f_2^{'}(x) = \frac{f(x)}{a(x)} \\
  }
  $$

![11.jpg](assets/imgs/07-05-25_17-09-15_649_IMG_20250507_165213.jpg)
![12.jpg](assets/imgs/07-05-25_17-09-15_516_IMG_20250507_165219.jpg)
![13.jpg](assets/imgs/07-05-25_17-09-15_675_IMG_20250507_165232.jpg)
![14.jpg](assets/imgs/07-05-25_17-09-15_653_IMG_20250507_165545.jpg)

# 17.84

Уравнение в частных производных (ЧП)

![14-05-25_15-37-23_006.png](assets/imgs/14-05-25_15-37-23_006.png)
![14-05-25_15-37-04_262.png](assets/imgs/14-05-25_15-37-04_262.png)

$$
\Gather{
(x - 2 x^2 y) \pdv{x}{u} + y \pdv{y}{u} + 2 x^2 z^2 \pdv{z}{u} = 0 \\
u = y^2 z, \quad x - y = 0
}
$$

$\Align{
\Cases{
\dot{x} = x - 2x^2 y \\
\dot{y} = y \\
\dot{z} = 2x^2 z^2
} \\
\Cases{
x \neq 2 x^2 y \\
y \neq 0 \\
2 x^2 z^2 \neq 0
} \\
\frac{\d x}{x - 2 x^2 y} = \frac{\d y}{y} = \frac{\d z}{2 x^2 z^2} \\
\frac{\d x}{x (1 - 2 x y)} = \frac{\d (xy)}{2 xy (1 - xy)} = 
\group{\frac{1}{2xy} + \frac{1}{2 - 2xy}} \d (xy) \\
2 \ln\abs{y} = \ln\abs{xy} - \ln\abs{1 - xy} + c \\
u_1 = \frac{y}{x} - y^2 \\
\hline
x = 
}$
