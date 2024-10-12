import random as rnd

LETTERS = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
            'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D',
            'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S',
            'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
NUMBERS = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
SYMBOLS = [ '_', '-', '@', '!', '#', '$', '%', '&', '(', ')', '*', '+']


if __name__ == "__main__":
    num_letters = int(input("Cuantas letras quieres: "))
    num_symbols = int(input("Cuantos simbolos quieres: "))
    num_numbers = int(input("Cuantos números quieres: "))
    
    password = list()
    # Con sample() cogemos valores sin que se repuitan
    # symbols = rnd.sample(SYMBOLS, num_symbols)
    # letters = rnd.sample(LETTERS, num_letters)
    # numbers = rnd.sample(NUMBERS, num_numbers)

    symbols = [rnd.choice(SYMBOLS) for _ in range(num_symbols)]
    letters = [rnd.choice(LETTERS) for _ in range(num_letters)]
    numbers = [rnd.choice(NUMBERS) for _ in range(num_numbers)]

    password.extend(letters)
    password.extend(symbols)
    password.extend(numbers)

    rnd.shuffle(password)
    print(f"Su contraseña es: {''.join(password)}")
