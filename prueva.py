#!/usr/bin/python3

c = input("cual es el user?")

a = ["hola, /home/user/, ¿como esta?",
     "hola, username, como estas?"]

b = a[0].replace("user", c)

print(b)
