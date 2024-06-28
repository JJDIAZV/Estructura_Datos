# Ejercicios de estructura de datos

## PARTER 1

###EJERCICIO:
 ## - Muestra ejemplos de creación de todas las estructuras soportadas por defecto en tu lenguaje.
 ## - Utiliza operaciones de inserción, borrado, actualización y ordenación.

# Listas
My_List =  ["A", "B", "C", "D", "E", "F"]
print(My_List)

My_List.append("G") #Inserción
print(My_List)

My_List.remove("B") # Eliminación
print(My_List)

My_List[1] = "W"   # Actualización
print(My_List)

My_List.sort()  #Ordena de acuerdo valores de lista
print(My_List)
print(type(My_List))

# Tupla

my_tuple: tuple = ("JHON", "JAIRO", "DIAZ", "VASQUEZ", "36")
print(my_tuple[2]) #acceso
print(my_tuple[4])
my_tuple = sorted(my_tuple) ## cambiar a lista
print(type(my_tuple))


# sets 
# permite crear listas sin datos duplicados --- No estructurados

my_set = {"JULIAN", "DIAZ", "VERA", "11"}
print(my_set)
my_set.add("2013juliandiaz10@gmail.com")  #Inserción
print(my_set)
my_set.remove("VERA")  #Elimina
print(my_set)
print(type(my_set))


# Diccionario

my_dict: dict = {"NAME":"COLOMBIA",
                 "CONTINENTE": "SURAMERICA",
                 "VECINO1": "VENEZUELA"
                 }
print(my_dict)

my_dict["VECINO2"] = "PANAMA"    #Inserción
print(my_dict)
my_dict["NAME"] = "ECUADOR"  # Actualización
print(type(my_dict))

## PARTER 2



 # - Crea una agenda de contactos por terminal.
 # - Debes implementar funcionalidades de búsqueda, inserción, actualización y eliminación de contactos.
 # - Cada contacto debe tener un nombre y un número de teléfono.
 # - El programa solicita en primer lugar cuál es la operación que se quiere realizar, y a continuación
 #   los datos necesarios para llevarla a cabo.
 # - El programa no puede dejar introducir números de teléfono no númericos y con más de 10 dígitos.
 # - También se debe proponer una operación de finalización del programa.


def my_agenda():

    agenda = {}
    
    while True:

        print("")
        print("1. Buscar contacto")
        print("2. Insertar contacto")
        print("3. Actualizar contacto")
        print("4. Eliminar contacto")
        print("5. Salir")
      
        option = input("\nSelecciona una opcion: ")
        match option:
            case "1":
                name = input("Introduce el nombre del contacto a buscar buscar:")
                if name in agenda:
                    print(
                        f"El nemero de celular de {name} es {agenda[name]}.")
                else:
                    print(f"El contacto {name} No existe." )
                
            case "2":
                name = input("Introduce nombre de contacto:")
                No_Celular = input("introduce numero de celular de contacto:")
                if No_Celular.isdigit() and len(No_Celular) > 0 and len(No_Celular) <= 10:
                    agenda [name] = No_Celular
                else:
                    print("El numero de celular debe contener 10 digitos")           
          
            case "3":
                name = input("Introduce el nombre de contacto a actualizar:")
                if name in agenda:
                    No_Celular = input("introduce numero de celular de contacto a actualizar:")
                    if No_Celular.isdigit() and len(No_Celular) > 0 and len(No_Celular) <= 10:
                        agenda [name] = No_Celular
                    else:
                        print("El numero de celular debe contener 10 digitos") 
                else:
                    print(f"El contacto {name} no existe.")  

                       
            case "4":
                name = input("Introduce el nombre de contacto a eliminar:")
                if name in agenda:
                    del agenda[name]
                else:
                    print(f"El contacto {name} No existe." )
                        
            case "5":
                print("saliendo de la agenda.")
                break
    
            case _:
              print("opcion no valida, Elige una opcion del 1 al 5")

my_agenda()

