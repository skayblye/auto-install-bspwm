# auto-install-bspwm

Un pequeño script, programado en python 3 para automatizar la instalación de bspwm y su configuración, así como un entorno funcional personalizado.

**IMPORTANTE**

- Este script solo ha sido probado en **Parrot OS 5.0 (Electro Ara)**.
  
- Siempre será recomendable su instalación en una máquina virtual con algún snapshot guardado.
  

## Instalacion

```
git clone https://github.com/skayblye/auto-install-bspwm

cd auto-install-bspwm/
```

La instalación está dividida en dos partes actualmente. La primera necesita root para funcionar e instalar lo necesario. La segunda es con su usuario.

```
sudo su


python3 install.py
```

### Vista general

![vista general 1](https://raw.githubusercontent.com/skayblye/auto-install-bspwm/master/img/zero1.png)

![vista general 2](https://raw.githubusercontent.com/skayblye/auto-install-bspwm/master/img/zero3.png)

![vista general 3](https://raw.githubusercontent.com/skayblye/auto-install-bspwm/master/img/zero4.png)

### Utilidades:

- **bspwm**:  Tiling Window Manager.
  
- **zsh**: Shell.
  
- **powerlevel10k**: Tema de la zsh.
  
- **sxhkd**: Gestor de shortcuts.
  
- **polybar**: Barra de estado.
  
- **polybar-themes**: Tema de la barra de estado.
  
- **picom**: Gestiona transparencias y sombras.
  
- **kitty**: Terminal.
  
- **rofi**: lanzador de aplicaciones
  
- **feh**: Visor de imágenes, usado para cargar el fondo.
  
- **Hack Nerd Font**: Fuente.
