#! /usr/bin/bash
null="> /dev/null 2>&1"
g="\033[1;32m"
r="\033[1;31m"
b="\033[1;34m"
w="\033[0m"
echo -e $b">"$w" TRISPI - Simple attaque par Ransomware pour Android"
echo -e $b">"$w" Préparation pour l'installation des dépendances ..."
sleep 3
echo -e $b">"$w" installation du paquet: "$g"default-jdk"$w
sudo apt-get install default-jdk -y
echo -e $b">"$w" iinstallation du paquet: "$g"aapt"$w
sudo apt-get install aapt zipalign -y
echo -e $b">"$w" installation du paquet: "$g"apktool"$w
sudo apt-get install apktool -y
echo -e $b">"$w" installation du paquet: "$g"imagemagick"$w
sudo apt-get install imagemagick -y
echo -e $b">"$w" installation du paquet: "$g"python3"$w
sudo apt-get install python3 python3-pip -y
echo -e $b">"$w" installation du module: "$g"pillow"$w
pip3 install Pillow
echo -e $b">"$w" installation des dépendances réussi"
echo -e $b">"$w" utilisez la commande "$g"python3 trispi.py"$w" pour démarrer la console"
