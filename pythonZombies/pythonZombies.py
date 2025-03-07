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
    def __init__(self, roomNumber):
        self.sensor = False
        self.roomNumber = roomNumber
    def activateSensor(self):
        self.sensor = True
    def resetSensor(self):
        self.sensor = False

class Floor:
    def __init__(self, floorNumber, numberOfRooms):
        self.floorNumber = floorNumber
        self.rooms = [Room(i) for i in range(numberOfRooms)]
    def getRooms(self):
        return[str(room) for room in self.rooms]

class Building:
    def __init__(self, numberOfFloors, roomsPerFloor):
        self.floors = [Floor(i, roomsPerFloor) for i in range(numberOfFloors)]

sensorLog = []

def createBuilding():
    while True:
        try:
            numberOfFloors = int(input("Ingrese numero de pisos: "))
            roomsPerFloor = int(input("Ingrese numero de habitaciones por piso: "))
            if numberOfFloors <= 0 or roomsPerFloor <=0:
                print("Infgrese un numero valido")
                continue
            building = Building(numberOfFloors, roomsPerFloor)

            print(f"Edificio creado con {numberOfFloors} pisos y {roomsPerFloor} habitaciones por piso.")
            return building

        except ValueError:
            print("Por favor, ingrese un número válido.")

def showActiveSensors(building):
    print("Sensores en alerta:")

    activeSensors = []

    for floor in building.floors:
        for room in floor.rooms:
            if room.sensor:
                activeSensors.append((floor.floorNumber, room.roomNumber))

    if not activeSensors:
        print("no hay sensores en alerta")
    else:
        for floorNumber, roomNumber in activeSensors:
            print(f"\nHabitacion: {roomNumber+1} del piso {floorNumber+1}")

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
            
            floorIndex = floorNumber - 1
            roomIndex = roomNumber - 1

            if floorIndex < 0 or floorIndex >= len(building.floors):
                print(f"Número de piso inválido. Debe estar entre 0 y {len(building.floors) - 1}")
                continue
                
            floor = building.floors[floorIndex]
            if roomIndex < 0 or roomIndex >= len(floor.rooms):
                print(f"Número de habitación inválido. Debe estar entre 0 y {len(floor.rooms) - 1}")
                continue
                
            room = floor.rooms[roomIndex]
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
        roomsToInfect.append((0, 0))
    else:
        for floorIndex, floor in  enumerate(building.floors):
            for roomIndex, room in enumerate(floor.rooms):
                if room.sensor:
                    if roomIndex > 0:
                        roomsToInfect.append((floorIndex, roomIndex-1))
                    if roomIndex < len(floor.rooms) - 1:
                        roomsToInfect.append((floorIndex, roomIndex+1))
                    if floorIndex > 0:
                        roomsToInfect.append((floorIndex -1, roomIndex))
                    if floorIndex < len(building.floors) -1:
                        roomsToInfect.append((floorIndex+1, roomIndex)) 

    for floorIndex, roomIndex in roomsToInfect:
        targetRoom = building.floors[floorIndex].rooms[roomIndex]
        if not targetRoom.sensor:
            targetRoom.activateSensor()
    print("Avanzo la infeccion, estas son las habitaciones con zombies: ")
    activeSensors = showActiveSensors(building)
    
def main():
    building = None

    while True:
        print("--- Menu ---")
        print("[1]. Configurar Edificio")
        print("[2]. Limpiar Habitacion")
        print("[3]. Avanzar la simulacion")
        print("[4]. Generar Log de sensores")
        print("[5]. Salir")

        opcion = input("Seleccione una opcion: ")

        if opcion == "1": #crear building
            building = createBuilding()
            FirstAdvance = True

        elif opcion == "2": #limpiar sensor
            if building:
                deactivateSensor(building)
            else:
                print("Primero debe configurar el edificio")

        elif opcion == "3": #avanzar simulacion
            if building:
                advanceSimulation(building, FirstAdvance)
                if FirstAdvance:
                    FirstAdvance = False  # After first advance, set flag to false
            else:
                print("Primero debe configurar el edificio.")      

        elif opcion == "4": #crear json
            print("Funcionalidad: Generar log de sensores (Pendiente)")

        elif opcion == "5": # cerrar
            print("Saliendo del programa...")
            break
        else:
                print("Opción inválida. Intente de nuevo.")

if __name__ == "__main__":
    main()
