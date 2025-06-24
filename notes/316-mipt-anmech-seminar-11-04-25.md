---
id: 316-mipt-anmech-seminar-11-04-25
aliases:
  - MIPT anmech seminar 11-04-25
tags: []
---

# MIPT anmech seminar 11-04-25

![1.jpg](assets/imgs/11-04-25_18-05-28_992_IMG_20250411_171637.jpg)
![2.jpg](assets/imgs/11-04-25_18-05-28_236_IMG_20250411_171904.jpg)
![3.jpg](assets/imgs/11-04-25_18-05-28_364_IMG_20250411_172046.jpg)
![7.jpg](assets/imgs/11-04-25_18-05-28_290_IMG_20250411_173524.jpg)
![8.jpg](assets/imgs/11-04-25_18-05-28_067_IMG_20250411_174032.jpg)

Ур-ия Лагранжа инвариантны относительно любого неособенного преобразования.

Ур-ия Гамильтона инвариантны только относительно канонического преобразования.

# Def. Неособенное преобразоание

$\Align{
q \to \tilde{q} \\
p \to \tilde{p} \\
\det M \neq 0 \\
M = \Pmatrix{
\Pmatrix{\pdv{q_k}{\tilde{q}_i}} & \Pmatrix{\pdv{p_k}{\tilde{q}_i}} \\
\Pmatrix{\pdv{q_k}{\tilde{p}_i}} & \Pmatrix{\pdv{p_k}{\tilde{p}_i}}
}
}$

# Def. Каноническое преобразоание

Неособенное преобразование, которое любую гамильтонову систему приводит к гамильтоновой.

# Theorem. Критерий каноничности.

Неособенное пр-ие является каноническим, если
$\exists c \neq 0$ - "валентность"
$\exists F$ - функционал - "производящая ф-ия"

$t \neq const$

$$
\sum{\tilde{p}_i \d \tilde{q}_i - \tilde{H} \d t - c \group{\sum{p_i \d q_i - H \d t}}} = - \d F
$$

$t = const$

$$
\sum{\tilde{p}_i \delta \tilde{q}_i - c \sum{p_i \delta q_i}} = - \delta F
$$

# 23.7

![4.jpg](assets/imgs/11-04-25_18-05-28_238_IMG_20250411_172529.jpg)
![5.jpg](assets/imgs/11-04-25_18-05-28_119_IMG_20250411_172854.jpg)
![6.jpg](assets/imgs/11-04-25_18-05-28_442_IMG_20250411_173213.jpg)

# Следствие из критерия.

Пусть преобразование каноническое.
$c \neq 0, F$
Тогда обратное преобразование тоже каноническое.
$\tilde{c} = \frac{1}{c}, \tilde{F} = -\frac{F}{c}$

# Свободные канонические преобразования

$$
\Gather{
q,p \to q, \tilde{q}\\
\det \Pmatrix{\pdv{p_k}{\tilde{q}_i}} \neq 0
}
$$

## Критерий каноничности

$$
\Cases{
\pdv{q_i}{F} = c p_i(t,q,\tilde{q}) \\
\pdv{\tilde{q}_i}{F} = -\tilde{p}_i(t,q,\tilde{q}) \\
}
$$

$$
c\ \pDv{\tilde{q}_i}{p_i(t,q,\tilde{q})} = \pDv{q_i}{\tilde{p}_i(t,q,\tilde{q})}
$$

![9.jpg](assets/imgs/11-04-25_18-05-28_367_IMG_20250411_174217.jpg)
![10.jpg](assets/imgs/11-04-25_18-05-28_661_IMG_20250411_174348.jpg)

# Полусвободные канонические преобразования

$$
\Gather{
q,p \to q, \tilde{p}\\
\det \Pmatrix{\pdv{p_k}{\tilde{p}_i}} \neq 0
}
$$

## Критерий каноничности

$$
\Cases{
\pdv{q_i}{F} = c p_i(t,q,\tilde{p}) \\
\pdv{\tilde{p}_i}{F} = \tilde{q}_i(t,q,\tilde{p}) \\
}
$$

$$
c\ \pDv{\tilde{p}_i}{p_i(t,q,\tilde{p})} = \pDv{q_i}{\tilde{q}_i(t,q,\tilde{q})}
$$

![11.jpg](assets/imgs/11-04-25_18-05-28_847_IMG_20250411_175318.jpg)
![12.jpg](assets/imgs/11-04-25_18-05-28_495_IMG_20250411_175547.jpg)
![13.jpg](assets/imgs/11-04-25_18-05-28_932_IMG_20250411_175907.jpg)

# 23.98

![14.jpg](assets/imgs/11-04-25_18-16-59_725_IMG_20250411_180746.jpg)
![15.jpg](assets/imgs/11-04-25_18-16-59_402_IMG_20250411_180855.jpg)
![16.jpg](assets/imgs/11-04-25_18-16-59_666_IMG_20250411_180900.jpg)
![17.jpg](assets/imgs/11-04-25_18-16-59_584_IMG_20250411_181350.jpg)
