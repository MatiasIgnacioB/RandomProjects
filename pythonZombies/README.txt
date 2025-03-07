como ejecutar aplicacion:
1-Instalar Python3
2-clonar repositorio
3-navegar a directorio donde se clono el repositorio
4-ejecutar usando python3 pythonZombies.py en terminal
(no se como es el proceso en windows, supongo que parecido)

Explicacion de las clases:
-Building: esta es la clase que contiene todas las otras en el problema y la unica que se inicializa como tal.
building tiene un arreglo de floors y ningun metodo mas alla del constructor, ya que las funcionalidades requeridas solo se preocupan del numero de floors y rooms, o del estado de una alarma.

-Floor: Al igual que con building, floor solo contiene un arreglo de rooms y el numero correspondiente al objeto floor. Y tambien no se requiere ningun otro tipo de metodo que el constructor para este problema en particular.

-Room: Room es la clase mas compleja en comparacion con las otras, simplemente por la existencia de los sensores. 
Como se asume que el edificio comienza vacio, y los sensores solo se activan (True) si hay zombies en una habitacion, entonces todos los sensores/alarmas se inicializan como False.
En esta clase si deben existir metodos mas alla del constructor, solo porque se debe cambiar el estado del sensor.

Instrucciones de menu:
considero que el menu es bien claro, pero en caso de que no:
al iniciar el programa se le presenta al usuario con todas las opciones disponibles, el numero denrto de [] indica el valor que debe ingresar el usuario para usar la funcionalidad correspondiente.
[1] - es la funcion que permite configurar el edificio, al elegirla, se le pedira al usuario por el numero de pisos que quiere para este edificio y luego, el numero de habitaciones por piso.
ejecutar esta funcion mas de una vez sobreescribira los edificios creados anteriormente

[2] - "limpiar la habitacion" presenta primero al usuario con un resumen de las habitaciones que tienen sensores activados (True, con zombies en la habitacion), luego se le pide al usuario insertar el piso y numero de habitacion de cuyo sensor quiere setear como falso (eliminando los zombies de la habitacion).
en caso de que el inmput del usuario sea una habitacion con el sensor desactivado, entonces se le dice que su input fue un error y se le pregunta denuevo.
Otro caso es que se seleccione esta opcion sin antes haber creado un edificio, lo que se le notificara al usuario y se volvera al menu principal.

[3] - es la funcion que se encarga de avanzar la simulacion, al igual que con la opcion anterior, esta falla si es que el edificio no a sido creado aun.
de la forma que funciona es que al usar esta opcion por primera vez, zombies entraran al edificio, infectando la habitacion 1 del piso 1, con usos subsecuentes, los zombies se moveran a habitaciones adyacentes, en las 4 direcciones, activando los sensores de estas habitaciones.

[4] - se encarga de generar el log en formato json (pendiente)

[5] - salir, simplemente cierra el programa.

Que sigue?
- terminar README
- representacion visual del edificio
- fusionar numero del floor y de la room
- que solo el main interactue con el user
- posibilidad de que una room no exista / barricada(?)
- usar timestamps en el log
- el log en json como tal
- No es necesario que el sensor tenga un metodo para activarlo y otro para desactivarlo. cambiar por un metodo que simplemente niega el valor del sensor.
- formatear mas lindo el README (?)