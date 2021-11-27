# Bucles [Python]
# Ejercicios de profundización

# Autor: Inove Coding School
# Version: 2.0

# NOTA: 
# Estos ejercicios son de mayor dificultad que los de clase y práctica.
# Están pensados para aquellos con conocimientos previo o que dispongan
# de mucho más tiempo para abordar estos temas por su cuenta.
# Requiere mayor tiempo de dedicación e investigación autodidacta.

# IMPORTANTE: NO borrar los comentarios en VERDE o NARANJA

'''
Enunciado:
Realice una calculadora:
Dentro de un bucle se debe ingresar por línea de comando dos números
Luego se ingresará como tercera entrada al programa el símbolo de la operación
que se desea ejecutar:
- Suma (+)
- Resta (-)
- Multiplicación (*)
- División (/)
- Exponente/Potencia (**)
Se debe efectuar el cálculo correcto según la operación ingresada por consola
Imprimir en pantalla la operación realizada y el resultado

El programa se debe repetir dentro del bucle hasta que como operador
se ingrese la palabra "FIN", en ese momento debe terminar el programa

Se debe debe imprimir un cartel de error si el operador ingresado no es
alguno de lo soportados o no es la palabra "FIN".
'''

print("Mi Calculadora (^_^)")
# Empezar aquí la resolución del ejercicio

palabra_final = ' '

while palabra_final != 'FIN':
    numero_1 = float(input('Ingrese el primer numero: '))
    numero_2 = float(input('Ingrese el segundo numero: '))
    operacion = str(input('Ingrese la operacion que desa realizar: '))
    
    if operacion == '+':
        suma = numero_1 + numero_2
        print('Operacion: +    La SUMA es ', suma)
        

    elif operacion == '-':
        resta = numero_1 - numero_2
        print('Operacion: -    La RESTA es ', resta)
        

    elif operacion == '*':
        multiplicacion = numero_1 * numero_2
        print('Operacion: *    El PRODUCTO da ', multiplicacion)
        

    elif operacion == '/':
        division = numero_1 / numero_2
        print('Operacion: /    La DIVISION da ', division)

    elif operacion == '**':
        potencia = numero_1 ** numero_2
        print('Operacion: **   La POTENCIA da', potencia)
        
    #palabra_final = str(input()) ---> Linea innecesaria

    else:
        print('Error. Simbolo incorrecto...')

    print('Ingrese la palabra FIN para finalizar la operacion o cualquier otra palabra para realizar otro calculo...')
    palabra_final = str(input())

    