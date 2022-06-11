# Ejemplo de debugging en Python

digito=["0","1","2","3","4","5","6","7","8","9"]
letra=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","ñ","o","p","q","r","s","t","u","v","w","x","y","z"]

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

print(AFDIdentificador("a875"))
