phone_book = {
    "1111111111": "Amal",
    "2222222222": "Mohammed",
    "3333333333": "Khadijah",
    "4444444444": "Abdullah",
    "5555555555": "Rawan",
    "6666666666": "Faisal",
    "7777777777": "Layla"
}
#check number validation
#print(phone_book[number_val])
#print(phone_book.values())
#Number_validation and search
def number_validation():
    number_val = input('Enter the number: ')
    if len(number_val) == 10:
        if number_val in phone_book:
            print("The name is ", phone_book[number_val])
        elif number_val != phone_book :
            print('Sorry, the number is not found')

    else:
        print('This is invalide number')
#search whit name=value

def find_number_by_name():
    name = input("Enter the name:")
    for number, owner in phone_book.items():
        if owner == name:
            print("The Number is ", number)
            return
    print("Sorry, the name is not found")

#number_validation(1)
#find_number_by_name()
#add new name and number
def add_new_data():
    new_keys = input('Enter the new number: ')
    if len(new_keys) != 10 or not new_keys.isdigit():
        print("Invalid number!")
        return
    new_value = input('Enter your name: ')
    phone_book[new_keys] = new_value
    print("✅ Contact added successfully!")
    print("Updated dictionary:", phone_book)

#add_new_data()
def main_menu():
    while True:
        print("\n=== Phone Book Menu ===")
        print("1. Search by number")
        print("2. Search by name")
        print("3. Add new contact")
        print("0. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            number_validation()
        elif choice == "2":
            find_number_by_name()
        elif choice == "3":
            add_new_data()
        elif choice == "0":
            print("Goodbye!")
            break
        else:
            print("❌ Invalid choice, try again!")

# Run the program
if __name__ == "__main__":
    main_menu()


