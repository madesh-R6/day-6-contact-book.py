contacts = {}
def add_contacts():
    name=input("enter a name :")
    phone=input("enter a phone number :")
    contacts[name]=phone
    print("contacts saved")
def view_contacts():
    if not contacts:
        print("no contact saved")
    else:
        for name ,phone in contacts.items():
          print(name,"-",phone)
def save_to_file():
    with open("contacts.txt","w") as f:
        for name ,phone in contacts.items():
            f.write(f"{name}:{phone}\n")
    print("contacts saved to file")
def menu():
    while True:
        print("/n---Contact book---")
        print("1. Add contacts")
        print("2. view contacts")
        print("3. save_to_file")
        print("4. Exit")
        choice=input("choose an option:")
        if choice =="1":
            add_contacts()
        elif choice=="2":
            view_contacts()
        elif choice=="3":
            save_to_file()
        elif choice =="4":
            break
        else:
            print("invalid choice!")
menu()