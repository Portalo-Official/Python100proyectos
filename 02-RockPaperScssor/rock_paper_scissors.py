import random as rnd
PIEDRA = 1
PAPEL = 2
TIJERA = 3

def eleccionJuego():
    print(f"""
1) Piedra ({PIEDRA})
2) Papel ({PAPEL})
3) Tijera ({TIJERA})
""")

def printMarcador(puntos_j1, puntos_j2):
    print("---------------------------------------------------------------")
    print("\tJugador 1: ", puntos_j1, "\t|\tJugador 2: ",puntos_j2)
    
def get_mano(numero_mano=0)->str:
    # Mejorar en otra versiós con mas jugadas
    isValid=validar_mano(numero_mano) 
    mano="NO_HAND"
    if(numero_mano==PIEDRA):
        mano = """  
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""
    if(numero_mano==PAPEL):
        mano="""
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
"""
    if(numero_mano==TIJERA):
            mano="""
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""
    return mano

def get_puntos(mano1=0, mano2=0, puntos_j1=0 , puntos_j2=0):
    # Mejorar en otra versiós con mas jugadas
    isValid=validar_mano(mano1) and validar_mano(mano2)
    if(mano1==PIEDRA):
        if(mano2==PIEDRA):
            return puntos_j1, puntos_j2
        elif(mano2==PAPEL):
            return puntos_j1, puntos_j2+1
        return puntos_j1+1, puntos_j2
    elif(mano1==PAPEL):
        if(mano2==PIEDRA):
            return puntos_j1+1, puntos_j2
        elif(mano2==PAPEL):
            return puntos_j1, puntos_j2
        return puntos_j1, puntos_j2+1
    elif(mano1==TIJERA):
        if(mano2==PIEDRA):
            return puntos_j1, puntos_j2+1
        elif(mano2==PAPEL):
            return puntos_j1 +1, puntos_j2
        return puntos_j1, puntos_j2    
     

def validar_mano(mano=0)-> bool:
     if(0 > mano or mano > 3 ):
          raise ValueError("Los valores de entrada deben ser: 1 (Piedra), 2 (Papel), o 3 (Tijera)")
     return True    

if __name__ == "__main__":
    puntos_j1= 0
    puntos_j2= 0
    print("\n#########    PIEDRA PAPEL O TIJERAS      ########")
    print("\nElige una opcion: ")
    eleccionJuego()
    mano_jugador1= int(input())
    mano_jugador2= rnd.randint(1,3)
    puntos_j1, puntos_j2 =get_puntos(mano_jugador1, mano_jugador2, puntos_j1, puntos_j2 )
    print(get_mano(mano_jugador1))
    print(get_mano(mano_jugador2))
    printMarcador(puntos_j1,puntos_j2)