user_ok="dhardy"
clave_ok=1234
numeros = []  # Usamos una lista para 14 numeros
numeros2 = []# lista para algunos numeros
cantidad = 14
import random

def usuario():
      intentos=0
      
      while intentos<3:
            try:
                  usuario=input("Ingrese su usuario:")
                  clave=int(input("Ingrese su contraseña que es su rut sin digito verificador:"))
                  intentos+=1
                  if usuario == user_ok and clave == clave_ok:
                        print("Usuario y contraseña correcta")
                        mostrar_menu()
                  if usuario != user_ok and clave == clave_ok:
                        print("\nUsuario Incorrecto")
                  if usuario == user_ok and clave != clave_ok:
                        print("\nContraseña Incorrecta")
                  if intentos==3:
                        print("Demasiados Intentos") 
                        break
                  if usuario != user_ok and clave!= clave_ok:
                        print("\nAcceso denegado - usuario o clave incorrecta")
            except ValueError:
                        ("Error Ingrese un dato correcto")

      
def mostrar_menu():

      op1 = 0      
      while op1 != 4:
            print()
            print("╔════════════════════════════╗")
            print("║     === MENU KINO ===      ║")
            print("╠════════════════════════════╣")
            print("║1. Jugar                    ║")
            print("╠════════════════════════════╣")
            print("║2. Ver Resultados           ║")
            print("╠════════════════════════════╣")
            print("║3. Estadisticas             ║")
            print("╠════════════════════════════╣")
            print("║4. Salir                    ║")
            print("╚════════════════════════════╝")
            try:
                  op1 = int(input("Ingrese una opción: "))
            except ValueError:
                  print("Error Ingrese un dato correcto") #MANEJO DE ERROR EN CASO DE QUE EL USUARIO INGRESE UN VALOR NO NUMERICO
            
      #SI EL USUARIO ELIGE LA OPCION 1 INGRESA A JUGAR EL KINO
            if op1 == 1:
                  op2 = 0
                  while op2 != 4:
                   print()
                   print("╔════════════════════════════╗")
                   print("║       === JUGAR ===        ║")
                   print("╠════════════════════════════╣")
                   print("║1. Escoge 14 Números        ║")
                   print("╠════════════════════════════╣")
                   print("║2. Escoge algunos Números   ║")
                   print("╠════════════════════════════╣")
                   print("║3. Números al azar          ║")
                   print("╠════════════════════════════╣")
                   print("║4. Salir                    ║")
                   print("╚════════════════════════════╝")
                   try:
                        op2 = int(input("Ingrese una opción: "))
                   except ValueError:
                        print("Error Ingrese un dato correcto")

                   if op2==1:
                         N14()
                   if op2==2:
                        ean()


def N14(): #escoger 14 numeros
    if len(numeros) == 0:
         print("Ingresa 14 números distintos entre 1 y 25:")

    while len(numeros) < cantidad:
        try:
            numero = int(input(f"Número {len(numeros) + 1}: "))
            if 1 <= numero <= 25:
                if numero in numeros:
                    print("Número ya ingresado, intenta con otro.")
                else:
                    numeros.append(numero)
            else:
                print("El número debe estar entre 1 y 25.")
        except ValueError:
            print("Por favor, ingresa un número válido.")
            
    print("\nHas ingresado los 14 números correctamente.")
    print("\nNúmeros seleccionados:", numeros)
    mostrar_menu()      


def ean():  # Escoger algunos números
    if len(numeros2) == 0:         
               
                  try:
                        cant_escoger = int(input("¿Cuántos números deseas escoger? (Máximo 13): "))
                        
                        if cant_escoger > cantidad or cant_escoger <= 0:
                              print("Debes ingresar un número entre 1 y 14.")
                              return  # Salimos de la función si el número ingresado es inválido

                        for i in range(cant_escoger):
                              while True:  # Asegura que el usuario ingrese un número válido
                                    try:
                                          numero = int(input(f"Ingrese el número {i + 1}: "))
                                          if 1 <= numero <= 25:
                                                if numero in numeros2:
                                                      print("Número ya ingresado, intenta con otro.")
                                                else:
                                                      numeros2.append(numero)
                                                      break  # Salimos del bucle si es válido
                                          else:
                                                print("El número debe estar entre 1 y 25.")
                                    except ValueError:
                                     print("Error: Ingresa un número válido.")
                        
                        # Generar números al azar para completar hasta `cantidad`
                        while len(numeros2) < cantidad:
                              num_aleatorio = random.randint(1, 25)
                              if num_aleatorio not in numeros2:
                                    numeros2.append(num_aleatorio)
                        
                        print("\nNúmeros seleccionados:", numeros2)
                        mostrar_menu()
                        
                  except ValueError:
                        print("Error: Ingresa un número válido.")
    else:
          print("Ya ingresaste tus numeros")

                        

            

