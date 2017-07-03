#!/usr/bin/env python
# -*- coding: utf-8 -*-

from scipy import ndimage,misc
import numpy as np
from lib import settings

def leer(path):
	try:
		img = ndimage.imread(path)
		return img
	except:
		print "[-] La imagen no existe [-]"

def guardar(img, path):	#guardar en directorio especifico
	try:
		misc.imsave(settings.BASE+path, img)
	except:
		print "[-] Error al Guardar la Imagen [-]"

def comparacion(img1, img2):
	if(img1.shape == img2.shape):
		tx,ty,tz = img1.shape
		for x in range(tx):
			for y in range(ty):
				if(img1[x][y].tolist()!=img2[x][y].tolist()):
					img1[x][y] = [255,0,0] #rojo
		guardar(img1,settings.BASE+"diferencias.png")
	else:
		print "[-] Error, Imagenes con tamanos distintos [-]"
