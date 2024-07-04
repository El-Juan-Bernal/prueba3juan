from os import system
import random

system("cls")

pedidos=[]
sectores=["Concepción" "Chiguayante" "Talcahuano" "Hualpén" "San Pedro"]



def id_pedido():
    id=random.randint(100,200)
    pedidos.append(id_pedido)



def registro_de_pedido():
    while True:
        nombre=input("Ingrese su nombre: ")
        if len(nombre)>=3 and nombre.isalpha:
            break
        else:
            print("Nombre inválido")
        pedidos.append(nombre)

    while True:
        apellido=input("Ingrese su apellido: ")
        if len(apellido)>=3 and apellido.isalpha:
            break
        else:
            print("Apellido inválido")
        pedidos.append(apellido)

    while True:
        direccion=input("Ingrese su dirección: ")
        if len(direccion)>=4 and direccion.isalpha:
            break
        else:
            print("Dirección inválida")
        pedidos.append(direccion)

    while True:
        comuna=input("seleccione su comuna\n'Concepción' 'Chiguayante' 'Talcahuano' 'Hualpén' 'San Pedro' \n : ")
        if len(comuna)>=3 and comuna.isalpha:
            break
        else:
            print("Comuna no válida")
        pedidos.append(comuna)

    while True:
        dispensador=int(input("Seleccione su dispensador en litros '6' '10' '20'\n: "))
        if dispensador==6 or dispensador==10 or dispensador==20:
            break
        else:
            print("Opción no válida")
        pedidos.append(dispensador)


def listar_todos_los_pedidos():
    print("""
ID pedido                  Cliente               Dirección                 Comuna               Disp.6 lts.               Disp. 10 lts.              Disp. 20 lts.
""")
    for pedidos in pedidos:
        print=(f"""
{pedidos[0]}            {pedidos[1]}             {pedidos[2]}            {pedidos[3]}           {pedidos[4]}              {pedidos[5]}               {pedidos[6]}

        """)






while True:
    print("-"*30)
    print("Dispensadores Wacoldo SA")
    print("-"*30)
    print("""
    1. Registrar pedido
    2. Listar todos los pedidos
    3. Imprimir hoja de ruta
    4. Buscar un pedido por ID
    5. Salir del programa

    """)
    op= input("Seleccione una opción: ")
    match op:
        case "1":
            print("Registro de pedidos")

            registro_de_pedido()

        case "2":
            listar_todos_los_pedidos()

        case "3":
            break




