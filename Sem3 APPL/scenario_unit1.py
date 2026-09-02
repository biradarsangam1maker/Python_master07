# Vehicle Showroom Management System
class Vehicle:
    def __init__(self, vehicle_number, brand, price):
        self.vehicle_number = vehicle_number
        self.brand = brand
        self.price = price

    def category(self):
        if self.price >= 1000000:
            return "Luxury"
        else:
            return "Economy"

    def display(self):
        print("Vehicle Number :", self.vehicle_number)
        print("Brand           :", self.brand)
        print("Price           :", self.price)
        print("Category        :", self.category())
        print("-" * 35)


class Showroom:
    def __init__(self):
        self.vehicles = []

    def add_vehicle(self):
        # Enter details of 4 vehicles
        for i in range(4):
            print(f"\nEnter details for Vehicle {i + 1}")

            vehicle_number = input("Enter Vehicle Number: ")
            brand = input("Enter Brand: ")
            price = float(input("Enter Price: "))

            vehicle = Vehicle(vehicle_number, brand, price)
            self.vehicles.append(vehicle)

            print("Vehicle added successfully!")

        print("\nAll 4 vehicles added successfully!\n")

    def display_all(self):
        if not self.vehicles:
            print("No vehicles available.\n")
            return

        print("\n--- All Vehicles ---")

        for vehicle in self.vehicles:
            vehicle.display()

    def display_luxury(self):
        print("\n--- Luxury Vehicles ---")

        found = False

        for vehicle in self.vehicles:
            if vehicle.category() == "Luxury":
                vehicle.display()
                found = True

        if not found:
            print("No luxury vehicles available.\n")

    def display_economy(self):
        print("\n--- Economy Vehicles ---")

        found = False

        for vehicle in self.vehicles:
            if vehicle.category() == "Economy":
                vehicle.display()
                found = True

        if not found:
            print("No economy vehicles available.\n")


# Main Program

showroom = Showroom()

while True:

    print("\n===== VEHICLE SHOWROOM MANAGEMENT SYSTEM =====")
    print("1. Add 4 Vehicles")
    print("2. Display All Vehicles")
    print("3. Display Luxury Vehicles")
    print("4. Display Economy Vehicles")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        showroom.add_vehicle()

    elif choice == "2":
        showroom.display_all()

    elif choice == "3":
        showroom.display_luxury()

    elif choice == "4":
        showroom.display_economy()

    elif choice == "5":
        print("\nThank you for using Vehicle Showroom Management System!")
        break

    else:
        print("\nInvalid choice! Please try again.")
