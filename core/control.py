#!/usr/bin/env python
# -*- coding: utf-8 -*-

from core.visual import *
from core.stego import *

def main(arg):
	if(arg.output == None):
		arg.output = "salida.png"

	#VISUAL TECNIQUES
	if arg.tec == '0': 	#shamir
		if arg.act == 'encode':
			shamir.cipher(arg.input[0],arg.output)
		else:
			shamir.decipher(arg.input,arg.output)
	else:
		pass

	#STEGO TECNIQUES
	if arg.tec == 1:
		pass
	else:
		pass
