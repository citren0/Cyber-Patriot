#!/bin/bash

if [[ $EUID -ne 0 ]]; then
	echo "Run as root."
	exit 1
fi

sudo apt-get purge wireshark zenmap nmap ophcrack hydra-gtk aisleriot five-or-more four-in-a-row gnome-chess gnome-klotski gnome-mahjongg gnome-mines gnome-nibbles gnome-robots gnome-sudoku 
sudo apt-get purge gnome-tetravex hitori iagno lightsoff quadrapassel swell-foop tali gnome-hearts