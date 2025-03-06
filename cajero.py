#Cajero 



Usuario = list()
Usuario.append("JacintoCortez") 
Usuario.append("4321")
Usuario.append(1000)

reciboLista = list()
reciboLista.append(["123",1000])
reciboLista.append(["124",2000])
reciboLista.append(["125",3000])
reciboLista.append(["126",4000])
reciboLista.append(["127",5000])

acciones= list()
acciones.append("depositar")
acciones.append("retirar")
acciones.append("pagos de recibos")

Usuario2 = list()
Usuario2.append("rosalioSerrano")
Usuario2.append("1234")
Usuario2.append(2000)

def registro():
    lista = list()
    user = input("ingrese su usuario:")
    password = input("ingrese su contraseña:")
    
    lista.append(user)
    lista.append(password)  
    
    if Usuario[0] == user and Usuario[1] == password:
        print("Bienvenido")
        return lista
    else:
        print("su usuario o contraseña son incorrectos")
        return None

def oportunidad():
    intentos = 0
    while intentos < 3:
        print("intento:", 3 - intentos)
        esValido = registro()
        if esValido:
            return esValido
        else:
            intentos += 1
    return None

def operacion():
    seleccion = list()
    print("Seleccione la operacion que desea realizar")
    print("1.- Depositar")
    print("2.- Retirar")
    print("3.- Pago de recibos")
    
    seleccion.append(input("Seleccione la operacion que desea realizar:"))
    
    if seleccion[0] == "1":
        print("Depositar")
        cantidadOperaciones = input("ingrese la cantidad a depositar:")
        seleccion.append(cantidadOperaciones)
        
    elif seleccion[0] == "2":
        print("Retirar")
        cantidadOperaciones = input("ingrese la cantidad a retirar:")
        seleccion.append(cantidadOperaciones)
        
    elif seleccion[0] == "3":
        print("Pago de recibos")
        cantidadOperaciones = input("ingrese la cantidad a pagar:")
        seleccion.append(cantidadOperaciones)
        
    else:
        print("esa opcion no es valida")
        
    return seleccion

def retiro():
    saldo = operacion()
    if int(saldo[1]) <= Usuario[2]:
        Usuario[2] = Usuario[2] - int(saldo[1])
        print("Retiro exitoso")
        print("Saldo actual: ", Usuario[2])
        return True
    else:
        print("la cantidad no es admitida")
        return False

def deposito():
    saldo = operacion()
    if int(saldo[1]) > 0:
        Usuario[2] = Usuario[2] + int(saldo[1])
        print("Deposito exitoso")
        print("Saldo actual: ", Usuario[2])
    else:
        print("Cantidad no admitida")

def pagoRecibo():
    op = operacion()
    for i in range(len(reciboLista)):
        if reciboLista[i][0] == op[1]:
            ingresarMonto = float(input(f"pago de NIC :{reciboLista[i][0]}, ingrese el monto a pagar: "))
            if ingresarMonto <= Usuario[2]:
                Usuario[2] = Usuario[2] - ingresarMonto
                print("pago exitoso")
                print("saldo actual:", Usuario[2])
                return True
            else:
                print("el pago no se puede realizar")
                print("saldo actual:", Usuario[2])
                return False
    print("Recibo no encontrado")
    return False