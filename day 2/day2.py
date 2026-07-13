#Funciones built-in, palabras reservadas, tales como: min(), input(), False...

#Ejemplo aportando una lista:
print("El resultado es: ", sum([20,30,40,50]));

"""Convención de variables:
-Deben empezar por una letra o guión bajo
-No puede empezar por un núero
-Tienen que ser descriptivos
-Solo puede contener caracteres alfanuméricos y guiones bajos
-Es case-sensitive
-Es recomendable usar la convención de nombres snake-case (en minúsculas todo y separado por un guión bajo si la palabra es compuesta)"""

#declaración compuesta de variables
nombre, edad, ganas = "Ari", 500, "muchas";

#Casting sirve para convertir "a la fuerza" a un tipo de dato
num_int = 10;
print("Num_int", num_int);
num_float = float(num_int);
print("Num_float", num_float);

#Ejercicios ------------------------
#1. Crear una carpeta con el día 2
#2. Comentar que es el día 2
#3. Declarar una variable y asignarle un valor
nombre = "Ari";

#4. Declarar un apellido
apellido = ".exe";

#5. Juntar ambos
nombre_completo = nombre+apellido;
print(nombre_completo);

#6. declarar un país
pais = "España";

#7. declarar una ciudad
ciudad ="Valencia";

#8. declarar una edad
edad = 500;

#9. declarar un año
year = 2026;

#10 declarar una variable is_married
is_married = "solter@";

#11. declarar is_true
is_true=True;

#12. declarar is_light_on
is_light_on = "lights off";

#13. Declarar múltiples variables en una línea

variables = is_married + " " + pais + " " + is_light_on;

print(variables, edad);

#nivel 2 -------------------
#1. comprobar el tipo de dato de las variables

print(type(pais), type(is_true));

#2. usar la función len()
print(len(apellido));

#3. comparar la longitud nombre + apellido
len1 = len(nombre);
len2 = len(apellido);

print("El nombre consta de: ", len1, "letras. El apellido consta de: ", len2, "letras");

#4. declarar el 5 como num1 y el 4 como num 2
num_1 = 5;
num_2 = 4;

#5. Sumarlos en una variable
suma = num_1+num_2;
print("La suma es de: ", suma);

#6. Restarlos
resta = num_1-num_2;
print("La resta es de: ", resta);

#7. Multiplicarlos
multi = num_1*num_2;
print("La multiplicación es de: ", multi);

#8. División
divi = num_1 / num_2;
print("La división es de: ", divi);

#9. resto módulo
resto = num_1 % num_2;
print("El resto módulo es de: ", resto);

#10. potencia
potencia = num_1 ** num_2;
print("La potencia es de: ", potencia);

#11. resto exacto
resto1 = num_1 // num_2;
print("El resto exacto es de: ", resto1);

help('keywords');