cars = ['audi','bmw,','subaru','toyota']
for car in cars :
    if car == 'bmw':
        print(car.upper())
    else:
        print(car.title())

        age = 12
        if age<4 :
            print("입장료 0$")
        elif age<18 :
            print("입장료 25$")
        
        else:
            print("입장료 40$")


available_toppings = ['mushrooms','olives','green pappers', 'pepperoni', 'pineapple', 'extra cheese']
requested_toppings = ['mushrooms', 'french fries', 'extra cheese']

for requested_topping in requested_toppings:
    if requested_topping in available_toppings:
        print(f"Adding{requested_topping}.")
    else:
        print(f"Sorry, we don't have {requested_topping}.")

print("\nFinished making your pizza!")