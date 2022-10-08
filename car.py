class Car(audi):

def __init__(audi,model,color,company,speed_limit):
    audi.color=color
    audi.company=company
    audi.speed_limit=speed_limit
    audi.model=model

def start(audi):
    print("started")

def stop(audi):
    print("stopped")

def accelarate(audi) :
    print("accelarating...")
    "accelarator functionality here"

def change_gear(audi,gear_type):
    print("gear changed")
    "gear space functionality here"

audi=Car("A6","black","audi",80)
