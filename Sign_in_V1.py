# username = input(f"INGRESAR NOMBRE DE USUARIO\n>>>")
password = input(f"INGRESAR CONTRASEÑA\n>>>")

# def accept_username(data):
#     for letras in data:
#         for numeros in range(0,10):
#             if letras == str(numeros):
#                 return 1
#     else:
#         return 0

def accept_sc(data):
    
    special_character = ["*","_","-","$"]
    for sc in special_character:
        for letras in data:
            if sc == letras:
               return 0
    else:
        return 1

def accept_cl(data):

     data_nsc = rsc(data)
     for cl in data_nsc.upper(): #capital letter -> cl
        for letras in data:
            if cl == letras:
                return 0
     else:
         return 1

def rsc(data): #remove special characters
    special_character = ["*","_","-","$"]
    for erase in special_character:
        data = data.strip(erase)
    return data

# while accept_username(username) == 1:
#     print("ERROR EL USUARIO NO DEBE CONTENER NUMEROS")
#     username = input(f"INGRESAR NOMBRE DE USUARIO\n>>>")

# else:
#     print("USUARIO VALIDO")

while accept_sc(password) == 1 or accept_cl(password) == 1: 
    
    print("ERROR DEBE CONTENER POR LO MENOS UN CARACTER ESPECIAL")
    password = input(f"INGRESAR CONTRASEÑA\n>>>")

else:
    print("CONTRASEÑA VALIDA")

    
    




