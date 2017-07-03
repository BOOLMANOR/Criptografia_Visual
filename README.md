# Criptografia Visual y Esteganografia
---------------------------------------
v1.0.0  | encode & decode 
---------------------------------------

A la espera de implementar más técnicas de criptografía visual y esteganografía. 

# Tecnicas
  0) Sistema de Umbral - Shamir (1,2) (un secreto y dos llaves) 

# Encode
```
python criptov.py --act encode --tec 0 -i examples/mensaje.png
```
Dando como Resultado 2 imagenes: 
1) 
![Sombra1](https://github.com/D14M4NT3/Criptografia_Visual/blob/master/temp/Sombra1.jpg?raw=true)
2)
![Sombra2](https://github.com/D14M4NT3/Criptografia_Visual/blob/master/temp/Sombra2.jpg?raw=true)
# Decode
```
python criptov.py --act decode --tec 0 -i temp/Sombra1.jpg -i temp/Sombra2.jpg
```
Dando como resultado la recuperación del secreto inicial. 
3)
![Descifrada](https://raw.githubusercontent.com/D14M4NT3/Criptografia_Visual/master/temp/Descifrada.jpg)

# Actualizaciones

Es constante actualización. 
