from Car import Car
from Truck import Truck
from Motorcycle import Motorcycle


def save_fleet_to_file(vehicles, filename):
    with open(filename, "w", encoding="utf-8") as file:
        for vehicle in vehicles:
            if isinstance(vehicle, Car):
                line = "Car, " + vehicle.vid + ", " + vehicle.model + ", " + str(vehicle.year) + ", " + vehicle.fuel_type + ", " + str(vehicle.doors)
            elif isinstance(vehicle, Truck):
                line = "Truck, " + vehicle.vid + ", " + vehicle.model + ", " + str(vehicle.year) + ", " + str(vehicle.max_load) + ", " + str(vehicle.axles)
            elif isinstance(vehicle, Motorcycle):
                line = "Motorcycle, " + vehicle.vid + ", " + vehicle.model + ", " + str(vehicle.year) + ", " + str(vehicle.engine_cc) + ", " + vehicle.type

            file.write(line + "\n")


def load_fleet_from_file(filename):
    vehicles = []

    with open(filename, "r", encoding="utf-8") as file:
        for line in file:
            parts = line.strip().split(", ")

            vehicle_type = parts[0]
            vid = parts[1]
            model = parts[2]
            year = int(parts[3])

            if vehicle_type == "Car":
                fuel_type = parts[4]
                doors = int(parts[5])
                vehicles.append(Car(vid, model, year, fuel_type, doors))

            elif vehicle_type == "Truck":
                max_load = int(parts[4])
                axles = int(parts[5])
                vehicles.append(Truck(vid, model, year, max_load, axles))

            elif vehicle_type == "Motorcycle":
                engine_cc = int(parts[4])
                motorcycle_type = parts[5]
                vehicles.append(Motorcycle(vid, model, year, engine_cc, motorcycle_type))

    return vehicles


def main():
    fleet = [
        Car("V001", "Tesla Model 3", 2023, "Electric", 4),
        Truck("T101", "Volvo FH16", 2019, 25000, 6),
        Motorcycle("M301", "Yamaha R1", 2024, 998, "Sport"),
        Car("V002", "Toyota Corolla", 2018, "Petrol", 4),
        Truck("T102", "Mercedes Actros", 2021, 18000, 4),
        Motorcycle("M302", "Harley Davidson", 2015, 1200, "Cruiser")
    ]

    save_fleet_to_file(fleet, "fleet.txt")

    print("Loading fleet data from 'fleet.txt'...")
    loaded_fleet = load_fleet_from_file("fleet.txt")
    print(str(len(loaded_fleet)) + " vehicles loaded successfully.")

    print("\n--- All Vehicles ---")
    for vehicle in loaded_fleet:
        print(vehicle)

    print("\n--- Recent Vehicles (Last 4 Years) ---")
    for vehicle in loaded_fleet:
        if vehicle.is_new(4):
            print(vehicle)

    print("\n--- Electric Cars Only ---")
    for vehicle in loaded_fleet:
        if isinstance(vehicle, Car) and vehicle.fuel_type == "Electric":
            print(vehicle)


main()
