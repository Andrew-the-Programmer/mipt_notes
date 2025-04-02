---
id: 578-mipt-differential-equations-lecture-02-04-25
aliases:
  - MIPT differential equations lecture 02-04-25
tags: []
---

# MIPT differential equations lecture 02-04-25

![1.jpg](assets/imgs/02-04-25_11-37-41_834_IMG_20250402_104452.jpg)

Классификация ПР для ЛАСОДУ.
![26-03-25_15-46-21_828_26-03-25_15-46-21_352.png](assets/imgs/26-03-25_15-46-21_828_26-03-25_15-46-21_352.png)

# Простейшие случаи

# 1.

$$
\Gather{
\det A \neq 0 \\
\lambda_1 \cdot \lambda_2 \neq 0 \\
\lambda_1 \neq \lambda_2
}
$$

![2.jpg](assets/imgs/02-04-25_11-37-41_303_IMG_20250402_105932.jpg)

## 1.1. $\lambda_i \in \RR$

### 1.1.1. $\lambda_1 \cdot \lambda_2 > 0$

Узел

#### 1.1.1.1. $\lambda_i > 0$

![3.jpg](assets/imgs/02-04-25_11-37-41_139_IMG_20250402_105938.jpg)

#### 1.1.1.2. $\lambda_i < 0$

![4.jpg](assets/imgs/02-04-25_11-37-41_870_IMG_20250402_110619.jpg)

### 1.1.2. $\lambda_1 \cdot \lambda_2 < 0$

Седло

![51.jpg](assets/imgs/02-04-25_11-54-43_486_IMG_20250402_110619.jpg)
![5.jpg](assets/imgs/02-04-25_11-37-41_981_IMG_20250402_110851.jpg)

## 1.2. $\lambda_i \in \CC$

$\lambda_{1,2} = \alpha \pm i \beta$

### 1.2.1. $\alpha \neq 0$

Фокус
$
\AlignCenter{
\Cases{
\vec{{h}_{1}} = \vec{u} + i \vec{v}\\
\vec{{h}_{2}} = \vec{u} - i \vec{v}\\
}\\
(x,y) = e^{\alpha t} A \group{\vec{u} \cos\group{\gamma - \beta t} +
\vec{v} \sin\group{\gamma - \beta t}} \\
}
$

![6.jpg](assets/imgs/02-04-25_11-37-41_777_IMG_20250402_110854.jpg)
![7.jpg](assets/imgs/02-04-25_11-37-41_715_IMG_20250402_112754.jpg)
![8.jpg](assets/imgs/02-04-25_11-37-41_459_IMG_20250402_112756.jpg)
![9.jpg](assets/imgs/02-04-25_11-37-41_841_IMG_20250402_112758.jpg)

### 1.2.2. $\alpha = 0$

Центр

![10.jpg](assets/imgs/02-04-25_11-37-41_075_IMG_20250402_113553.jpg)

# Пример: 889

![02-04-25_12-20-15_801_IMG_20250402_114256.jpg](assets/imgs/02-04-25_12-20-15_801_IMG_20250402_114256.jpg)
![02-04-25_12-20-16_550_IMG_20250402_114259.jpg](assets/imgs/02-04-25_12-20-16_550_IMG_20250402_114259.jpg)

# 2. $\lambda_1 = \lambda_2$

## 2.1. Существует базис из собств. векторов

Дикритический узел

![02-04-25_12-20-16_710_IMG_20250402_114800.jpg](assets/imgs/02-04-25_12-20-16_710_IMG_20250402_114800.jpg)

## 2.2. Не существует базис из собств. векторов

Вырожденный узел

![02-04-25_12-20-17_762_IMG_20250402_120403.jpg](assets/imgs/02-04-25_12-20-17_762_IMG_20250402_120403.jpg)

# 3. $\det A = 0$

$$
\Gather{
\lambda_1 = 0 \\
\lambda_2 \in \RR
}
$$

## 3.1. $\lambda_2 < 0$

![02-04-25_12-20-17_904_IMG_20250402_120414.jpg](assets/imgs/02-04-25_12-20-17_904_IMG_20250402_120414.jpg)

## 3.2. $A = 0$

$$
\lambda_2 = 0
$$

![02-04-25_12-20-17_538_IMG_20250402_120900.jpg](assets/imgs/02-04-25_12-20-17_538_IMG_20250402_120900.jpg)

## 3.3. $A \neq 0$

![02-04-25_12-20-17_538_IMG_20250402_120900.jpg](assets/imgs/02-04-25_12-20-17_538_IMG_20250402_120900.jpg)
