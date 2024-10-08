def eleccionJuego():
    print("""
1) Piedra
2) Papel
3) Tijera
""")

def printMarcador(puntos_j1, puntos_j2):
    print("---------------------------------------------------------------")
    print("\tJugador 1: ", puntos_j1, "\t|\tJugador 2: ",puntos_j2)
    





if __name__ == "__main__":
    puntos_j1= 0
    puntos_j2= 0
    print("\n#########    PIEDRA PAPEL O TIJERAS      ########")
    print("\nElige una opcion: ")

    eleccionJuego()
    printMarcador(puntos_j1,puntos_j2)