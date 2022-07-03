
global date
date = ""
def accept_username(data):
    for letras in data:
        for numeros in range(0,10):
            if letras == str(numeros):
                return 1
    else:
        return 0

def accept_password(data):
    
    special_character = ["*","_","-","$"]
    for sc in special_character:
        for letras in data:
            if sc == letras:
                for l in data:
                    for numeros in range(0,10):
                        if l == str(numeros):
                            for erase in special_character:
                                data = data.strip(erase)
                                for cl in data.upper(): #capital letter -> cl
                                    for letras in data:
                                        if cl == letras:
                                            return 0
    else:
        return 1

def accept_date(date):
    find_okey = date.find("-")
    if find_okey != -1:
     
        date_aux = date.split("-")
        dia = date_aux[0]
        mes = date_aux[1]
        año = date_aux[2]
    else:
        return 1

def change_username():
    global username
    username = input(f"Ingresar Nombre de Usuario\n>>>")
    while accept_username(username) == 1:
      
        print("""El usuario no puede contener:
                 1)_Numeros""")
        username = input(f"INGRESAR NOMBRE DE USUARIO\n>>>")
    else:
      print("USUARIO VALIDO")
      return username

def change_password():
    global password
    password = input(f"Ingresar Contraseña\n>>>")
    while accept_password(password) == 1: 
    
        print("""La contraseña debe contener al menos:
                1)_Un caracter especial
                2)_Una letra mayuscula
                3)_Un numero""")

        password = input(f"INGRESAR CONTRASEÑA\n>>>")
    else:
        print("CONTRASEÑA VALIDA")
        
def change_date():

    global date
    date = input(f"Ingresar Fecha de nacimiento 'dia-mes-año' \n>>>")
    while accept_date(date) == 1: 
        print("""La Fecha debe contener al menos:
                1)_Separacion con -
                2)_rango correcto dias/mes/año""")
        date = input(f"INGRESAR FECHA\n>>>")
    else:
        print("FECHA VALIDA")

def change_function(function):
    if function == 1:
        change_username()
    elif function == 2:
        change_password()
    elif function == 3:
        change_date()
    elif function == 4:
        pass
        #change_dni()

def menu():
    while True:
     
     selection = input("""Seleccione el número correspondiente a la opción:
            1)_Usuario
            2)_Contraseña
            3)_Fecha de nacimiento
            4)_DNI
            5)_Cerrar sesion
            >>>>""")
   
     options = {'1':["Su nombre es:",username,1],'2':["La contraseña es:",password,2],'3':["La Fecha de nacimiento es:",date,3]}

     if selection in options:

        while True:
            selection2 = int(input("""Que quieres hacer:
                     1)_Cambiar
                     2)_Ver
                     3)_Atras
                     >>>>"""))

            if selection2 == 1:
                change_function(options[selection][2])
                print("CAMBIO EXITOSO!!!")
                break
            elif selection2 == 2:
                print(f"{options[selection][0]} {options[selection][1]}")
            elif selection2 == 3:
                break
     else:
         print("Opcion invalida")

    
change_username()
change_password()
menu()



    
    


            
    
    


