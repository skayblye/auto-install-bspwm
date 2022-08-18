#!/usr/bin/python3

from dataclasses import replace
import subprocess


def shellerores():
    shellpregunta = "echo $?"
    
    errores = subprocess.run(shellpregunta, shell=True)
    return errores

# actializacion de dependecias
def systemupdate():
    updatesystem = "sudo apt update -y"
    
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
    
    username = input("¿cual es tu username?")
    user = "usermod --shell /usr/bin/zsh " + str(username)
    
    zsh= ["sudo apt install zsh",
        "git clone --depth=1 https://github.com/romkatv/powerlevel10k.git ~/powerlevel10k && echo 'source ~/powerlevel10k/powerlevel10k.zsh-theme' >>~/.zshrc",
        "usermod --shell /usr/bin/zsh root",
        "ln -s -f /home/user/.zshrc .zshrc"]
    
    simbolico = zsh[3].replace("user",username)
    
    subprocess.run(zsh[0], shell=True)
    subprocess.run(zsh[1], shell=True)
    subprocess.run(zsh[2], shell=True)
    subprocess.run(user, shell=True)
    subprocess.run(simbolico, shell=True)


systemupdate()
installfont()
zshinstall()
