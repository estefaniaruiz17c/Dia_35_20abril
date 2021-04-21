# Librería collections: Python tiene varias estructuras de datos integradas: tuplas, diccionarios y listas. Las estructuras de datos nos proporcionan una forma de organizar y almacenar datos. El módulo collections nos ayuda a completar y manipular las estructuras de datos de forma eficiente.
print("Librería Collections\n")

# Importar de collections, Counter
from collections import Counter

# Counter: permite contar las ocurrencias de un artículo en particular
print("\nCounter\n")

#Ejercicio 1: cantidad de veces que sale cada número de una lista
print("\n- Ejercicio 1:\n")

# Variable a utilizar 
lista1_numbers = [7,6,7,3,2,7,5,8,2,6]
print("\nLista original:",lista1_numbers,"\n")

# lista1_numbers con Counter
print(Counter(lista1_numbers))

# Ejercicio 2: cantidad de veces que sale una misma palabra en un string 
print("\n","- Ejercicio 2:\n")

# Variable a utilizar
string1 = "manzana papaya piña fresa papaya manzana papaya"
print("String original:",string1,"\n")

# string1 con Counter. Usamos split() para que se el string se divida en palabras, sin este, el Counter contará cada letra de forma individual
coun_string = Counter(string1.split())
print(coun_string)


# Ejercicio 3: cantidad de veces que sale cada letra en una palabra
print("\n","\n- Ejercicio 3:\n")

# Variable a utilizar
word1 = "hipopotomonstrosesquipedaliofobia" # Significa miedo a las palabras largas y complicadas
print("\nPalabra:",word1,"\n")

# word1 con Counter
print(Counter(word1))


print("\n","----------"*7,"\n")


# Importar de collections, defaultdict
from collections import defaultdict

# defaultdict: crear diccionarios con un valor por defecto aunque el registro no haya sido definido anteriormente
print("\ndefaultdict\n")

# Ejercicio 4: usar defaultdict de tipo int
print("\n- Ejercicio 4:\n")

# Creación del defaultdict
default_int = defaultdict(int, first=23, second=54, third=16)

# Mostrar el defaultdict
print(default_int,"\n")

# Ejercicio 5: usar defaultdict de tipo str
print("\n- Ejercicio 5:\n")

# Creación del defaultdict str
default_str = defaultdict(str)  

# Indicar valor de la clave
default_str['primero']

# Mostrar el defaultdict
print(default_str,"\n")

# Darle un valor a la clave 'primero'
default_str['primero'] = 'one'

# Mostrar el defaultdict str con la clave y el valor que acabamos de asignar
print("\n",default_str,"\n")


print("\n","----------"*7,"\n")


# Importar de collections, OrderedDict
from collections import OrderedDict

# OrderedDict: mantiene sus entradas ordenadas tal como se insertaron inicialmente
print("\nOrderedDict\n")

# Ejercicio 6: creación de un diccionario a partir de OrderedDict
print("\n- Ejercicio 6:\n")

# Creación del diccionario OrderedDict
dict1 = OrderedDict()

# Designación de claves y valores 
dict1["clave1"]="Enero"
dict1["clave2"]= "Febrero"
dict1["clave3"]= "Marzo"

# Mostrar el resultado
print("\n",dict1,"\n")

# Ejercicio 7: realizaremos la comparación de 2 diccionarios creados con OrderedDict para analizar de que si se estén almacenando en orden
print("\n- Ejercicio 7:\n")

# Creación del diccionario OrderedDict
dict2 = OrderedDict()

# Designación de claves y valores 
dict2["primero"]= "Paso 1"
dict2["segundo"]= "Paso 2"
dict2["tercero"]= "Paso 3"

# Mostrar el resultado
print("\nDiccionario 'a':",dict2,"\n")

# Creación del diccionario OrderedDict
dict3 = OrderedDict()

# Designación de claves y valores 
dict3["tercero"]= "Paso 3"
dict3["segundo"]= "Paso 2"
dict3["primero"]= "Paso 1"

# Mostrar el resultado
print("\nDiccionario 'b':",dict3,"\n")

# Comparación diccionario a y b
print("\nEl diccionario 'a' y 'b' son iguales?:",dict2==dict3)


print("\n","----------"*7,"\n")


# Importar de collections, deque
from collections import deque

# deque: admite agregar y eliminar elementos de cualquier extremo de la cola
print("\ndeque\n")

# Ejercicio 8: eliminar por el frente y por detras elementos 
print("\n- Ejercicio 8")

# Creación de la lista a utilizar
lista_deq1 = ["hola","queridos","estudiantes"]
print("\nLista original:\n",lista_deq1)

# Creación del deque 
deque1 = deque(lista_deq1)

# Eliminación del elemento de la izquierda
deque1.popleft()
# Mostrar el resultado después de popleft()
print("\nLuego de popleft():\n",deque1)

# Eliminación elemento de la derecha
deque1.pop()
# Mostrar el resultado después de pop()
print("\nLuego de pop():\n",deque1)


print("\n","----------"*7,"\n")


# Importar de collections, namedtuple
from collections import namedtuple

# namedtuple: utilizada para crear pequeñas estructuras inmutables, como una clase y sus objetos, pero más simples
print("\nnamedtuple\n")

# Ejercicio 9: ejemplo de namedtuple frutas
print("\n- Ejercicio 9")

# Creación de namedtuple
Frutas = namedtuple('Frutas','nombre color sabor')

frut = Frutas(nombre='Banano',color='amarillo',sabor='dulce')

# Impresión de la variable frut para conocer su estructura
print("\nCon namedtuple:",frut)

# Accedemos a los elementos como si fueran atributos de un objeto
print("\nColor de la fruta:",frut.color)
print("\nNombre de la fruta:",frut.nombre)
print("\nSabor de la fruta:",frut.sabor)


print("\n","----------"*7,"\n")


# Importar de collections, ChainMap
from collections import ChainMap

# ChainMap: encapsula varios diccionarios en una unidad
print("\nChainMap\n")

# Ejercicio 10: juntar varios dicionarios 
print("\n- Ejercicio 10")

# Creación de los diccionarios
di1 = {"nombre":"César","deporte":"natación"}
di2 = {"juez":"Sonia","edad":32}
di3 = {"premio":"trofeo","lugar":"primer puesto"}

# Mostrar los diccionarios
print("\nDiccionario 1:",di1)
print("\nDiccionario 2:",di2)
print("\nDiccionario 3:",di3)

# Uso de ChainMap
chain = ChainMap(di1,di3,di2)

# Mostrar el resultado
print("\nUsando ChainMap con los diccionarios anteriores, empezando por el 1, continuando con el 3 y terminando con el 2:\n","\n",chain)
