
def division(dividendo:float ,divisor:int=0)-> float:
    """
    Realiza una division entre un dividendo y un divisor, asegurando que ambos numeros sean validos y el resultado sea redondeado a dos decimales.

    Este metodo realiza una division entre el `dividendo` y el `divisor`, asegurandose de que:
    1. El `dividendo` sea un valor positivo.
    2. El `divisor` no sea negativo ni igual a cero, dado que la division entre cero es indefinida.

    Si alguna de estas condiciones no se cumple, se lanza una excepcion `ValueError` con un mensaje descriptivo.

    Args:
        dividendo (float): El numero a ser dividido. Debe ser mayor o igual a 0.
        divisor (int, opcional): El numero por el cual se dividira el dividendo. Debe ser mayor que 0. Valor por defecto es 0.

    Returns:
        float: El resultado de la division, redondeado a dos decimales.

    Raises:
        ValueError: Si el `dividendo` es negativo.
        ValueError: Si el `divisor` es negativo o igual a cero.

    Ejemplos:
        >>> division(10.0, 2)
        5.0

        >>> division(10.0, 3)
        3.33

        >>> division(-5.0, 2)
        ValueError: El dividendo no puede ser negativo

        >>> division(10.0, 0)
        ValueError: El divisor no puede ser negativo o cero
    """

    if dividendo < 0:
        raise ValueError("El dividendo no puede ser negativo")
    if divisor <=0:
        raise ValueError("El divisor no puede ser negativo o cero")
    return round(dividendo/divisor, 2)


def validarCuenta(monto:float=0)->float:
    """
    Realiza una validacion de la cuenta de un pedido, el dominion del monto debe ser mayor que 0.
    Args:
        monto (float): valor del monto a validar.
    Raises:
        ValueError: Si el valor de la cuenta es menor que cero.
    Return:
        El valor del monto validado redondeado a dos cifras (como el valor monetario)
    """
    if not type(monto) == int:
        monto = int(monto)
    if monto < 0:
        raise ValueError(f"El monto debe no puede ser menor que cero. Valor= {monto}")
    return round(monto, 2)

def validarNumeroPersona(numero_personas:int)->bool:
    if( isinstance(numero_personas, int) ):
        return numero_personas > 0
    return False



if __name__ == "__main__":
    print("\n\tCalculator Tip\n")
    monto= input("Inserte la cuenta a pagar: ")
    monto = validarCuenta(monto)
    
    is_personas_validada = False

    while not is_personas_validada:
        personas= int(input("\nIntroduzca el numero de personas: "))
        if validarNumeroPersona(personas):
            is_personas_validada = True
        else:
            print(f"El valor {personas} no es valido para el numero de personas\n")

    print((
        "Resumen:"
        f"\n\tCuenta:         {monto}€"
        f"\n\tPersonas:       {personas}"
        "\n\t-----------------------------------"
        f"\n\t€ por persona:  {division(monto, personas)}"
        "\nCuanta propina quereis dar? (minimo 5%)"
        "\nSugerencias de propina: 12, 15 ,20%"
    ))
    propina= float(input("\nIndique propina: ")) 
    while propina< 5:
        print("La propina minima es 5%.")
        propina= float(input("\nPor favor indique una propina: "))
    
    propina = propina*monto/100

    print((
    "\n\nResultado:"
    f"\n\tCuenta:         {monto}€"
    f"\n\tPersonas:       {personas}"
    f"\n\tPropina:        {propina}"
    "\n\t-----------------------------------"
    f"\n\t€ por persona:  {division(monto+propina, personas)}"
    ))
