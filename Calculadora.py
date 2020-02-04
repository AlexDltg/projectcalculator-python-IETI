# importando la libreria math
import math

# incializando la variable seleccion
seleccion = int(1)

# bucle general
while seleccion != 0:
    # seleccion, en bucle, por si se equivoca el usuario
    while (seleccion <= 1) or (seleccion >= 7):
        print("Menu:")
        print("1-> SUMA")
        print("2-> RESTA")
        print("3-> MULTIPLICACION")
        print("4-> POTENCIA")
        print("5-> RAIZ QUADRADA")
        print("6-> LOGARITMO")
        print("7-> TRIGONOMETRIA")
        print("0-> Cerrar Calculadora")
        seleccion = int(input())
        if (seleccion >= 1) or (seleccion <= 7):
            break

# relacionando el input (1-7) con las operaciones
    if seleccion == 1:
        print("Has seleccionado: SUMA")
    elif seleccion == 2:
        print("Has seleccionado: RESTA")
    elif seleccion == 3:
        print("Has seleccionado: MULTIPLICACION")
    elif seleccion == 4:
        print("Has seleccionado: POTENCIA")
    elif seleccion == 5:
        print("Has seleccionado: RAIZ QUADRADA")
    elif seleccion == 6:
        print("Has seleccionado: LOGARITMO")
    elif seleccion == 7:
        print("Has seleccionado: TRIGONOMETRIA")

# inicializar operaciones
    if seleccion == 1:  # suma
        num1 = float(input())
        num2 = float(input())
        print(num1 + num2)

    elif seleccion == 2:  # resta
        num1 = float(input())
        num2 = float(input())
        print(num1 - num2)

    elif seleccion == 3:  # multiplicacion
        num1 = float(input())
        num2 = float(input())
        print(num1 * num2)

    elif seleccion == 4:  # potencia
        num1 = float(input())
        num2 = float(input())
        print(num1 ** num2)

    elif seleccion == 5:  # raiz quadrada
        num1 = float(input())
        print(math.sqrt(num1))

    elif seleccion == 6:  # logaritmo
        num1 = float(input())
        num2 = float(input())
        print(math.log(num1[num2]))

    elif seleccion == 7:  # trigonometria
        selec = float(input(" 1 -> seno // 2 -> coseno // 3 -> tangente: "))
        if selec == 1:
            num = float(input())
            print(math.sin(math.pi / num))
        elif selec == 2:
            num = float(input())
            print(math.cos(math.pi / num))
        elif selec == 3:
            num = float(input())
            print(math.tan(math.pi / num))
