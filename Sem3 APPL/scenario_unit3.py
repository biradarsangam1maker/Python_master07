# Read mobile records from CSV file

filename = "mobiles.csv"

mobiles = []

with open(filename, "r") as file:
    header = file.readline().strip().split(",")

    for line in file:
        data = line.strip().split(",")

        mobile = {}

        for i in range(len(header)):
            mobile[header[i]] = data[i]

        mobiles.append(mobile)


# Display all mobile records
def display_mobiles():
    print("\n--- All Mobile Records ---")

    for mobile in mobiles:
        print("Mobile ID :", mobile["MobileID"])
        print("Brand     :", mobile["Brand"])
        print("Model     :", mobile["Model"])
        print("Price     :", mobile["Price"])
        print("RAM       :", mobile["RAM"])
        print("------------------------")


# Search mobile by brand
def search_by_brand():
    brand = input("Enter brand name: ")

    found = False

    for mobile in mobiles:

        if mobile["Brand"].lower() == brand.lower():

            print("\nMobile Found")
            print("Mobile ID :", mobile["MobileID"])
            print("Brand     :", mobile["Brand"])
            print("Model     :", mobile["Model"])
            print("Price     :", mobile["Price"])
            print("RAM       :", mobile["RAM"])
            print("------------------------")

            found = True

    if found == False:
        print("No mobile found.")


# Main menu
while True:

    print("\n===== MOBILE STORE RECORD SYSTEM =====")
    print("1. Display all mobile records")
    print("2. Search mobile by brand")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        display_mobiles()

    elif choice == "2":
        search_by_brand()

    elif choice == "3":
        print("Program terminated.")
        break

    else:
        print("Invalid choice.")