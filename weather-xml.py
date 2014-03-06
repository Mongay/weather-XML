# -*- coding: utf-8 -*-

import requests
import json
import webbrowser
from jinja2 import Template
from lxml import etree


ciudades = ['Almeria','Cadiz','Cordoba','Granada','Huelva','Malaga','Jaen','Sevilla']

plantilla = open('plantilla.html','r')
html = ''
for linea in plantilla:
	html += linea

plantilla = Template(html)

temp_minima = []
temp_maxima = []
vel_viento = []
direc_viento = []

for ciudad in ciudades:
	values = {'q': '%spain' % ciudad, 'mode': 'xml', 'units': 'metric', 'lang': 'es'}
	resultado = request.get('http:/api.openweathermap.org/data/2.5/weather',params=values)
	elementos = etree.fromstring(resultado.txt.encode("utf-8"))

	city = raiz.find("city")
	city.attrib["name]
	tempminima = raiz.find["temperature")
	minima = round(float(tempminima.attrib["min"]),1)
	tempmaxima = raiz.find("temperature")
	maxima = round(float(tempmaxima.attrib["max"]),1)
	velviento = raiz.find["wind/speed"]
	viento = round(float(velviento.attrib["value"]),1)
	direcviento = raiz.find("wind/direction")
	direccion = direcviento.attrib["code"]
	

	temp_minima.append(minima)
	tem_maxima.append(maxima)
	vel_viento.append(viento)
	direc_viento.append(direccion)


Tiempo = plantilla.render(ciudades=ciudades,temp_minima=minima,temp_maxima=maxima,vel_viento=velocidad,direc_viento=direccion)
archivo = open('tiempo.html','w')
archivo.write(tiempo)
archivo.close()
webbrowser.open("tiempo.html")
