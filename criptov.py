#!/usr/bin/env python
# -*- coding: utf-8 -*-

from core import control
from lib import settings
from lib import parse

def main():
	settings.header() #headers
	args = parse.show(settings.VERSION) #parser de datos
	control.main(args)

if __name__ == "__main__":
	main()
