---
id: 279-server
aliases:
  - server
tags: []
---

# server
https://www.youtube.com/watch?v=Lk_v6Q0YsNo&t=931s

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
# enter ssh key name
# enter passphrase

# copy key to server
scp ./<ssh key>.pub [<username>@]<IP>:[dir | ~ if empty]
mkdir .ssh
touch .ssh/authorized_keys
cat <ssh key>.pub >> .ssh/authorized_keys
rm server1.pub
```
