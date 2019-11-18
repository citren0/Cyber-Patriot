#!/bin/bash
echo 'Run as root.'

chmod 777 /etc/shadow
chmod 777 /etc/passwd
cp /etc/shadow /etc/shadow.bk
cp /etc/passwd /etc/passwd.bk

chmod 640 ~/.bash_history
chmod 600 /etc/shadow
chmod 644 /etc/passwd
chmod 644 /etc/hosts
chmod 644 /etc/lightdm/lightdm.conf
chmod 644 /etc/apt/sources.list
