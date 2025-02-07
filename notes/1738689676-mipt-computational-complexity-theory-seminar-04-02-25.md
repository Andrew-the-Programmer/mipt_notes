---
id: 1738689676-mipt-complexity-theory-seminar-04-02-25
aliases:
  - MIPT complexity theory-seminar 04-02-25
tags: []
---

# MIPT complexity theory-seminar 04-02-25

## 1
Найти $O(n \log n)$ алгоритм на одноленточной МТ M : $M(1^n) = 1^{2n}$
## 2
$PAL = \set{x \in \Sigma^* \mid x = x^R}$ 
### 2.1
многоленточноая $= O(n)$
### 2.2
одноленточноая $\ge O(n^2)$
$$
\AlignLeft{
S_i(x) - \text{мн-во сост. МТ, когда она переходит границу i-го символа} \\
x,y \in PAL \land S_i(x) = S_j(y) \implies
x[:i]y[j:], y[:j]x[i:] \in PAL \\
I_n = \set{x 2^{2n} x^R \mid \abs{x} = n} \\
\forall x \in I_n \forall i \in [n, 3n] \hthen \abs{S_i(x)} \le T(4n) / 2n \\
\forall x_1, x_2 \in I_n \hthen S_i(x_1) \neq S_j(x_2) \\
\abs{I_n} = 2^n \\
\abs{\set{S_i(x)}} =(<?) \sum_{i=0}^{T(4n) / 2n}{\abs{Q}^i} \le 
\abs{Q}^{T(4n) / 2n} \\
\abs{I_n} \le \abs{\set{S_i(x)}} \\
\implies \\
T(n) \ge \frac{n}{2} \left(\frac{n}{4} \log_{\abs{Q}}{2} - 1\right) \ge n^2
}
$$
## 3
$DTIME(n) \neq DTIME(n^2)$
