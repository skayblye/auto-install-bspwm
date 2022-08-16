#!/usr/bin/python3

import subprocess

#instalacion de funestes y instalcion de terminal 
def installfont():
    
    #comandos
    #font = "sudo wget https://github.com/ryanoasis/nerd-fonts/releases/download/v2.1.0/Hack.zip -O /usr/local/share/fonts/Hack.zip"
    #zipfont = "sudo unzip /usr/local/share/fonts/Hack.zip -d /usr/local/share/fonts/"
    #deletezip = "sudo rm /usr/local/share/fonts/Hack.zip"
    
    installhackfonts = ["sudo wget https://github.com/ryanoasis/nerd-fonts/releases/download/v2.1.0/Hack.zip -O /usr/local/share/fonts/Hack.zip",
                        "sudo unzip /usr/local/share/fonts/Hack.zip -d /usr/local/share/fonts/",
                        "sudo rm /usr/local/share/fonts/Hack.zip"]
    
    subprocess.run(installhackfonts, shell=True)    
    

installfont()