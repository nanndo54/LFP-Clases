# Ejemplo de implementación de un analizador léxico

# LENGUAJE

'''
  # Sintaxis de un lenguaje de operaciones aritméticas

  ## Generalidades
  El lenguaje será case sensitive

  El código fuente debe empezar con el lexema "INICIO"
  El código fuente debe terminar con el lexema "FIN"

  ## Operaciones
  Las operaciones se deben dividir por líneas
  Las operaciones soportadas son

  | Operación      | Operador |
  | :------------: | :------: |
  | Suma           |    +     |
  | Resta          |    -     |
  | Multiplicación |    *     |
  | División       |    /     |
  | Resto          |    %     |

  ## Operandos
  Se operarán números enteros sin signo
'''

# IMPLEMENTACIÓN

import os

digito=["0","1","2","3","4","5","6","7","8","9"]

# AFD

def AFDNumero(lexema):
    estado=0
    estados_aceptacion = [1]

    for char in lexema:
        if estado==0:
            if char in digito:
                estado=1

            else:
                estado=-1

        elif estado==1:

            if char in digito:
                estado=1

            else:
                estado=-1

        if estado==-1:
            return False

    return estado in estados_aceptacion

def AFDIdentificador(lexema):
    '''
      [a-zA-Z_][a-zA-Z0-9_]*
    '''
    estado=0
    estados_aceptacion = [1]

    for caracter in lexema:
        if estado==0:
            if caracter == "_" or caracter in letra:
                estado=1

            else:
                estado=-1

        elif estado==1:
            if caracter == "_" or caracter in letra or caracter in digito:
                estado=1

            else:
                estado=-1

        if estado==-1:
            return False

    return estado in estados_aceptacion


# Tokens

tokens = {
  "tk_reservada_inicio": "INICIO",
  "tk_reservada_fin": "FIN",
  "tk_operador_suma": "+",
  "tk_operador_resta": "-",
  "tk_operador_multiplicacion": "*",
  "tk_operador_division": "/",
  "tk_operador_resto": "%",
  "tk_operador_igualacion": "==",
  "tk_operador_asignacion": "=",
  "tk_operador_resto": "%",
  "tk_numero_double": AFDNumeroDouble
  "tk_numero": AFDNumero
}

IGNORAR = " \n\t"

def AnalizadorLexico(codigo):
    linea, columna = 1, 0
    indice = 0

    while indice < len(codigo):
        caracter = codigo[indice]
        reconocido = False

        # Conteo de líneas
        if caracter=="\n":
            linea+=1
            columna=0

        columna+=1

        caracter_impresion = caracter
        if caracter_impresion == '\n': caracter_impresion = '\\n'

        print(f"[{linea},{columna}] CARACTER: '{caracter_impresion}'")

        # Caracteres a ignorar
        if caracter in IGNORAR:
            print("IGNORANDO")
            indice += 1
            continue

        for token, patron in tokens.items():
            if isinstance(patron, str):
                if indice + len(patron) > len(codigo): continue

                lexema = codigo[indice : indice + len(patron)]

                if lexema == patron:
                    reconocido = True
                    indice += len(patron)
                    columna += len(patron)
                    print(f"RECONOCIDO: '{lexema}' | {token} - {patron}")

            else: # AFD
                indice_adelante = indice + 1
                anterior_reconocido = False

                while indice_adelante <= len(codigo) and codigo[indice_adelante - 1] != '\n':
                    lexema = codigo[indice : indice_adelante]
                    reconocido = patron(lexema)

                    if not reconocido and anterior_reconocido:
                        lexema = codigo[indice : indice_adelante - 1]
                        reconocido = True
                        indice = indice_adelante - 1
                        break

                    anterior_reconocido = reconocido
                    indice_adelante += 1

                if reconocido:
                    print(f"RECONOCIDO: '{lexema}' | {token} - AFD")
                    columna += indice_adelante - indice + 1
                    indice = indice_adelante - 1

            if reconocido: break

        if not reconocido:
            indice += 1
            print("ERROR LEXICO")


def Aplicacion():
    salir=False

    while not salir:
        print(
'''
~~~~~~~~~~~~~~~~~~
  EJEMPLO LFP-VJ
~~~~~~~~~~~~~~~~~~

1. Analisis Lexico

2. Salir del programa
'''
        )

        opcion=input(">> ")

        if opcion=="1":
          directorio=input("Ingrese el directorio del archivo (" + os.getcwd() + ")\n")

          try:
            archivo=open(directorio, encoding="utf8").read()
            AnalizadorLexico(archivo)

          except:
              print("\nArchivo no encontrado\n")

        elif opcion=="2":
            print(""".\n..\n...""")
            salir=True

        else:
            if opcion:
                print("Opción no reconocida")


Aplicacion()

# AnalizadorLexico("""
# INICIO
# 2+78
# 3*5-4
# FIN
# """)

# print(AFDNumero("abc"))
# print(AFDNumero("a"))



