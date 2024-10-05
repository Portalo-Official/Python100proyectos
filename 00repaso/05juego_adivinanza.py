import random

def generar_numero(min_val=1, max_val=100)-> int:
    """Genera un número aleatorio entre min_val y max_val."""
    return random.randint(min_val, max_val)

def obtener_intentos(max_intentos:int=10)->int:
    """Obtiene la cantidad de intentos permitidos del usuario"""
    while True:
        try:
            intentos = int(input(f"¿Cuantos intentos deseas? (1-{max_intentos}): "))

            if 1<= intentos <= max_intentos:
                return intentos
            else:
                print("Error.\nMotivo: has introducido un número negativo.\nMensaje: Por favor introduzca un numero entero")
        except ValueError:
            print("Error.\nMotivo: No has introducido un número.\nMensaje: Por favor introduzca un numero entero")

def jugar(intentos:int):
    numero_sercreto = generar_numero()
    print(f"Se ha generado un numero secreo {numero_sercreto}")

    while 0 < intentos or resultado == numero_sercreto:
        print(f"Intetos: {intentos}")
        try:
            resultado = int(input("Introduzca un numero: "))

            if(resultado > numero_sercreto):
                print("El numero secreto es más pequeño")
            elif (resultado < numero_sercreto):
                print("El numero secreto es más grande")
            else:
                print("Felicidades , has acertado!")
                return 1

            intentos -=1
        except ValueError:
            print("Error.\nMotivo: No has introducido un número.\nMensaje: Por favor introduzca un numero entero")
        print("\n--------------------\n")
    
    else:
        print("Has agotado todos tus intentos")


if __name__ == "__main__":
    jugar(obtener_intentos(15))