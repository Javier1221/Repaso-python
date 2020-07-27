import procedimientos as llamado
import os
if __name__ == "__main__":
    menu=0
    while(menu!=11):
        print("\n\n")
        print("          ----Problemas de Repaso----       ")
        print("______________________________________________")
        print("| 1-Repetición de Palabra 10 veces           |")
        print("| 2-Numeros impares hasta el numero ingresado|")
        print("| 3-Saludo Hola                              |")
        print("| 4- Saludo con nombre                       |")
        print("| 5-Area de círculo y cilindro               |")
        print("| 6-Media de una lista de numeros            |")
        print("| 7-Edad del usuario                         |")
        print("| 8-Comparación de Contraseñas               |")
        print("| 9-Division de numeros                      |")
        print("| 10-Numero que es par o impar               |")
        print("| 11-Salir                                   |")
        print("______________________________________________")
        menu=int(input("Ingrese el numero ="))
        if menu==1:
            llamado.p1()
        elif menu==2:
            llamado.p2()
        elif menu==3:
            llamado.p3()
        elif menu==4:
            os.system("cls")
            print(" Opción 4 ")
            nombre=input("Ingrese un nombre : ")
            llamado.p4(nombre)
        elif menu==5:
            llamado.p5()
        elif menu==6:
            print(" Opción 6 ")
            os.system("cls")
            cantidad=int(input("Ingrese la cantidad de numeros que agregara en la lista: "))
            lista=[]
            for i in range(0,cantidad):
                numero=int(input("Ingrese el valor "+str(i+1)+" de la lista :"))
                lista.append(numero)
            llamado.p6(lista)
        elif menu==7:
            llamado.p7()
        elif menu==8:
            #La contraseña es hola mundo
            llamado.p8()
        elif menu==9:
            llamado.p9()
        elif menu==10:
            llamado.p10()
        elif menu==11:
            os.system("cls")
            print("Gracias por Paricipar")