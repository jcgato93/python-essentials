# Clases y métodos

- Los obsjetos tiene atributos que se pueden definir al momento de inicializar un nuevo objeto o directamente en la instancia.

- Las clases puden tener variables de clase,variables de instancia y variables locales.

- Aunque Python no tiene el concepto de variables privadas integrado al lenguaje, es practica comun definirlas con un guion bajo.

- isinstance y hasattr

- Los métodos son como funciones que tienen únicamente en el contexto de una clase.

- Al igual que las variables, los métodos privados se
definene con un guión bajo.

- la encapsulación es un concepto clave de la programación orientada a objetos.
        
        la forma practica  de aplicar este principio es declarar todas las variables y metodos como privados a menos de que sea necesrio exponerlos a nuestros programadores

- Un metodo clave que casi todas las clases deben tener es  \_init_

- Otro es \_str_

- Existen varios tipos de métodos ,estáticos, de clase, de instancia ,getters y setters


##  Definir clase

```py
# -*- coding: utf-8 -*-


class Lamp:
    _LAMPS = ['''
          .
     .    |    ,
      \   '   /
       ` ,-. '
    --- (   ) ---
         \ /
        _|=|_
       |_____|
    ''',
    '''
         ,-.
        (   )
         \ /
        _|=|_
       |_____|
    ''']

    def __init__(self, is_turned_on):
        self._is_turned_on = is_turned_on

    def turn_on(self):
        self._is_turned_on = True
        self._display_image()

    def turn_off(self):
        self._is_turned_on = False
        self._display_image()

    def _display_image(self):
        if self._is_turned_on:
            print(self._LAMPS[0])
        else:
            print(self._LAMPS[1])

```

