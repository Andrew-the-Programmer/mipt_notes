---
id: 1730897483-accept-reject-halt-notholt
aliases:
  - Accept-Reject-Halt-NotHolt
  - Accept
  - Reject
  - Halt
  - NotHolt
tags: []
---

# Accept Reject Halt NotHolt
`Let:`
$M$ - [[1729687005-машина-Тьюринга|машина Тьюринга]]
$$
\aligncenter{
Accept(M) \ldefeq \set{x \in \Gamma_{in}^* \mid M(x) = 1} \\
Reject(M) \ldefeq \set{x \in \Gamma_{in}^* \mid M(x) = 0} \\
Halt(M) \ldefeq Accept(M) \cup Regect(M) \\
NotHalt(M) \ldefeq \Gamma_{in}^* \setminus Halt(M)
}
$$
