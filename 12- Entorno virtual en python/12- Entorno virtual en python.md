# Paquetes de terceros

- PyPi (python package index) es un reposiorio de paquetes de terceros
que se pueden utilizar en proyectos de python

- Para instalar un paquete , es necesario utilizar la herramienta pip.

- La forma de instalar un paquete es ejecutar el comando:

        pip install <nombre_paquete>

- Tambien se puede agrupar la instalacion de varios archivos  a la vez con el
archivo requirements.txt con el comando:

                $ pip install -r requirements.txt

# Ambientes virtuales 

- Es una buena práctica crear un ambiente virtual por cada proyecto de python en el que se trabaje.

- Esto evita conflictos de paquetes en el intérprete principal.

- pip install virtualenv

- virtualenv venv

- source venv/bin/active

- deactivate


# Como instalar pip

- Descargar el archivo get-pip.py

            curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py

- Ejecutar el siguiente comando en el directorio donde se descargo el archivo

            python get-pip.py



# Crear y ejecutar ambiente virtual

- Crear ambiente

        $ virtualenv <nombre_entorno> // por convencion suele ser venv

- Ejecutar ambiente

        // linux
        $ source venv\bin\active

        // windows
        $ start <ambiente>\Scripts\activate

        ó

        $ <ambiente>\Scripts\activate


