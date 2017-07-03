#!/usr/bin/env python
# -*- coding: utf-8 -*-

import argparse

def show(VERSION):
    ps = argparse.ArgumentParser(description='Ingrese los datos para el correcto funcionamiento del Script')
    ps.add_argument("--act", choices=['decode', 'encode'], required=True, help="Accion a Realizar")
    ps.add_argument("--tec", required=True, help="Tecnica a Utilizar")
    ps.add_argument("-o", dest="output",help="Imagen de Resultado")
    ps.add_argument("-i", dest="input", required=True, action="append", help="Imagenes de Entrada")
    ps.add_argument("--version",action='version', version=VERSION)
    args = ps.parse_args()
    return args
