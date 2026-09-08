from models import * 
def get_delivery_info():
    name=input("enter packege name: ")
    dest=input("enter destination planet: ")
    weight=float(input("enter pckage weight: "))
    return name,dest,weight

def create_delivery(user: User ,package_name: str,destination:str,weight:float):
    try:
        if not package_name.strip():
            raise ValueError("package name must not be empty")
        if not destination.strip():
            raise ValueError("destination must not be empty")
        if weight<=0:
            raise ValueError("weight must be higher then zero")
    except ValueError as error:
        print(f"Delivery not created: {error}")
    delvery=Delivery.create(package_name=package_name,destination=destination,weight=weight,owner=user)
    return delvery

def get_user_deliveries(user: User):
    result=list(Delivery.select().where(Delivery.owner==user).dicts())
    if result==[]:
        print("You do not have any deliveries")
        return
    return result

def update_delivery_status(user:User,delivery_id: int, new_status:str):
    valid_statuses=["wating","in transit","delivered","cancelled"]
    if new_status not in valid_statuses:
        print("not valid status")
        return False
    delivery=Delivery.get_or_none(
        (Delivery.id==delivery_id)and(Delivery.owner==user)
    )
    if not delivery:
        print("delivery not found")
        return False
    delivery.status=new_status
    delivery.save()
    return True

def delete_delivery(user: User,delivery_id:int):
    delivery=Delivery.get_or_none(
        (Delivery.id==delivery_id)and(Delivery.owner==user)
    )
    if not delivery:
        print("delivery not found!")
        return False
    delivery.delete_instance()
    return True
