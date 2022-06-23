- [1. Gramática de Simple MAT](#1-gramática-de-simple-mat)
  - [1.1. Alfabeto](#11-alfabeto)
    - [1.1.1. Símbolos terminales](#111-símbolos-terminales)
      - [1.1.1.1. Expresiones regulares](#1111-expresiones-regulares)
      - [1.1.1.2. Palabras reservadas](#1112-palabras-reservadas)
    - [1.1.2. Símbolos no terminales](#112-símbolos-no-terminales)
  - [1.2. Sintáxis](#12-sintáxis)
    - [1.2.1. Precedencia](#121-precedencia)
    - [1.2.2. Producciones](#122-producciones)

# 1. Gramática de Simple MAT

## 1.1. Alfabeto
### 1.1.1. Símbolos terminales
#### 1.1.1.1. Expresiones regulares

| Token                   |         Patrón         |
| ----------------------- | :--------------------: |
| operador_suma           |           +            |
| operador_resta          |           -            |
| operador_multiplicacion |           *            |
| operador_division       |           /            |
| operador_resto          |           %            |
| numero                  |          \d+           |
| id                      | [a-zA-Z_][a-zA-Z_0-9]* |

#### 1.1.1.2. Palabras reservadas

| Token            | Patrón |
| ---------------- | ------ |
| reservada_inicio | INICIO |
| reservada_fin    | FIN    |

### 1.1.2. Símbolos no terminales

| Token       | Descripción                                       |
| ----------- | ------------------------------------------------- |
| INIT        | Estado inicial de la sintáxis                     |
| EXPRESSIONS | Lista de expresiones separadas por salto de linea |
| E           | Cualquier expresión                               |

## 1.2. Sintáxis

### 1.2.1. Precedencia
Precedencia de operadores de más a menos:

| Precedencia | Operador                                   | Asociatividad |
| :---------: | ------------------------------------------ | ------------- |
|     11      | Agrupacion                                 | Ninguna       |
|     10      | Acceso a arreglo                           | Izquierda     |
|      9      | Llamada a función                          | Izquierda     |
|      8      | Negación unaria, not                       | Derecha       |
|      7      | Potencia                                   | Derecha       |
|      6      | Multiplicación, división, módulo           | Izquierda     |
|      5      | Suma, resta                                | Izquierda     |
|      4      | Menor, menor o igual, mayor, mayor o igual | Izquierda     |
|      3      | Igualación, diferenciación                 | Izquierda     |
|      2      | And                                        | Izquierda     |
|      1      | Or                                         | Izquierda     |


### 1.2.2. Producciones
```ru
Símbolo inicial = INITIAL

INITIAL : reservada_inicio EXPRESSIONS reservada_fin

EXPRESSIONS : EXPRESSIONS E
            | E

E : E operador_suma E
  | E operador_resta E
  | E operador_multiplicacion E
  | E operador_division E
  | E operador_resto E
  | id
  | numero
```
