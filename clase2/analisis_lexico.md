# Código fuente

```java

public class MiClase {

    public static void main(String[] args) {
        char ch = 'a';
        boolean valor = 'a' == ch;
        int ascii = ch;
        System.out.println("El valor ASCII de " + ch + " es: " + ascii);
    }

}

```


# Lexemas

- public
- class
- MiClase
- {
- public
- static
- void
- main
- (
- String
- [
- ]
- args
- )
- {
- char
- ch
- =
- 'a'
- ;
- int
- ascii
- =
- ch
- ;
- System
- .
- out
- .
- println
- (
- "El valor de "
- +
- ch
- +
- " es: "
- +
- ascii
- )
- ;
- }
- }

# Definición de tokens

| Token               | Descripción                          | Patrón                              |
| ------------------- | ------------------------------------ | ----------------------------------- |
| reservada_public    | Palabra reservada                    | public                              |
| reservada_class     | Palabra reservada                    | class                               |
| identificador       | Cualquier identificador del lenguaje | (_\|[a-zA-Z])(_\|[a-zA-Z0-9])       |
| llaveA              | Llave abierta                        | {                                   |
| llaveB              | Llave cerrada                        | }                                   |
| reservada_static    | Palabra reservada                    | static                              |
| reservada_void      | Palabra reservada                    | void                                |
| parA                | Paréntesis abierto                   | (                                   |
| parB                | Paréntesis cerrado                   | )                                   |
| tipo_string         | Tipo de dato string                  | String                              |
| tipo_char           | Tipo de dato char                    | char                                |
| tipo                | Tipo de dato                         | tipo_string\|tipo_int\|tipo_boolean |
| corA                | Corchete abierto                     | [                                   |
| corB                | Corchete cerrado                     | ]                                   |
| operador_igualacion | Operador de igualación               | ==                                  |
| operador_igual      | Operador de asignación               | =                                   |
| operador_suma       | Operador de suma                     | +                                   |
| dato_char           | Dato de tipo char                    | '[^']\|(\')'                        |
| dato_string         | Dato de tipo string                  | "([^"]\|(\"))*"                     |
| dato                | Dato de cualquier tipo               | dato_char\| dato_string \| dato_int |
| punto_coma          | Punto y coma                         | ;                                   |
| punto               | Operador                             | .                                   |

# Análisis léxico

| Lexema         | Token            |
| -------------- | ---------------- |
| public         | reservada_public |
| class          | reservada_class  |
| MiClase        | identificador    |
| {              | llaveA           |
| public         | reservada_public |
| static         | reservada_static |
| void           | reservada_void   |
| main           | identificador    |
| (              | parA             |
| String         | tipo_string      |
| [              | corA             |
| ]              | corB             |
| args           | identificador    |
| )              | parB             |
| {              | llaveA           |
| char           | tipo_char        |
| ch             | identificador    |
| =              | operador_igual   |
| 'a'            | dato_char        |
| ;              | punto_coma       |
| int            | tipo_int         |
| ascii          | identificador    |
| =              | operador_igual   |
| ch             | identificador    |
| ;              | punto_coma       |
| System         | identificador    |
| .              | punto            |
| out            | identificador    |
| .              | punto            |
| println        | identificador    |
| (              | parA             |
| "El valor de " | dato_string      |
| +              | operador_suma    |
| ch             | identificador    |
| +              | operador_suma    |
| " es: "        | dato_string      |
| +              | operador_suma    |
| ascii          | identificador    |
| )              | parB             |
| ;              | punto_coma       |
| }              | llaveB           |
| }              | llaveB           |


