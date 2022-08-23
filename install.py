#!/usr/bin/python3
#version: python 3.9.2

from dataclasses import replace
import subprocess

username = input("¿cual es tu username? ")

# actializacion de dependecias (root)
def systemupdate():
    updatesystem = ["apt update",
                    "apt install bspwm sxhkd picom feh polybar rofi i3lock kitty ranger git -y"]
    
    subprocess.run(updatesystem[0], shell=True)
    subprocess.run(updatesystem[1], shell=True)
    
#instalacion de funestes y instalcion de terminal (root)
def installfont():
    
    #comandos
    installhackfonts = ["wget https://github.com/ryanoasis/nerd-fonts/releases/download/v2.1.0/Hack.zip -O /usr/local/share/fonts/Hack.zip",
                        "unzip /usr/local/share/fonts/Hack.zip -d /usr/local/share/fonts/",
                        "rm /usr/local/share/fonts/Hack.zip"]
    
    #NOTA PERSONAL: recuerda buscar una manera de hacer esto sin tres subprocess.run
    subprocess.run(installhackfonts[0], shell=True)
    subprocess.run(installhackfonts[1], shell=True)
    subprocess.run(installhackfonts[2], shell=True)

#instalacion de zsh (root)
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

#instalacion de zsh para el usuario normal
def zshinstalluser():
    
    zsh = ["cd",
           "git clone --depth=1 https://github.com/romkatv/powerlevel10k.git ~/powerlevel10k && echo 'source ~/powerlevel10k/powerlevel10k.zsh-theme' >>~/.zshrc"]
    
    subprocess.run(zsh[0], shell=True)
    subprocess.run(zsh[1], shell=True)
    
#instalacion de kitty y configuraciones
def kittyinstall():
    
    kitty = ["mv color.ini ~/.config/kitty/",
             "mv kitty.ini ~/.config/kitty/"]
    
    subprocess.run(kitty[0], shell=True)
    subprocess.run(kitty[1], shell=True)
 
#instalacion de bspwm y sxhkd con sus configuraciones
def bspwminstall():
    
    bspwm = ["mv bspwm/ ~/.config/",
             "mv sxhkd/ ~/.config/",
             "cd && cd ~/.config/bspwm/ && chmod +x bspwmrc",
             "cd && cd ~/.config/bspwm/scripts/ && chmod +x bspwm_resize"]
    
    subprocess.run(bspwm[0], shell=True)
    subprocess.run(bspwm[1], shell=True)
    subprocess.run(bspwm[2], shell=True)
    subprocess.run(bspwm[3], shell=True)

#instalacion de picom
def picominstall():
    
    picom = "mv picom/ ~/.config/"
    
    subprocess.run(picom, shell=True)

#instacion de polybar
def polybarinstall():
    polybar = ["git clone --depth=1 https://github.com/adi1090x/polybar-themes.git && cd polybar-themes && chmod +x setup.sh",
               "./setup.sh"]
    
    subprocess.run(polybar[0], shell=True)
    subprocess.run(polybar[1], shell=True)
    

systemupdate()
installfont()
zshinstall()
kittyinstall()
bspwminstall()
polybarinstall()
