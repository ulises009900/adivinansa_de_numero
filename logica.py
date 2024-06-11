import random
numero_secreto = random.randint(1, 100)

def clave(password):

    has_space = False  
    has_upper = False 
    has_lower = False 
    has_digit = False 
    is_alnum = password.isalnum() 
    is_valid = True 
    

    for char in password: 
        if char.isspace(): 
            has_space = True 
        if char.isupper(): 
            has_upper = True 
        if char.islower(): 
            has_lower = True 
        if char.isdigit(): 
            has_digit = True 
    
    
    if has_space: 
        print("La contraseña no puede contener espacios")
        is_valid = False

    
    if len(password) < 8:
        print("Mínimo 8 caracteres")
        is_valid = False 

 
    if has_upper and has_lower and has_digit and not is_alnum:
        is_secure = True 
    else:
        is_secure = False 
    
   
    if is_valid and not is_secure:
        print("La contraseña elegida no es segura: debe contener letras minúsculas, mayúsculas, números y al menos 1 carácter no alfanumérico")
        is_valid = False

    return is_valid and is_secure


registros = []


def registrar_usuario():
    
    usuario = input("Introduce tu nombre de usuario: ")
    print(" debe contener letras minúsculas, mayúsculas, números y al menos 1 carácter no alfanumérico")
    
    password = input("Introduce tu contraseña: ")
    
    if clave(password):
        
        registros.append({'usuario': usuario, 'password': password})
        print("Usuario registrado con éxito")
    else:
        print("Registro fallido. La contraseña no cumple con los requisitos.")


registrar_usuario()


print("Registros almacenados:")
for registro in registros:
    print(registro)


eleccion=int(input("adivine el numero: "))
while (eleccion!=numero_secreto):
    if (eleccion >numero_secreto):
        eleccion=int(input("menos: "))
    else:
        eleccion=int(input("mas: "))
        

        
print(eleccion, " es correcto")

