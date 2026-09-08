import questionary
from auth import * 
from deliveries import *
def get_name():
    name=input("Enter your name: ")
    return name

def get_password():
    password=input("Enter your password: ")
    return password

def get_package_id():
    package_id=input("enter package id: ")
    return package_id

def get_new_status():
    new_status=input("enter new status: ")
    return new_status

def menu():
    while True:
        choice = questionary.select(
            "=== SPACE DELIVERY MANAGER ===",
            choices=[
                "Register",
                "Login",
                "Exit"]).ask()

        if choice == "Register":
            print("Register selected")

            for n in range(3):

                name = get_name()
                password = get_password()

                if register_user(name, password):
                    print("Register complete!")
                    break


        elif choice == "Login":
            print("Login selected")

            name = get_name()
            password = get_password()
            user = login_user(name, password)
            if user:
                while True:
                    print(f"Welcome {user.username}")
                    choice=questionary.select(
                            "Choose your action: ",choices=[
                            "Create delivery",
                            "Show my deliveries",
                            "Update delivery status",
                            "Delete delivery",
                            "Logout"]).ask()
                        
                    
                    if choice == "Create delivery":
                        package_name, dest, weight = get_delivery_info()

                        delivery = create_delivery(user,package_name, dest, weight)
                        if not delivery:
                            return False 
                        else:
                            print("Delivery created sussefully!!!")

                    elif choice == "Show my deliveries":
                        result = get_user_deliveries(user)
                        if result:
                            print(result)

                    elif choice == "Update delivery status":
                        new_status=get_new_status()
                        id=get_package_id()
                        if update_delivery_status(user,id,new_status):
                            print("delivery updated succesfully")
                        else:
                            print("update faild")

                    elif choice == "Delete delivery":
                        id=get_package_id()
                        if delete_delivery(user,id):
                            print("delivery deleted succecfully")
                        else:
                            print("delete faild")
                    
                    elif choice == "Logout":
                        break
            else:
                print("not valid name or password!")
                    

        elif choice == "Exit":
            print("Goodbye!")
            break



