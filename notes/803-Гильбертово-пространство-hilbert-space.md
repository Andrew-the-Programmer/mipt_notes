---
id: 803-Гильбертово-пространство-hilbert-space
aliases:
  - hilbert space
  - гильбертово пространство
tags: []
---

# Гильбертово пространство-Hilbert space
$\mcH$
1. [[879-евклидово-пространство|евклидово пространство]]
2. $(\cdot, \cdot): \mcH \times \mcH \to \RR$ - полная мера 

$$
\norm{x}^2 \defeq (x,x)
$$

# Properties
- $\mcH$ - [[416-банахово-пространство|банахово пространство]]

# [[282-базис-Шаудера|базис Шаудера]] (топологический Базис)
$$
\AlignLeft{
\set{e_n}_{n\in\NN} \\
\set{e_n}\ ортогоналeн\ (\veccross{e_i}{e_j} = 0)
}
$$
$$
x = \sum_{n=1}^{\infty} {\alpha_n e_n}, \quad \alpha_n = \frac{\veccross{x}{e_n}}{\veccross{e_n}{e_n}}
$$

# Theorem
([[901-сепарабельность|сепарабельность]])
$$
\Gather{
сепарабельность \\
\same \\
\text{есть базис Шаудера}
}
$$
