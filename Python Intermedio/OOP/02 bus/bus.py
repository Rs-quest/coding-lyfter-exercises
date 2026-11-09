class Person:
    def __init__(self, name):
        self.name = name


class Bus:
    max_passengers = 15

    def __init__(self):
        self.passengers = []

    def add_passenger(self, person):
        if len(self.passengers) < self.max_passengers:
            self.passengers.append(person)
            print(f"{person.name} ha subido al bus.")
        else:
            print("El bus está lleno.")

    def remove_passenger(self, person):
        if person in self.passengers:
            self.passengers.remove(person)
            print(f"{person.name} ha bajado del bus.")
        else:
            print(f"{person.name} no está en el bus.")


# Agregué un programa porque no se especificaba en la tarea pero me parecía extraño dejar solo
# las clases

bus = Bus()

while True:
    print("\n¿Qué deseas hacer?")
    print("1. Subir pasajero")
    print("2. Bajar pasajero")
    print("3. Ver pasajeros")
    print("4. Salir")

    option = input("Selecciona una opción: ")

    if option == "1":
        name = input("Nombre del pasajero: ")
        person = Person(name)
        bus.add_passenger(person)

    elif option == "2":
        name = input("¿Quién desea bajar? ")

        passenger_to_remove = None

        for passenger in bus.passengers:
            if passenger.name.lower() == name.lower():
                passenger_to_remove = passenger
                break

        if passenger_to_remove:
            bus.remove_passenger(passenger_to_remove)
        else:
            print("Ese pasajero no está en el bus.")

    elif option == "3":
        print(f"Pasajeros a bordo: {len(bus.passengers)}")
        for passenger in bus.passengers:
            print(passenger.name)

    elif option == "4":
        print("Finalizando programa.")
        break

    else:
        print("Opción inválida.")