---
id: 1738759267-mipt-differential-equations-seminar-05-02-25
aliases:
  - MIPT differential equations seminar 05-02-25
tags: []
---

# MIPT differential equations seminar 05-02-25
## 19.102
$$
I(y) = \int_0^\pi{(y_x^2 - \frac{16}{9} y^2 + 2 y \sin x) \d x}
$$
$$
\AlignLeft{
F(x, y, {y}^{'}) = y_x^2 - \frac{16}{9} y^2 + 2 y \sin x \\
F_y = \pdv{y}{F} = \Dv{x}{\Dv{{y}^{'}}{F}} = \Dv{x}{2 {y}^{'}} = 2 {y}^{''} \\
{y}^{''} + \frac{16}{9} y = \sin x - \text{ур-ие Эйлера} \\
{y}^{''} + \frac{16}{9} y = 0 \\
y_o = C_1 \cos{\frac{4}{3} x} + C_2 \sin{\frac{4}{3} x} \\
y = y_o + \frac{9}{7} \sin x
C_1 = 0, \quad C_2 = 1 \\
y = \sin{\frac{4}{3} x} + \frac{9}{7} \sin x - \text{допустимая экстремаль} \\
h(0) = 0, \quad h(\pi) = 0 \\
\int{{y}^{'} {h}^{'} \d x} = \int{{y}^{'} \d h} = h {y}^{'} - \int{h {y}^{''} \d x} \\
\D I = I(y + h) - I(y) = \dots = 
\int_0^\pi{( h_x^2 - \frac{16}{9} h^2 ) \d x} + \int{...} 
}
$$

## T1
## 20.1.9
