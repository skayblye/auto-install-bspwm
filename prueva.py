#!/usr/bin/python3


def user():
     c = input("cual es el user?")

     a = ["hola, /home/user/, ¿como esta?",
          "wget https://raw.githubusercontent.com/skayblye/auto-install-bspwm/master/kitty.conf -O home/12345/.config/kitty/kitty.conf"]

     b = a[1].replace("12345", c)

     print(b)


user()