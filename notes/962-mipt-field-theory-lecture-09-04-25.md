---
id: 962-mipt-field-theory-lecture-09-04-25
aliases:
  - MIPT field theory lecture 09-04-25
tags: []
---

# MIPT field theory lecture 09-04-25

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
4\pi\rho c \implies \\
\rot B = \frac{4\pi}{c} j + \frac{1}{c} \pdv{t}{E} \implies \\
\frac{1}{c^2} \pdv[2]{t}{A} - \Laplace A - \frac{1}{c} 
\grad \group{\frac{1}{c} \pdv{t}{\varphi} + \divv A} = 
\frac{4\pi}{c} j \\
\Cases{
\frac{1}{c^2} \pdv[2]{t}{\varphi} - \Laplace \varphi -\frac{1}{c} 
\pdv{t}{} \group{\frac{1}{c} \pdv{t}{\varphi} + \divv A} = 
4\pi (\rho c) \implies \\
\frac{1}{c^2} \pdv[2]{t}{A} - \Laplace A - \frac{1}{c} 
\grad \group{\frac{1}{c} \pdv{t}{\varphi} + \divv A} = 
\frac{4\pi}{c} j \\
}
}
$
