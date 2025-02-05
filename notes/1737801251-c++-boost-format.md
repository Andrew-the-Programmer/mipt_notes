---
id: 1737801251-c++-boost-format
aliases:
  - c++-boost-format
  - format
tags: []
---

# c++ boost format
[boost wiki](https://www.boost.org/doc/libs/1_77_0/libs/format/doc/format.html)
```cpp
#include <boost/format.hpp>
auto format = boost::format("writing %1%,  x=%2% : %3%-th try");
format % "toto" % 40.23 % 50
// writing toto,  x=40.230 : 50-th try
```
