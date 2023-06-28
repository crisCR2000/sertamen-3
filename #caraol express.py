#caraol express


menu = print (""" menu
1. registrar_encomienda
2.buscar encomienda
3.lista encomienda
0.salir 

ingrese una opcion para continuar :
""") 


listanombres = []
listarut = []
listarutdestinatario = []
listapeso = []
listaprecio = []
listaciudad = []
listapaquete = []
listasobres = []
listanomdes = []

def registrar_encomienda():
    while True:
        try:
            rut = int(input("ingrese rut"))
            if rut > 0 :
                listarut.append(rut)
                break
            else:
                print("rut incorrecto")
                break
        except:
            print ("A OCURRIDO UN ERROR ")    #nombre
            
    while True:
        try:
            nombre = input("ingrese nombre ")
            if len(nombre) > 5: 
                listanombres.append(nombre)
                break
            else:
                print ("error nombre")
        except:
            print("a ocurrido una exepcion")
    while True:
        try:
            tipo = input("¿paquete o carta?")
            if tipo  == "carta":
                listasobres.append(tipo)
                break
            else:
                tipo == 'paquete'
                listapaquete.append(tipo)
                break
        except:
            print("ocurrio un error :o")
            break
    while True: # peso
        try:
            tipo == 'paquete'
            if peso == "si":
                peso  = int(input("ingrese el peso del envio"))
                peso > 2000 
                listapeso.append(peso)
                break

            else:
                tipo != 'paquete'
                peso == "no"
                break  
        except:
            print ("A OCURRIDO UN ERROR ")  
                  #nombre destinatario 
    while True:
        try:
            nombredes = input("ingrese nombre del destinatario ")
            if len(nombredes) > 20: 
               listanomdes.append(nombredes)
               break
            else:
                print ("error nombre")
                break
        except:
            print("a ocurrido una exepcion")
            break
    while True:
        try:
            destino = input("ingrese ciudad destino : ")
            if len(listaciudad) > 10: 
               listaciudad.append(destino)
               break
            else:
                print ("error nombre")
                break
        except:
            print("a ocurrido una exepcion")
            break
    while True:
        try:
            rutdes = int(input("ingrese rut del destinatario :"))
            if rutdes > 5 :
                listarutdestinatario.append(rutdes)
                break
            else:
                print("rut incorrecto")
                break
        except:
            print ("A OCURRIDO UN ERROR ") 

    
def lista_encomienda():
    for i in range (len(listarut)):
       print ("listado de encomiendas")
       print(f"{i+1},| {listarut[10]} |,{listanombres[20]},| {listanomdes[20]},|{listarutdestinatario[10]},|{listaciudad[20]},|{listapaquete[10]},|{listasobres[10]} ,")
        
def buscar_encomienda():
    nombre









while True:
    try:
        opc = int(input(menu))
        if opc == 0:
            break
        elif opc == 1:
            registrar_encomienda()
        elif opc == 2:
            buscar_comienda()
        elif opc == 3 :
            lista_encomienda()
    except:
        print("error :p")



