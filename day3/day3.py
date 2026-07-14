import math;

#Los booleanos True False son la primera en mayúscula a diferencia de JavaScript

#El signo = se utiliza para asignar un valor, en caso de que queramos que un dato sea igual a otro tenemos que usar el doble igual ==

#Aparte de los signos matemáticos para comparar, permite alternar con is, is not, in, not in, and, or, not; que devolveran resultados booleanos

#Ejercicios -------------------------
#1. Declarar la edad como un entero
edad = 500;

#2. altura como un flotante
altura = 1.67;

#3. número complejo
complejo = 3j;

#4. calcular el área de un triángulo
base = float(input("Escribe la base del triángulo: "));

altura = float(input("Escribe la altura del triángulo: "));

area = 0.5 * base * altura;

print("El área del triángulo es de: ", area);

print("\n");

#5. Calcular el perímetro del triángulo
lado_a = float(input("Escribe un lado del triángulo: "));

lado_b = float(input("Escribe otro lado del triángulo: "));

lado_c = float(input("Escribe el último lado del triángulo: "));

perimetro = lado_a + lado_b + lado_c;

print("El perímetro del triángulo es de: ", perimetro);

#6. Obtener el largo y ancho de un rectángulo

largo = float(input("Dime el largo de un rectángulo: "));

ancho = float(input("Dime el ancho de un rectángulo: "));

area_rec = largo * ancho;

perimetro_rec = 2 *(largo+ancho);

print("El área del rectángulo es de: ", area_rec);

print("El perímetro del rectángulo es de: ",perimetro_rec);

#7. Radio de un círculo

radio = float(input("Dime el radio del círculo: "));

area_circ = round((math.pi * radio * radio),2);

circun_circ = round(2*math.pi*radio,2);

#Calcular el largo de 

largo1 = len("python");
largo2 = len("dragon");

print(largo2>largo1);


#imprimir en formato

tabla = print("""1 1 1 1 \n 2 1 2 4 8 \n 3 1 3 9 27 \n 4 1 4 16 64 \n 5 1 5 25 125""")
