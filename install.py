#!/usr/bin/python3
#version: python 3.9.2

from dataclasses import replace
import subprocess

username = input("¿cual es tu username? ")

def shellerores():
    shellpregunta = "echo $?"
    
    errores = subprocess.run(shellpregunta, shell=True)
    return errores

# actializacion de dependecias
def systemupdate():
    updatesystem = "sudo apt update"
    
    subprocess.run(updatesystem, shell=True)
    
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
    
    #pedimos el nombre de usuario para usarlo en establecer la shell principal como zsh y para hacer un enlase en la config del usuario y de root
   
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
    
    kitty = ["sudo apt install kitty -y",
             "wget -P /home/12345/.config/kitty/ https://raw.githubusercontent.com/skayblye/auto-install-bspwm/master/kitty.conf",
             "wget -P /home/12345/.config/kitty/ https://raw.githubusercontent.com/skayblye/auto-install-bspwm/master/color.ini"]
    
    a = kitty[1].replace("12345", username)
    b = kitty[2].replace("12345", username)
    
    subprocess.run(kitty[0], shell=True)
    subprocess.run(a, shell=True)
    subprocess.run(b, shell=True)
    

systemupdate()
installfont()
zshinstall()
kittyinstall()