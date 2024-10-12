import random as rnd

LETTERS = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
            'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D',
            'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S',
            'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
NUMBERS = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
SYMBOLS = [ '_', '-', '@', '!', '#', '$', '%', '&', '(', ')', '*', '+']

def generateList(lista = None, cantidad=0)-> list:
    lista_nueva= list()
    if (not isinstance(lista, list)):
        raise TypeError("Tiene que ser tipo lista (list)")
    if lista:
        for _ in range(1, cantidad + 1):
            index = rnd.randint(0, len(lista)-1)
            lista_nueva.append(lista[index])
    return lista_nueva

def desordenarLista(lista= None):
    if (not isinstance(lista, list)):
        raise TypeError("Tiene que ser tipo lista (list)")
    if lista:
        for _ in range(len(lista)):
            index1 = rnd.randint(0, len(lista) -1)
            index2 = rnd.randint(0, len(lista)-1)
            aux = lista[index1]
            lista[index1] = lista[index2]
            lista[index2] = aux

if __name__ == "__main__":
    num_letters = int(input("Cuantas letras quieres: "))
    num_symbols = int(input("Cuantos simbolos quieres: "))
    num_numbers = int(input("Cuantos números quieres: "))
    
    password = list()
   
    letters = generateList(LETTERS, num_letters)
    symbols = generateList(SYMBOLS, num_symbols)
    numbers = generateList(NUMBERS, num_numbers)

    password.extend(letters)
    password.extend(symbols)
    password.extend(numbers)
    
    print(password)
    desordenarLista(password)
    print(f"Su contraseña es: {''.join(password)}")
