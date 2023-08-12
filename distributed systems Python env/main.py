#importacion de librerias
import mysql.connector


#declaracion de la conexion con la base de datos

# declaracion de una clase en python
class personaje:
	nombre = 'Arno Dorian'
	fuerza = 5
	inteligencia = 2
	defensa = 3
	vida = 0

	# declaracion de el metodo constructor de la clase en python	
	# LA clase inicializadora de la clase donde el self dice que se referencia a si misma
	def __init__(self, nombre, fuerza, inteligencia,defensa, vida):
		self.nombre = nombre
		self.fuerza = fuerza
		self.inteligencia = inteligencia
		self.defensa =defensa
		self.vida = vida
		
		# declaracion de los metodos para imprimir los atributos
	def imprimirAtributos(self):
		print("nombre:", self.nombre)
		print("fuerza:", self.fuerza)
		print("inteligencia:", self.inteligencia)
		print("defensa:", self.defensa)
		print("vida:", self.vida)
		
		# Metodo para subir nivel
	def subirNivel(self, fuerza, inteligencia, defensa, vida):
		self.fuerza += fuerza
		self.inteligencia += inteligencia
		self.defensa += defensa
		self.vida += vida

	def saveperson(self, nombre, fuerza, inteligencia,defensa, vida):
		fecha = '2002-09-20'
		#notas para identificar las partes la cadena de la conexion para la base de datos
		#mysql -hcontainers-us-west-101.railway.app -uroot -pKq2hMlEqVuNNO1wn82cA --port 7171 --protocol=TCP railway
		#la primera parte donde dice mysql es el tipo de lenguaje que se usara de database
		# despues de la h es el hotst hasta el -u
		#el -u despues de eso dice el usuario en este caso es root
		#el-p es la contraseña en este caso lo que este despues es la contraseña 
		#luego obviamente es un port es el puerto 
		# y luego el protocolo
		conex = mysql.connector.connect(user='root', password='Kq2hMlEqVuNNO1wn82cA', host='containers-us-west-101.railway.app', database='railway', port=7171)
		print('Conexion exitosa', conex)
		mycursor = conex.cursor()
		#query = 'INSERT INTO personaje (id,nombre,fuerza,inteligencia,defensa,vida,fecha) VALUES (1193080520,"Ludwing",15,100,20,500,"2002-09-20")'
		query = 'INSERT INTO personaje (id,nombre,fuerza,inteligencia,defensa,vida,fecha) VALUES (1193080520,"Ludwing",15,100,20,500,"2002-09-20")'
		mycursor.execute(query)
		conex.commit()
		

# buena practica es declarar una condicion para que reconozca el main dentro del python
# el alcance de esta condicion es que debe iniciar desde el main
if __name__ == '__main__':
	print('Hello World')
	# Creamos una variable de tipo de la clase que creamos
	# ahora debeos poner dentro de la clase los nuevos atributos que se reciben
	mi_personaje = personaje('Ludwing', 1, 2, 3, 4)
	# imprimimos el atributo de la clase mediante la variable que declaramos
	print(mi_personaje.nombre)
	# llamamos al metodo imprimirAtributos para imprimir de una mejor forma los atributos
	mi_personaje.imprimirAtributos()
	# llamamos metodo de subir nivel
	mi_personaje.subirNivel(1000, 1500, 10000, 1_000_000)
	mi_personaje.imprimirAtributos()
	mi_personaje.saveperson( 'Ludwing',1000, 1500, 10000, 1_000_000)
