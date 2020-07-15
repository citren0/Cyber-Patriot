#!/bin/bash
sed -i -e 's/#PermitRootLogin/PermitRootLogin/g' /etc/ssh/sshd_config
sed -i -e 's/PermitRootLogin yes/PermitRootLogin no/g' /etc/ssh/sshd_config
sed -i -e 's/PermitRootLogin prohibit-password/PermitRootLogin no/g' /etc/ssh/sshd_config
systemctl restart sshd
