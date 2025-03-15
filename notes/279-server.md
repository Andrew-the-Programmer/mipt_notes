---
id: 279-server
aliases:
  - server
tags: []
---

# server

# [[1728763957-ssh|ssh]]

# Linux

## Add wheel group

```bash
groupadd wheel
echo "%wheel ALL=(ALL) ALL" >> /etc/sudoers
```
## Add user

```bash
useradd -m <username>
passwd <username>
usermod -G wheel <username>
```

## Create ssh
```bash
ssh-keygen -t rsa -b 4096
```
