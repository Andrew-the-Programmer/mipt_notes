---
id: 835-mipt-computational-complexity-theory-lecture-21-02-25
aliases:
  - MIPT computational complexity theory lecture 21-02-25
tags: []
---

# MIPT computational complexity theory lecture 21-02-25
Полные языки.
$$
\Gather{
L_{NP} \defeq \set{(N, x, 1^t) \mid N - НМТ\ принимает\ x\ за\ t\ тактов} \\
L_{NP} \in \NP-hard \\
}
$$
$$
\Gather{
L_{P} \defeq \set{(N, x, 1^t) \mid N - МТ\ принимает\ x\ за\ t\ тактов} \\
L_{P} \in \P-hard \\
}
$$

# Theorem. Кука-Левина.
$$
\Gather{
Sat \defeq \set{\varphi \mid \varphi - выполнима} \\
CNFSat \defeq \set{\varphi \mid \varphi - КНФ\ и\ выполнима} \\
3-CNFSat \defeq \set{\varphi \mid \varphi - КНФ,\ выполнима и\ \textit{в каждом дизъюнкте }} \\
}
$$
