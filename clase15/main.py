
def getColumn(t):
  line_start = INPUT.rfind('\n', 0, t.lexpos) + 1
  return (t.lexpos-line_start)+1

# Tokens

reserved = {
  'INICIO': 'reservada_inicio',
  'FIN': 'reservada_fin',
}

tokens = (
  'operador_suma',
  'operador_resta',
  'operador_multiplicacion',
  'operador_division',
  'operador_resto',
  'numero',
  'id',
) + tuple(reserved.values())

t_reservada_inicio = r'INICIO'
t_reservada_fin = r'FIN'
t_operador_suma = r'\+'
t_operador_resta = r'-'
t_operador_multiplicacion = r'\*'
t_operador_division = r'/'
t_operador_resto = r'%'
t_numero = r'\d+'

# Lexemas ignorados
t_ignore = ' \t\r\n'


def t_id(t):
  r'[a-zA-Z_][a-zA-Z_0-9]*'
  if t.value.upper() in reserved.keys(): t.type = reserved[t.value.upper()]
  return t

def t_newline(t):
  r'\n+'
  t.lexer.lineno+=len(t.value)

def t_error(t):
  print(t.lineno, getColumn(t), f"No se pudo reconocer el lexema '{t.value}'")
  t.lexer.skip(1)

precedence = (
  ('left','operador_suma','operador_resta'),
  ('left','operador_multiplicacion','operador_division','operador_resto')
)

"""
ASOCIATIVIDAD IZQUIERDA (left)
((5 + 5) + 5)
((5 ^ 5) ^ 5)

ASOCIATIVIDAD DERECHA (right)
(5 + (5 + 5))
(5 ^ (5 ^ 5))
"""

"""
p[0] : Lado izquierdo de la producción
p[1+] : Lado derecho de la producción

Lo que habrá en los elementos del lado derecho será:
- Un token si es un símbolo terminal
- Lo que regresemos de su producción si es un símbolo no terminal

Para retornar algo de una producción se debe asignar a p[0]
"""

# Producciones
def p_INITIAL(p):
  '''
  INITIAL : reservada_inicio EXPRESSIONS reservada_fin
  '''
  p[0] = p[2]

def p_EXPRESSIONS(p):
  '''
  EXPRESSIONS : EXPRESSIONS E
              | E
  '''
  if len(p)==3:
    p[0] = p[1]
    p[0].append(p[2])
  else:
    p[0] = [p[1]]

def p_E(p):
  '''
  E : E operador_suma E
    | E operador_resta E
    | E operador_multiplicacion E
    | E operador_division E
    | E operador_resto E
    | id
    | numero
  '''
  if len(p)==2:
    p[0] = {"linea": p.lexer.lineno, "columna": getColumn(p.lexer), "valor": p[1]}
  else:
    p[0] = {"linea": p.lexer.lineno, "columna": getColumn(p.lexer), "operacion": p[2], "izquierda": p[1], "derecha": p[3]}

def p_error(p):
  print(p)
  if p:
    print(f"Sintaxis no válida cerca de '{p.value}' ({p.type})")
  else:
    print("Ninguna instrucción válida")


from ply.yacc import yacc
from ply.lex import lex

lexer = lex()
parser = yacc(start='INITIAL')
# lexer.lex(reflags=re.IGNORECASE)  # case insensitive

INPUT = r'''
INICIO
5+6
56*9-5/2552
'''

ast = parser.parse(INPUT, lexer)

import json
print(json.dumps(ast, indent=4, sort_keys=False))
