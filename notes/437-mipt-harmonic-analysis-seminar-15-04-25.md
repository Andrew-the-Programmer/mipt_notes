---
id: 437-mipt-harmonic-analysis-seminar-15-04-25
aliases:
  - MIPT harmonic analysis seminar 15-04-25
tags: []
---

# MIPT harmonic analysis seminar 15-04-25

# Немного несобственных интегралов

# 1.

$$
I(\alpha) = \int_0^{+\infty}{e^{-x^2} \cos\group{2\alpha x} \d x} \\
$$

$\Align{
I^1(\alpha) = -\int_0^{+\infty}{2x e^{-x^2} \sin\group{2\alpha x} \d x} \\
\textit{По пр. Вейерштрасса.} \\
I^1(\alpha) = \textit{по частям} = 
2 \alpha \int_0^{+\infty}{e^{-x^2} \cos\group{2\alpha x}} \\
{I}^{'} = 2 \alpha I \\
I = c e^{-\alpha^2} \\
I(0) = \frac{\sqrt{\pi}}{2} \\
}$

$$
I(\alpha) = \frac{\sqrt{\pi}}{2} e^{-\alpha^2} \\
$$

# Интеграл Френеля

$$
I = \int_0^{+\infty}{\sin x^2 \d x}
$$

$\Align{
t = x^2 \\
I = \frac{1}{2} \int_0^{+\infty}{\frac{\sin t}{\sqrt{t}} \d t} \\
\textit{Заметим:} \\
\frac{1}{\sqrt t} = \frac{2}{\sqrt{t}} \int_0^{+\infty}{e^{-t x^2} \d x} \\
I = \frac{1}{\sqrt\pi} \int_0^{\infty}{\d t \sin t \int_0^{\infty}{e^{-t x^2} \d x}} \\
\textit{Можно ли переставить интегралы?}\\
\textit{Ответ: почему бы и нет. (я не понял почему...) По теореме.} \\
I = \frac{1}{\sqrt\pi} \int_0^{\infty}{\d x \int_0^{\infty}{\d t e^{-t x^2} \sin t}} \\
J \defeq \int_0^{\infty}{e^{-t x^2} \sin t \d t} = \textit{по частям} = \\
= -\int_0^{\infty}{x^2 e^{-t x^2} \cos t \d t} = \textit{по частям} = \\
= 1 + \int_0^{\infty}{x^4 e^{-t x^2} \sin t \d t} \\
J = 1 + x^4 J \\
J = \frac{1}{1 + x^4} \\
I = \frac{1}{\sqrt\pi} \int_0^{\infty}{\d x \frac{1}{1 + x^4}}\\
G \defeq \int_0^{\infty}{\frac{\d x}{1 + x^4}}
H \defeq \int_0^{\infty}{\frac{x^2}{1 + x^4} \d x} = 
-\int_{\infty}^{0}{\frac{\d \group{\frac{1}{x}}}{1 + \group{\frac{1}{x}}^4}} =
\int_0^{\infty}{\frac{\d u}{1 + u^4}} \\
2 G = G + H = \int_0^{\infty}{\frac{1 + x^2}{1 + x^4} \d x} =
\int_0^{\infty}{\frac{x^{-2} + 1}{x^{-2} + x^2} \d x} = \\
\int_{-\infty}^{+\infty}{\frac{\d \group{x - \frac{1}{x}}}{x^{-2} + x^2} \d x} = \\
\int_{-\infty}^{+\infty}{\frac{\d u}{2 + u^2}} =\\

}$
