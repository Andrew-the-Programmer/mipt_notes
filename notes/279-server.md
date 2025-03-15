---
id: 279-server
aliases:
  - server
tags: []
---

# server

# [[1728763957-ssh|ssh]]

# Linux

## Add user

```bash
# Add wheel group
groupadd wheel
vim /etc/sudoers

useradd -m <username>
passwd <username>
usermod -G wheel <username>
```
