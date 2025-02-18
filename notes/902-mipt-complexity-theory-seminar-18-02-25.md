---
id: 902-mipt-complexity-theory-seminar-18-02-25
aliases:
  - MIPT complexity theory seminar 18-02-25
tags: []
---

# MIPT complexity theory seminar 18-02-25
Морфизм.
Нестирающий морфизм.

# 1
$$
P = NP \same P \text{замкнут отн. нестирающих морф.}
$$
$$
\AlignLeft{
\implies \\
P = NP \\
L \in P \\
\text{Want to show } f(L) \in P = NP \\
M_s(x,y): \\
1) \abs{y} \le \abs{x} \\
2) M_L(y) = 1 \\
3) z = f(y) \\
4) x = z \\
\impliedby \\
}
$$

# 2
$Primes \defeq \set{\text{двоичная запись простых}} \in NP, \co NP$
 $$
\AlignLeft{
1)\ Primes \in \co NP \\
M_s(x,y): y \mid x \\
2)\ Primes \in NP \\
bombaclat 💔 \\
}
$$

# [[736-полиномиальная-сводимость-сводимсть-по-Карпу|полиномиальная сводимость]]

- CNF-SAT
- 3-CNF-SAT
- VertexCover
- Clique
- 3-color

# 3
$$
L \in NP-c, \quad L \in \co NP \implies NP = \co NP
$$

# 4
$$
(\co NP)-complete = \co(NP-complete)
$$

# 5
$$
\Halt \in NP-hard
$$

# 6
$$
Clique \same AntiClique
$$

# 7
$$
Clique \same VertexCover
$$
