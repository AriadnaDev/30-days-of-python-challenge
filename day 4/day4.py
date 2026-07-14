"""
Los formatos que permite Python de string son: 
1. Comillas simples (')
2. Comillas dobles (")
3. Triples comillas simples
4. Triples commilas dobles
"""

#Para hallar el largo usamos len(str)

#Para concatenar cadenas usando el +

"""
Las secuencias de escape son:

\n nueva línea
\t tabulador (8 espacios)
\\ slash hacia la izquierda
\" comilla simple
\' comilla doble

"""

"""

FORMATO 1 (MÁS ANTIGUO)

Para formatear los strings e incluirlos en un print por ejemplo:

%s -> cualquier string u objeto con string
%d -> enteros
%f -> flotantes
%.num -> flotantes con un número especificado de precisión

"""

#Ejemplo
nombre = "Ari";
lenguaje = "Python";

formateado = "Soy %s y estudio %s" %(nombre, lenguaje);

print(formateado);

"""
FORMATO 2 (+ NUEVO, A PARTIR DE V.3)

"""

#Ejemplo

formateado_2 = "Soy {} y estudio {}".format(nombre, lenguaje);

print(formateado_2);

#Interpolación de strings (v.3.6 en adelante) f-string

a = 4;
b = 3;

print(f"{a} + {b} = {a+b}");


#Python como secuencia de caracteres si queremos desempaquetarlo podemos hacerlo en forma de lista o tupla

a,b,c,d,e,f = lenguaje;

print(a)
print(b)
print(c)
print(d)
print(e)
print(f)


#Otro método para acceder a los strings es por su índice (empiezan por 0)

primera = lenguaje[0];
print(primera);

#último índice
ultima = len(lenguaje)- 1;
ultimo =lenguaje[ultima];
print(ultimo);

#trocear strings para convertirlos en substrings

primeras_3 = lenguaje[0:3];
print(primeras_3);
ultimas_3 = lenguaje[-3:];
print(ultimas_3);

#darles la vuelta a un string
hola = "buenas tardes";
print(hola[::-1]);


#saltar algunos caracteres (indicando cuantos)
salto = lenguaje[0:6:2];
print(salto)

#para que la primera sea capital con str.capitalize()
challenge = "treinta dias de python";
print(challenge.capitalize());
print(challenge.title())

#mayus en minus y viceversa
print(challenge.swapcase())

#para encontrar la posición str.count(str)

print(challenge.count("y"))

#comprobar si empieza o termina por algo, resultado BOOL str.startswith(letra)

print(challenge.startswith("x"))
print(challenge.endswith("n"))

#expandtabs() reemplaza el tab con espacios
print(challenge.expandtabs(10)); 

#buscar una recurrencia str.find(str)
print(challenge.find("y"));

"""
.format()

FORMA 1
como anteriormente 

FORMA 2
igual que el primero pero .format(str(var),float(var2))

"""

#encontrar el índice primero

substring = "tre";
print(challenge.index(substring));

#saber si es alfanum

print(challenge.isalnum())
print(challenge.isalpha())
print(challenge.isdecimal())
print(challenge.isdigit())
print(challenge.isnumeric())

#saber si es valido un nombre para una variable

valido=".num"
print(valido.isidentifier())

#mayus o minus
print(challenge.isupper())
print(challenge.islower())

#unir cadenas con espacios o lo que indiquemos

web = ["HTML", "CSS", "JS"];
resultado = " ".join(web);
print(resultado)
resultado1 = " lol ".join(web);
print(resultado1)

#quitar los caracteres indicados 
print(challenge.strip('thon'))

#reemplazar
print(challenge.replace("python", "programar"));

#separar el str, lo convertirá en una lista separandolo por espacios
print(challenge.split())

#podemos indicarlo quitandole algo personalizado
print(challenge.split(","))



#Ejercicios ---------------------------
#1. Concatenar str
e,f,g,h = "30", "dias", "de", "Python";
print("{} {} {} {}".format(e,f,g,h))
print("%s %s %s %s" %(e,f,g,h))

# 2.
company = "Coding For All" ;
print(company);
print("Es de largo: ", len(company))

# 3.
print(company.upper())
print(company.lower())
print(company.capitalize())
print(company.title())
print(company.swapcase())

#4.
print(company[6:])

#5. 
incluye = company.find("Coding")
print("Coding está en la posición", incluye)

#6.
palabra = "Python",
print(company.replace("All", palabra))
