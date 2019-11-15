# Las tuplas son una secuencia de valores indexada por enteros
# similares a las listas, con la gran diferencia de que son inmutables
# Las tuplas se crean separando los valores con comas (1,2,3,4)

# de un solo valor
mi_tupla = (1,) 

# varios valores
mi_tupla2 = (2,3,4,5)


# Ejemplo de uso


# Verificar los valores repetidos

"""
"abacabad" c
"abacabaabacaba" _
"abcdefghijklmnopqrstuvwxyziflskecznslkjfabe" d
"bcccccccccccccyb" y
"""

def first_not_repeating_char(char_sequence):
    seen_letters = {}

    for idx, letter in enumerate(char_sequence):
        if letter not in seen_letters:
            # si la ve por primera ver agrega a la lista una tupla
            seen_letters[letter] = (idx, 1)
        else:
            seen_letters[letter] = (seen_letters[letter][0], seen_letters[letter][1] + 1)

    final_letters = []
    for key, value in seen_letters.items():
        if value[1] == 1:
            final_letters.append( (key, value[0]) )

    # ordena los valores segun el segundo indice de cada tupla guardada en la
    not_repeated_letters = sorted(final_letters, key=lambda value: value[1])

    if not_repeated_letters:
        return not_repeated_letters[0][0]
    else:
        return '_'


if __name__ == '__main__':
    char_sequence = str(input('Escribe una secuencia de caracteres: '))

    result = first_not_repeating_char(char_sequence)

    if result == '_':
        print('Todos los caracteres se repiten.')
    else:
        print('El primer caracter no repetido es: {}'.format(result))