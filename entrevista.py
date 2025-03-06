# Building con Floors y Floors con Rooms
# Sensor con 2 estados
# "Simulation: Orquesta la lógica de la propagación zombi y muestra el estado general."

# funcion: inicializar el building con floors y rooms
# funcion: mostrar estado de sensors
# funcion: avanzar turno, zombies se mueven entre habitaciones adjacentes
# rooms en el mismo floor tienen numeros contiguos
# la adyacencia es vertical tmb
# zombies siempre se mueven a todas las adyacentes cuando lo hacen, como explosion
# room con zombies = sensor = 1

# funcion: configurar building
# funcion: "limpiar" room
# funcion: cerrar programa
# funcion: buildiar json con el log de sensores

# """Back-End"""
class Room:
    def __init__(self, roomNumber, sensor):
        self.sensor = False
        self.roomNumber = roomNumber
    def activateSensor(self):
        self.sensor = True
    def resetSensor(self):
        self.sensor = False

class Floor:
    def __init__(self, floorNumber, numberOfRooms):
        self.floorNumber = floorNumber
        self.rooms = [Rooms(i) for i in range(numberOfRooms)]
    def getRooms(self):
        return[str(room) for room in self.rooms]

class Building:
    def __init(self, numberOfFloors, roomsPerFloor):
        self.floors = [Floor(i, roomsPerFloor) for i in range(numberOfFloors)]

def createBuilding():
    while True:
        try:
            numberOfFloors = int(input("Ingrese numero de pisos: "))
            roomsPerFloor = int(input("Ingrese numero de habitaciones por piso: "))
            if numberOfRooms <= 0 or roomsPerFloor <=0:
                print("Infgrese un numero valido")
                continue
            building = Building(numberOfFloors, roomsPerFloor)

            print(f"Edificio creado con {num_floors} pisos y {rooms_per_floor} habitaciones por piso.")
            return building

        except ValueError:
            print("Por favor, ingrese un número válido.")

def showActiveSensors(building):
    print("Sensores en alerta:")

    activeSensors = []

    for floor in building.floors:
        for room in floor.rooms:
            if room.sensor:
                activeSensors.append((floor.number, room.number))

    if not activeSensors:
        print("no hay sensores en alerta")
    else:
        for floorNumber, roomNumber in activeSensors:
            print(f"\nHabitacion: {roomNumber} del piso {floorNumber}")

    return activeSensors

def deactivateSensor(building):
    activeSensors = showActiveSensors(building)
    if not activeSensors:
        print("No hay sensores activos para desactivar.")
        return
        
    while True:
        try:
            floorNumber = int(input("Ingrese número de piso de la habitación: "))
            roomNumber = int(input("Ingrese número de habitación para desactivar el sensor: "))
            
            if floorNumber < 0 or floorNumber >= len(building.floors):
                print(f"Número de piso inválido. Debe estar entre 0 y {len(building.floors) - 1}")
                continue
                
            floor = building.floors[floorNumber]
            if roomNumber < 0 or roomNumber >= len(floor.rooms):
                print(f"Número de habitación inválido. Debe estar entre 0 y {len(floor.rooms) - 1}")
                continue
                
            room = floor.rooms[roomNumber]
            if not room.sensor:
                print(f"El sensor en la habitación {roomNumber} del piso {floorNumber} no está activo.")
                continue
                
            room.resetSensor()
            print(f"Sensor en la habitación {roomNumber} del piso {floorNumber} desactivado exitosamente.")
            return
            
        except ValueError:
            print("Por favor, ingrese un número válido.")
    
def advanceSimulation(building, isFirstAdvance = False):
    roomsToInfect = []

    if isFirstAdvance:
        print("Zombies entraron al edificio, (habitacion 1 del piso 1)")
        roomsToInfect.append((0, 0))
    else:
        for floorIndex, floor in 

    for floorIndex, roomIndex in roomsToInfect:
        targetRoom = building.floors[floorIndex].rooms[roomIndex]
        if not room.sensor:
            room.activateSensor()

def main():
    while True:
        print("--- Menu ---")
        print("[1]. Configurar Edificio")
        print("[2]. Limpiar Habitacion")
        print("[3]. Generar Log de sensores")
        print("[4]. Salir")

        opcion = input("Seleccione una opcion: ")

        if opcion == "1": #crear building
            building = createBuilding()

        elif opcion == "2": #limpiar sensor
            if building:
                deactivateSensor(building)
            else:
                print("Primero debe configurar el edificio")

        elif opcion == "3": #avanzar simulacion
            print("Avanzar Simulacion")
            if building:
                ########################
            else:
                print("Primero debe configurar el edificio")
        elif opcion == "4": #crear json
            print("Funcionalidad: Generar log de sensores (Pendiente)")

        elif opcion == "5": # cerrar
            print("Saliendo del programa...")
            break
        else:
                print("Opción inválida. Intente de nuevo.")

if __name__ == "__main__":
    main()
