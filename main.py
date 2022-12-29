import csv

class Contacto():
	def __init__(self,empresa=None):
		self.name = input("Escribe el nombre del contacto:").title()
		self.email = input("Escribe el correo electrónico:").lower()
		self.telephone = input("Escribe el teléfono de contacto:")
		# Podemos asignar una empresa preexistente o bien, solicitar que se asigne desde 0.
		if empresa == None:
			self.empresa = Empresa()
		else:
			self.empresa=empresa

class Empresa():
	def __init__(self):
		self.name =input("Escribe el nombre de la empresa:").title()
		self.address = Direccion()
		self.rfc = input("Escribe el RFC de la empresa:").upper()
		self.url = input("Escribe la página web de la empresa:").lower()

class Direccion():
	def __init__(self):
		print("A continuación te vamos a solicitar los datos de la dirección.")
		self.street = input("Escribe la calle:").capitalize()
		self.number = input("Escribe el número:")
		self.city = input("Escribe la ciudad:").capitalize()
		self.state = input("Escribe el estado:").capitalize()
		self.country = input("Escribe el país:").capitalize()
		self.postalcode = input("Escribe el código postal:")

def guardarContacto(nuevo_contacto):
	contacto=[nuevo_contacto.name,
					nuevo_contacto.email,
					nuevo_contacto.telephone,
					nuevo_contacto.empresa.name,
					nuevo_contacto.empresa.address.street,
					nuevo_contacto.empresa.address.number,
					nuevo_contacto.empresa.address.city,
					nuevo_contacto.empresa.address.state,
					nuevo_contacto.empresa.address.country,
					nuevo_contacto.empresa.address.postalcode,
					nuevo_contacto.empresa.rfc,
					nuevo_contacto.empresa.url
			  ]
	filename=input("Introduce el nombre del archivo: ")
	with open(filename,"a",encoding='utf-8') as file:
		writer=csv.writer(file)
		writer.writerow(contacto)
	print("Se ha cerrado adecuadamente el archivo.")

nuevo_contacto=Contacto()
guardarContacto(nuevo_contacto)
