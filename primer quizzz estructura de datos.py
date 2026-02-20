habitaciones=[101,102,103,104,105]
huespedes={}
orden_llegada=[]
libro_salidas=[]

def registrar_huesped():
    cedula=input("Ingrese cedula:")
    if cedula in huespedes:
        print("El huesped ya esta registrado")
        return
    nombre=input("Ingrese nombre: ")
    habitacion=int(input("Ingrese numero de habitacion: " ))
    
    if habitacion not in habitaciones:
        print("La habitacion no existe")
        return
    huespedes[cedula]={"nombre": nombre, "habitacion": habitacion}
    orden_llegada.append(cedula)
    print("Huesped registrado exitosamente")

def retirar_huesped():
        cedula=input("Ingrese cedula del huesped que se retira: ")
        if cedula not in huespedes:
         print("Huesped no encontrado")
         return   
        libro_salidas.append(huespedes[cedula])
        del huespedes[cedula] 
        print("Huesped retirado correctamente")

def consulta_individual():
        cedula=input("Ingrese cedula del huesped a consultar:")

        if cedula in huespedes:
            print("Nombre:", huespedes[cedula]["nombre"])
            print("Habitacion: ", huespedes[cedula]["habitacion"])
        else:
            print("Huesped no encontrado")

def consulta_general():
        for cedula in sorted(huespedes):
            print("Cedula: ", cedula)
            print("Nombre:", huespedes[cedula]["nombre"])
            print("Habitacion: ", huespedes[cedula]["habitacion"])
    
def consulta_orden_llegada():
        for cedula in orden_llegada:
            if cedula in huespedes:
                print("Cedula:", cedula)
                print("Nombre: ", huespedes[cedula]["nombre"])
                print("Habitacion: ", huespedes[cedula]["habitacion"])
def habitaciones_ocupadas():
        ocupadas=[]
        for cedula in huespedes:
            ocupadas.append(huespedes[cedula]["habitacion"])
        print("Habitaciones ocupadas: ", ocupadas)
def habitaciones_disponibles():
        ocupadas=[]
        for cedula in huespedes:
            ocupadas.append(huespedes[cedula]["habitacion"])
        print("Habitaciones disponibles: ")
        for hab in habitaciones:
            if hab not in ocupadas:
                print(hab)
while True:
    print("1. Registrar huesped")
    print("2. Retirar huesped")
    print("3. Consulta individual")
    print("4. Consulta general por cedula")
    print("5. Consulta general por orden de llegada")
    print("6. Habitaciones ocupadas")
    print("7. Habitaciones disponibles")
    print("8. Salir")

    opcion=int(input("Seleccione una opcion: "))

    if opcion==1:
        registrar_huesped()
    elif opcion==2:
        retirar_huesped()
    elif opcion==3:
        consulta_individual()
    elif opcion==4:
        consulta_general()
    elif opcion==5:
        consulta_orden_llegada()
    elif opcion==6:
        habitaciones_ocupadas()
    elif opcion==7:
        habitaciones_disponibles()
    elif opcion==8:
        print("Saliendo del programa...")
        break
    else:
        print("Opcion no valida, intente nuevamente")
    
       