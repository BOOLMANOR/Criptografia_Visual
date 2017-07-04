#!/usr/bin/env python
# -*- coding: utf-8 -*-

from scipy import ndimage,misc
import numpy as np
from lib import imagen


def cipher(imgI, imgo):
	img = imagen.leer(imgI)
	tx,ty,tz = img.shape
	tm = 2

	#sombras
	s1 = np.ndarray((tx*2,ty*2,3), dtype="uint8")
	s2 = np.ndarray((tx*2,ty*2,3), dtype="uint8")

	for x in range(tx):
		for y in range(ty):
			if (img[x][y][0]==255):	#pixel blanco
				encode(0,np.random.randint(0,3),s1,s2,x*tm,y*tm)
			else:	#pixel Negro
				encode(1,np.random.randint(0,3),s1,s2,x*tm,y*tm)
	imagen.guardar(s1,"Sombra1.jpg")
	imagen.guardar(s2,"Sombra2.jpg")
	#print "salidaaaaaa"

def decipher(imgI, imgo):
	img1 = imagen.leer(imgI[0])
	img2 = imagen.leer(imgI[1])

	tx,ty,tz = img1.shape
	ds = np.ndarray((tx,ty,tz), dtype="uint8")

	for x in range(tx):
		for y in range(ty):
			if(img1[x][y][0]==255 and img2[x][y][0]==255):
				ds[x][y] = [255,255,255]
			else:
				ds[x][y] = [0,0,0]
	print "Secreto:     \tDescifrada.jpg"
	imagen.guardar(ds,"Descifrada.jpg")

#funciones adicionales del CIPHER ------------------------------ #
def transpuesta(opt): #2x2
	if (opt == 0):
		tr = [ [[255,255,255],[0,0,0]], # BW
		      [[0,0,0],[255,255,255]] ] # WB
	elif (opt == 1):
		tr = [ [[255,255,255],[0,0,0]], # BW
			  [[255,255,255],[0,0,0]] ] # BW
	else:
		tr = [ [[255,255,255],[255,255,255]], # BB
			   [[0,0,0],[0,0,0]] ] 			  # WW
	return tr

def basica(opt): #2x2
	if (opt == 0):
		tr = [ [[0,0,0],[255,255,255]],  # WB
			   [[255,255,255],[0,0,0]] ] # BW
	elif (opt == 1):
		tr = [ [[0,0,0],[255,255,255]],  # WB
			   [[0,0,0],[255,255,255]] ] # WB
	else:
		tr = [ [[0,0,0],[0,0,0]],   			# WW
			   [[255,255,255],[255,255,255]] ]  # BB
	return tr

def encode(n, sombra, imag1, imag2,i,j):
	temp = np.random.randint(0,2)	#hacemos aleatorio la sombra blanca y negra
	if(n == 0):
		#temp2 = np.random.randint(0,3)
		if(temp == 0):	#ampliamos de 3 a 6 matrices basicas
			s1,s2 = basica(sombra),basica(sombra)
		else:
			s1,s2 = transpuesta(sombra),transpuesta(sombra)
	else:
		if(temp == 0):	#intercambiamos sombras
			s1,s2 = basica(sombra),transpuesta(sombra)
		else:
			s2,s1 = basica(sombra),transpuesta(sombra)
	#guardamos en primera sombra
	imag1[i][j] = s1[0][0]
	imag1[i][j+1] = s1[0][1]
	imag1[i+1][j] = s1[1][0]
	imag1[i+1][j+1] = s1[1][1]

	#guardamos en segunda sombra
	imag2[i][j] = s2[0][0]
	imag2[i][j+1] = s2[0][1]
	imag2[i+1][j] = s2[1][0]
	imag2[i+1][j+1] = s2[1][1]
