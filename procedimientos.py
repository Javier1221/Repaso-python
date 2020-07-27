import math
import os
def p1():
    os.system("cls")
    print(" Opción 1 ")
    palabra=""
    palabra=input("Ingrese una palabra ")
    for i in range(0,10):
        print(palabra)
#///////////////////////////////////////////////////
def p2():
    os.system("cls")
    print(" Opción 2 ")
    numero=0
    numero=int(input("Ingrese un número entero positivo: "))
    for i in range(1,numero+1):
        if i%2!=0:
            print(i)
#///////////////////////////////////////////////////
def p3():
    os.system("cls")
    print(" Opción 3 ")
    print("!Hola Amiga!")
#///////////////////////////////////////////////////
def p4(nombre):
    print("Hola "+nombre)

#///////////////////////////////////////////////////
def p5():
    os.system("cls")
    print(" Opción 5 ")
    radio=0
    altura=0
    v_cilindro=0
    area_circulo=0
    radio=float(input("Ingrese el radio: "))
    altura=float(input("Ingrese la altura: "))
    area_circulo=area(radio)
    print("El area del círculo  es:{:.2f}".format(area_circulo))
    v_cilindro=area_circulo*altura
    print("El Volumen del cílindro  es:{:.2f}".format(v_cilindro))

def area(radio):
    return math.pi * (radio**2)

#///////////////////////////////////////////////////
def p6(lista_numeros):
    sumatoria=0
    media=0
    for i in range(0,len(lista_numeros)):
        sumatoria+=lista_numeros[i]
    media=sumatoria/len(lista_numeros)
    print("La media de los datos ingresados es :{:.2f}".format(media))


#///////////////////////////////////////////////////
def p7():
    os.system("cls")
    print(" Opción 7 ")
    edad=0
    edad=int(input("Por favor ingrese su edad "))
    if edad<18:
        print(" Oh eres menor de edad")
    else:
        print("Oh que bien ya eres mayor de edad ")
#///////////////////////////////////////////////////
def p8():
    os.system("cls")
    print(" Opción 8 ")
    contraseña="hola mundo"
    contraseña_usuario=""
    contraseña_usuario=input("Ingrese la contraseña ")
    contraseña_usuario=contraseña_usuario.lower()
    if(contraseña==contraseña_usuario):
        print("Contraseña correcta ")
    else:
        print("Contraseña incorrecta ")

#///////////////////////////////////////////////////
def p9():
    os.system("cls")
    print(" Opción 9 ")
    validacion=False
    while(validacion != True):
        numerador=float(input("Ingrese el numerador :"))
        denominador=float(input("Ingrese el denominador :"))
        try:
            division=numerador/denominador
            print("La división es :{:.2f}".format(division))
            validacion=True
        except ZeroDivisionError:
            print("Ups parece que tu divisor es 0...")
            print("Nuevamente ")
            validacion=False
#///////////////////////////////////////////////////
def p10():
    os.system("cls")
    print(" Opción 10 ")
    numero=int(input("Ingrese un numero entero "))
    if numero%2==0:
        print("El número ingresado es par")
    else:
        print("El número ingresado es impar")

