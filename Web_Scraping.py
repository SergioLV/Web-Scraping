import requests	
import re

def CheckName(actor,datos):

	if datos.url == "https://www.boxofficemojo.com/people/":
		actor = input("Oops! Al parecer ingresaste mal el nombre, intenta denuevo: ")
		print ("\n")
		datos = requests.get('https://www.boxofficemojo.com/people/chart/?id='+actor.replace(" ","")+'.htm')
		CheckName(actor,datos)
	else:
		ITB(datos)
		ITBInflacion(datos)
		Peliculas(datos)
		PeliculasMayorIngreso(actor)
		PeliculasMenorIngreso(actor)
	return

def ITB(datos): 
	ITB = re.findall(r"Lifetime\sGross\sTotal\s\((.*?)\):\s(\$([0-9]{1,3},([0-9]{3},)*[0-9]{3}|[0-9]+)(\.[0-9][0-9])?)", datos.text)
	print ("Ingreso total bruto: ", ITB[0][1])
	print ("\n")

	return 


def ITBInflacion(datos): 
	AdjustedTotal = re.findall(r"Adjusted\sTotal\:\s(\$([0-9]{1,3},([0-9]{3},)*[0-9]{3}|[0-9]+)(\.[0-9][0-9])?)", datos.text)
	print ("Ingreso total bruto ajustado a la inflacion: ", AdjustedTotal[0][1])
	print ("\n")

	return 

def Peliculas(datos):
	Totalpeliculas = re.findall(r"<b>(.*?)</b>", datos.text)
	PeliculasGrises = re.findall(r"<font color=\"\#666666\">(.*?)</font>", datos.text)
	cont = 0

	print ("Ultimas 5 peliculas: ")

	for peliculas in range (1,6):
		
		match = re.match(r"<font color=", Totalpeliculas[peliculas])
		match2 = re.match(r"Average",Totalpeliculas[peliculas])
		
		if match2:
			print("\n")
			return

		if match:
			if PeliculasGrises[cont-1] != '(Cameo)' and PeliculasGrises[cont-1] != '(Voice)' and PeliculasGrises[cont-1] != '(Narrator)':
				print (PeliculasGrises[cont])
				cont = cont + 2
			else:
				print(PeliculasGrises[cont+1])
		else: 
			print (Totalpeliculas[peliculas])	

	print ("\n")	

	return

def PeliculasMayorIngreso(actor):
	datos = requests.get('https://www.boxofficemojo.com/people/chart/?view=Actor&id='+actor.replace(" ","")+'.htm&sort=gross&order=DESC&p=.htm')
	Totalpeliculas = re.findall(r"<b>(.*?)</b>", datos.text)
	PeliculasGrises = re.findall(r"<font color=\"\#666666\">(.*?)</font>", datos.text)
	cont = 0

	print ("10 peliculas con mayor ingreso: ")


	for peliculas in range(0,20):
		if peliculas % 2 == 1:
			match = re.match(r"<font color=", Totalpeliculas[peliculas])
			match2 = re.match(r"Average",Totalpeliculas[peliculas])
		
			if match2:
				print("\n")
				return

			if match:
				if PeliculasGrises[cont-1] != '(Cameo)' and PeliculasGrises[cont-1] != '(Voice)' and PeliculasGrises[cont-1] != '(Narrator)':
					print (PeliculasGrises[cont])
					cont = cont + 2
				else:
					print(PeliculasGrises[cont+1])
			else: 
				print (Totalpeliculas[peliculas])	


	print ("\n")

	return

def PeliculasMenorIngreso(actor):
	datos = requests.get('https://www.boxofficemojo.com/people/chart/?view=Actor&id='+actor.replace(" ","")+'.htm&sort=gross&order=ASC&p=.htm')
	Totalpeliculas = re.findall(r"<b>(.*?)</b>", datos.text)
	PeliculasGrises = re.findall(r"<font color=\"\#666666\">(.*?)</font>", datos.text)
	cont = 0

	print ("10 peliculas con menor ingreso: ")

	for peliculas in range(0,20):
		if peliculas % 2 == 1:
			match = re.match(r"<font color=", Totalpeliculas[peliculas])
			match2 = re.match(r"Average",Totalpeliculas[peliculas])
		
			if match2:
				print("\n")
				return

			if match:
				if PeliculasGrises[cont-1] != '(Cameo)' and PeliculasGrises[cont-1] != '(Voice)' and PeliculasGrises[cont-1] != '(Narrator)':
					print (PeliculasGrises[cont])
					cont = cont + 2
				else:
					print(PeliculasGrises[cont+1])
			else: 
				print (Totalpeliculas[peliculas])	


	print ("\n")

	return



if __name__ == '__main__':
	actor = input("Nombre del actor: ")
	datos = requests.get('https://www.boxofficemojo.com/people/chart/?id='+actor.replace(" ","")+'.htm')
	CheckName(actor,datos)