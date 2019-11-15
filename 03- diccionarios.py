def main():
    calificaciones = {}
    calificaciones['matematicas'] = 10
    calificaciones['letras'] = 8
    calificaciones['letras'] = 9
    calificaciones['fisica'] = 7
    suma_de_notas = 0

    for key,value in calificaciones.items():
        print('{} nota: {}'.format(key,value))

    for nota in calificaciones.values():
        suma_de_notas += nota

    average = suma_de_notas / len(calificaciones.items())
    print('')
    print('El promedio de notas es {}'.format(round(average,2)))

if __name__ == "__main__":
    main()