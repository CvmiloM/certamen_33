import os
os.system("cls")

listacodigo = []
listanombre = []
listacategoria = []
listaprecio = []
listacantidad = []

menu = '''
#######Menu######### 
1)Registrar productos
2)Buscar producto
3)Listar porductos
4)Salir
####################
Digite opcion: '''


def busquedaP ():
    print("Opcion 2")
    codigo = input("Ingrese Codigo Para Buscar producto")
    print(f"listado segundo: {codigo} ")
    print("ID|NOMBRE|CATEGORIA|PRECIO|CANTIDAD|STOCK")
    print("-------------------------------------------------------------------------")
    for i in range(len(listacodigo)):
        if listacodigo[i]():
             print(f"{listacodigo[i]:6d}|{listanombre[i]:50s}|{listacategoria[i]:30s}|{listaprecio[i]:10d}|{listacantidad[i]: 6d |{stock}}")
             print("-------------------------------------------------------------------------")




def listadoP ():
    print("Opcion 3")
    print("Listado General")
    print("ID|NOMBRE|CATEGORIA|PRECIO|CANTIDAD|STOCK")
    cant = 0
    for i in range (len(listacodigo)):
        if listacantidad[i] < 5:
            stock = "Si"
            cant += 1
        else:
            stock = "No"
    print("-------------------------------------------------------------------------")
    print(f"{listacodigo[i]:6d}|{listanombre[i]:50s}|{listacategoria[i]:30s}|{listaprecio[i]:10d}|{listacantidad[i]: 6d |{stock}}")
    print("-------------------------------------------------------------------------")




def registroP ():
    
            while True:
                try:
                    codigo = int(input("Ingrese codigo: "))
                    if len(str(codigo)) < 6 or len(str(codigo)) > 6:
                        print("No valido")
                    else:
                        listacodigo.append (codigo)
                        break
                except:
                    print("Ocurrio una expecion")
                    break 
                   
            while True:
                try:
                    nombre = input("Ingrese el nombre: ")
                    if len(str(nombre)) < 2 or len(str(nombre)) > 50:
                        print("No valido")
                    else:
                        listanombre.append(nombre)
                        break
                except:
                    print("Ocurrio una expecion")
                    break

            while True:
                try:
                    print("Tiene para elegir entre Paquete o Sobre")
                    categoria = input("Ingrese categoria: ")
                    if categoria == "Paquete" or categoria == "Sobre":
                       listacategoria.append(categoria)
                    break
                except:
                    print("Ocurrio una expecion")
                    break

            while True:
                try:
                    precio = int(input("Coloque precio: "))
                    if len(str(precio)) > 0:
                       listaprecio.append(precio)
                       break
                except:
                    print("Ocurrio una expecion")
                    break
                    
            
            while True:
                try:
                    stock = int(input("Cantidad de stock: "))
                    if stock >= 0:
                       listacantidad.append(stock)
                       break
                    elif stock < 0 or float:
                        print("Error")
                except:
                    print("Ocurrio una expecion")
                    

while True:
    try:
        opc = int(input(menu))
        if opc == 4:
            break
        elif opc == 1:
            registroT()
        elif opc == 2:
            busquedaT()
        elif opc == 3:
            listadoT()
    except:
        print("Ocurrio una excepcion")