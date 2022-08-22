#!/usr/bin/python3
#version: python 3.9.2

from dataclasses import replace
import subprocess

username = input("¿cual es tu username? ")

# actializacion de dependecias
def systemupdate():
    updatesystem = ["apt update",
                    "apt install bspwm sxhkd picom feh polybar rofi i3lock kitty ranger -y"]
    
    subprocess.run(updatesystem[0], shell=True)
    subprocess.run(updatesystem[1], shell=True)
    
#instalacion de funestes y instalcion de terminal 
def installfont():
    
    #comandos
    installhackfonts = ["sudo wget https://github.com/ryanoasis/nerd-fonts/releases/download/v2.1.0/Hack.zip -O /usr/local/share/fonts/Hack.zip",
                        "sudo unzip /usr/local/share/fonts/Hack.zip -d /usr/local/share/fonts/",
                        "sudo rm /usr/local/share/fonts/Hack.zip"]
    
    #NOTA PERSONAL: recuerda buscar una manera de hacer esto sin tres subprocess.run
    subprocess.run(installhackfonts[0], shell=True)
    subprocess.run(installhackfonts[1], shell=True)
    subprocess.run(installhackfonts[2], shell=True)

#instalacion de zsh   
def zshinstall():
    
    #pasamos el nombre de usuario a otra varivle con el comando 
    user = "usermod --shell /usr/bin/zsh " + str(username)
    
    zsh= ["sudo apt install zsh -y",
        "git clone --depth=1 https://github.com/romkatv/powerlevel10k.git ~/powerlevel10k && echo 'source ~/powerlevel10k/powerlevel10k.zsh-theme' >>~/.zshrc",
        "usermod --shell /usr/bin/zsh root",
        "cd && ln -s -f /home/user/.zshrc .zshrc"]
    
    #renplazamos la palabra user del ultimo comando con el usuario intruducido en la variable usermane
    simbolico = zsh[3].replace("user", username)
   
    subprocess.run(zsh[0], shell=True)
    subprocess.run(zsh[1], shell=True)
    subprocess.run(zsh[2], shell=True)
    subprocess.run(user, shell=True)
    subprocess.run(simbolico, shell=True)

#instalacion de kitty y configuraciones
def kittyinstall():
    
    kitty = ["wget -P /home/12345/.config/kitty/ https://raw.githubusercontent.com/skayblye/auto-install-bspwm/master/kitty.conf",
             "wget -P /home/12345/.config/kitty/ https://raw.githubusercontent.com/skayblye/auto-install-bspwm/master/color.ini"]
    
    a = kitty[0].replace("12345", username)
    b = kitty[1].replace("12345", username)
    
    subprocess.run(a, shell=True)
    subprocess.run(b, shell=True)
    
def bspwminstall():
    
    bspwm = ["cd ~/.config/ && mkdir bspwm sxhkd && cd bspwm && mkdir scripts",
             "wget -P ~/.config/bspwm/ https://raw.githubusercontent.com/skayblye/auto-install-bspwm/master/bspwm/bspwmrc",
             "wget -p ~/.config/bspwm/scripts/ https://raw.githubusercontent.com/skayblye/auto-install-bspwm/master/bspwm/scripts/bspwm_resize"
             "wget -P ~/.config/sxhkd/ "]


systemupdate()
installfont()
zshinstall()
kittyinstall()