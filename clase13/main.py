from ply.yacc import yacc
from ply.lex import lex

def getColumn(t):
  line_start = INPUT.rfind('\n', 0, t.lexpos) + 1
  return (t.lexpos-line_start)+1

# Tokens

reserved = (
  'reservada_inicio',
  'reservada_fin'
)

tokens = reserved + (
  'operador_suma',
  'operador_resata',
  'operador_multiplicacion',
  'operador_division',
  'operador_igualacion',
  'operador_resto',
  'numero',
  'id',
)

t_reservada_inicio = r'INICIO'
t_reservada_fin = r'FIN'
t_operador_suma = r'\+'
t_operador_resata = r'-'
t_operador_multiplicacion = r'\*'
t_operador_division = r'/'
t_operador_resto = r'%'
t_numero = r'\d+'

# Lexemas ignorados
t_ignore = ' \t\r\n'


"""
  t:
    - lineno: numero de linea
    - value: valor del lexema
    - type: nombre del token
"""

def t_id(t): # t_id
  r'[a-zA-Z_][a-zA-Z_0-9]*'

  if t.value in reserved: t.type = t.value

  return t

def t_newline(t):
  r'\n+'
  t.lexer.lineno+=len(t.value)

def t_error(t):
  print(t.lineno, getColumn(t), f"No se pudo reconocer el lexema '{t.value}'")
  t.lexer.skip(1)

lexer = lex()

INPUT = r'''
INICIO
56*9-5/2552
FIN
'''

lexer.input(INPUT)

for tok in lexer:
  print(tok)
